from typing import Optional

try:
    import boto3
except ImportError:
    boto3 = None


from launchflow.config import config
from launchflow.resource import Resource
from pydantic import BaseModel


class SecretsManagerSecretConnection(BaseModel):
    secret_id: str


class SecretsManagerSecret(Resource[SecretsManagerSecretConnection]):
    """A Secrets Manager Secret resource.

    **Attributes**:
    - `name` (str): The name of the secret.

    Example usage:
    ```python
    import launchflow as lf
    secret = lf.aws.SecretsManagerSecret("my-secret")
    value = secret.version()
    ```
    """

    def __init__(self, name: str) -> None:
        super().__init__(
            name=name,
            product_name="aws_secrets_manager_secret",
            create_args={},
        )
        self._success_message = f"Set value with `launchflow secrets set --project={config.project} --environment={config.environment} {name} <VALUE>`"

    def version(self, version_id: Optional[str] = None) -> str:
        """Get the secret version from the Secrets Manager.

        Args:
        - `verison_id` (Optional[str]): The version of the secret to get. If not provided, the latest version is returned.

        Returns:
        - The value associated with the secret version.

        Example usage:

        ```python
        import launchflow as lf

        secret = lf.aws.SecertsManager("my-secret")
        value = secret.version()
        ```
        """
        if boto3 is None:
            raise ImportError(
                "boto3 not found. "
                "You can install it with pip install launchflow[aws]"
            )
        connection_info = self.connect()
        sm = boto3.client("secretsmanager")
        if version_id is None:
            value = sm.get_secret_value(SecretId=connection_info.secret_id)
        else:
            value = sm.get_secret_value(
                SecretId=connection_info.secret_id, VersionId=version_id
            )
        return value["SecretString"]

    def add_version(self, payload: str):
        """Adds a new version of the secret to the Secrets Manager.

        Args:
        - `payload` (str): The value to add to the secret.

        Example usage:

        ```python
        import launchflow as lf

        secret = lf.aws.SecertsManager("my-secret")
        secret.add_version("my-new-value")
        ```
        """
        if boto3 is None:
            raise ImportError(
                "boto3 not found. "
                "You can install it with pip install launchflow[aws]"
            )
        connection_info = self.connect()
        sm = boto3.client("secretsmanager")
        sm.put_secret_value(SecretId=connection_info.secret_id, SecretString=payload)
