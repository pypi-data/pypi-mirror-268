import typer
from launchflow.aws.secrets_manager import SecretsManagerSecret
from launchflow.cli.constants import ENVIRONMENT_HELP, PROJECT_HELP
from launchflow.cli.utyper import UTyper
from launchflow.flows.environments_flows import get_environment
from launchflow.flows.project_flows import get_project
from launchflow.gcp.secret_manager import SecretManagerSecret
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

from launchflow.clients import async_launchflow_client_ctx

app = UTyper(help="Commands for managing secrets in LaunchFlow")


@app.command()
async def set(
    resource_name: str = typer.Argument(..., help="Resource to fetch information for."),
    secret_value: str = typer.Argument(..., help="The value to set for the secret."),
    project: str = typer.Option(None, help=PROJECT_HELP),
    environment: str = typer.Option(None, help=ENVIRONMENT_HELP),
):
    """Set the value of a secret managed by LaunchFlow."""

    async with async_launchflow_client_ctx() as client:
        project_info = await get_project(client, project, prompt_for_creation=False)
        environment_info = await get_environment(
            client,
            project=project_info,
            environment_name=environment,
            prompt_for_creation=False,
        )
        resource = await client.resources.get(
            project_name=project_info.name,
            environment_name=environment_info.name,
            resource_name=resource_name,
        )
        add_version_fn = None
        if resource.resource_product == "gcp_secret_manager_secret":

            def add_version_fn():
                secret = SecretManagerSecret(name=resource_name)
                secret.add_version(secret_value.encode("utf-8"))

        elif resource.resource_product == "aws_secrets_manager_secret":

            def add_version_fn():
                secret = SecretsManagerSecret(name=resource_name)
                secret.add_version(secret_value)

        else:
            typer.echo(
                "Only secrets managed by Google Cloud Secret Manager and AWS Secrets Manager are supported."
            )
            raise typer.Exit(1)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            TextColumn("["),
            TimeElapsedColumn(),
            TextColumn("]"),
        ) as progress:
            task = progress.add_task(
                f"Setting secret value for {resource_name}...",
            )
            add_version_fn()
            progress.remove_task(task)
            progress.console.print("[green]✓[/green] Successfully added secret value")
