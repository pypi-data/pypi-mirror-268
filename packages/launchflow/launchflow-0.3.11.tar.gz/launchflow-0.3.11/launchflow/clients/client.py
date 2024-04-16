import httpx
from launchflow.clients.accounts_client import AccountsAsyncClient
from launchflow.clients.connect_client import CloudConectAsyncClient
from launchflow.clients.environments_client import EnvironmentsAsyncClient
from launchflow.clients.operations_client import OperationsAsyncClient
from launchflow.clients.projects_client import ProjectsAsyncClient
from launchflow.clients.resources_client import ResourcesAsyncClient
from launchflow.clients.services_client import ServicesAsyncClient


class LaunchFlowAsyncClient:
    def __init__(self) -> None:
        self.http_client = httpx.AsyncClient(timeout=60)

        self.accounts = AccountsAsyncClient(self.http_client)
        self.environments = EnvironmentsAsyncClient(self.http_client)
        self.projects = ProjectsAsyncClient(self.http_client)
        self.connect = CloudConectAsyncClient(self.http_client)
        self.resources = ResourcesAsyncClient(self.http_client)
        self.operations = OperationsAsyncClient(self.http_client)
        self.services = ServicesAsyncClient(self.http_client)

    async def close(self):
        await self.http_client.aclose()
