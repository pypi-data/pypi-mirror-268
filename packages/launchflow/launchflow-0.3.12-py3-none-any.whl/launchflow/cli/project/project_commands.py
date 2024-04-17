import rich
import typer
from launchflow.cli.utils import print_response
from launchflow.cli.utyper import UTyper
from launchflow.config import config
from launchflow.exceptions import LaunchFlowException, LaunchFlowRequestFailure
from launchflow.flows.project_flows import create_project
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

from launchflow.clients import async_launchflow_client_ctx

app = UTyper(help="Interact with your LaunchFlow projects.")


@app.command()
async def list():
    """Lists all current projects in your account."""
    async with async_launchflow_client_ctx() as client:
        projects = await client.projects.list(config.settings.default_account_id)

    print_response(
        "Projects", {"projects": [projects.model_dump() for projects in projects]}
    )


@app.command()
async def get(project_name: str):
    """Get information about a specific project."""
    async with async_launchflow_client_ctx() as client:
        project = await client.projects.get(project_name)

    print_response("Project", project.model_dump())


@app.command()
async def create(
    project_name: str = typer.Argument(None, help="The name of the project to create."),
    account_id: str = typer.Option(
        None,
        help="The account ID to fetch. Of the format `acount_123`. Defaults to the account in your config file.",  # noqa: E501
    ),
):
    """Create a new project in your account."""
    async with async_launchflow_client_ctx() as client:
        try:
            project = await create_project(
                client=client, project_name=project_name, account_id=account_id
            )
        except LaunchFlowException as e:
            e.pretty_print()
            raise typer.Exit(1)

    print_response("Project", project.model_dump())


@app.command()
async def delete(name: str = typer.Argument(..., help="The project name.")):
    """Delete a project."""
    try:
        async with async_launchflow_client_ctx() as client:

            operation = await client.projects.delete(name)
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                TextColumn("["),
                TimeElapsedColumn(),
                TextColumn("]"),
            ) as progress:
                task = progress.add_task("Deleting project...")
                try:
                    async for _ in client.operations.stream_operation_status(
                        operation.id
                    ):
                        pass
                except LaunchFlowRequestFailure as e:
                    if e.status_code != 404:
                        raise e
                except Exception:
                    progress.console.print("[red]✗[/red] Failed to delete project")
                    raise typer.Exit(1)
                finally:
                    progress.remove_task(task)

    except Exception as e:
        typer.echo(e)
        raise typer.Exit(1)

    rich.print("[green]✓[/green] Project deleted.")
