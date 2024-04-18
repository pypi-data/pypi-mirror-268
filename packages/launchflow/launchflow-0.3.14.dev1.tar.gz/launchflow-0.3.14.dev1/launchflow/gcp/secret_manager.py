from launchflow.config import config
from launchflow.resource import Resource
from pydantic import BaseModel


class SecretManagerConnectionInfo(BaseModel):
    secret_name: str


class SecretManagerSecret(Resource[SecretManagerConnectionInfo]):
    """
    A Secret Manager secret resource.

    This creates the container for the secret and allows you to access the secret's value. You will need to manually add a value to the secret.

    Example usage:
    ```python
    import launchflow as lf

    # Docs: https://docs.launchflow.com/reference/gcp-resources/gcp-secret-manager
    api_key = lf.gcp.SecretManagerSecret("api-key")
    ```
    """

    def __init__(self, name: str) -> None:
        super().__init__(
            name=name,
            product_name="gcp_secret_manager_secret",
            create_args={},
        )
        self._success_message = f"Set value with `launchflow secrets set --project={config.project} --environment={config.environment} {name} <VALUE>`"

    def version(self, version: str = "latest") -> bytes:
        """Access a version of the secret.

        Args:
        - `version` (str): The version of the secret to access. Defaults to "latest".

        Returns:
        - The value of the secret as bytes.

        Example usage:

        ```python
        import launchflow as lf

        api_key = lf.gcp.SecretManagerSecret("api-key")
        secret = api_key.version()
        ```
        """
        try:
            from google.cloud import secretmanager
        except ImportError:
            raise ImportError(
                "google-cloud-storage not found. "
                "You can install it with pip install launchflow[gcp]"
            )
        connection_info = self.connect()
        client = secretmanager.SecretManagerServiceClient()
        response = client.access_secret_version(
            name=f"{connection_info.secret_name}/versions/{version}"
        )
        return response.payload.data

    def add_version(self, payload: bytes):
        """Add a version of the secret.

        Args:
        - `payload` (str): The payload to add to the secret.

        Example usage:

        ```python
        import launchflow as lf

        api_key = lf.gcp.SecretManagerSecret("api-key")
        api_key.add_version(open("api-key.txt", "rb").read())
        ```
        """
        try:
            from google.cloud import secretmanager
        except ImportError:
            raise ImportError(
                "google-cloud-storage not found. "
                "You can install it with pip install launchflow[gcp]"
            )
        connection_info = self.connect()
        client = secretmanager.SecretManagerServiceClient()
        client.add_secret_version(
            parent=connection_info.secret_name,
            payload=secretmanager.SecretPayload(data=payload),
        )
