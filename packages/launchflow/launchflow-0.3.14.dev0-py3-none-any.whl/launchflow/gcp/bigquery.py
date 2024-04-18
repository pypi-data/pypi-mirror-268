try:
    from google.cloud import bigquery
except ImportError:
    bigquery = None

from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional

from launchflow.resource import Resource
from pydantic import BaseModel


class BigQueryDatasetConnectionInfo(BaseModel):
    gcp_project_id: str
    dataset_name: str


class BigQueryDataset(Resource[BigQueryDatasetConnectionInfo]):
    """A BigQuery Dataset resource.

    **Attributes**:
    - `name`: The name of the dataset. This must be globally unique.
    - `location`: The location of the dataset. Defaults to "US".

    Example usage:
    ```python
    from google.cloud import bigquery
    import launchflow as lf

    dataset = lf.gcp.BigQueryDataset("my-dataset")

    schema = [
        bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]
    table = dataset.create_table("table_name", schema=schema)

    dataset.insert_table_data("table_name", [{"name": "Alice", "age": 30}])

    # You can also use the underlying resource directly
    # For example, for a table with columns name,age
    query = f'''
    SELECT name, age
    FROM `{dataset.dataset_id}.table_name`
    WHERE age > 10
    ORDER BY age DESC
    '''

    for row in dataset.client().query(query):
        print(row)
    """

    def __init__(self, name: str, *, location="US") -> None:
        super().__init__(
            name=name,
            product_name="gcp_bigquery_dataset",
            create_args={"location": location},
        )
        # public metadata
        self.location = location

    def _validate_installation(self) -> None:
        """Validate that the google-cloud-bigquery library is installed.

        **Raises** `ImportError` if the library is not installed.
        """
        if bigquery is None:
            raise ImportError(
                "google-cloud-bigquery library is not installed. Please install it with `pip install launchflow[gcp]`."
            )

    @property
    def dataset_id(self) -> str:
        """Get the dataset id.

        **Returns**:
        - The dataset id.
        """
        return self.dataset().dataset_id


    def get_table_uuid(self, table_name: str) -> str:
        """Get the table UUID, {project_id}.{dataset_id}.{table_id}.

        **Arguments**:
        - `table_name`: The name of the table.

        **Returns**:
        - The table UUID.
        """
        connection_info = self.connect()
        return f"{connection_info.gcp_project_id}.{connection_info.dataset_name}.{table_name}"

    @lru_cache
    def client(self) -> bigquery.Client:
        """Get the BigQuery Client object.

        **Returns**:
        - The [BigQuery Client](https://cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client) object.
        """
        self._validate_installation()

        connection_info = self.connect()
        return bigquery.Client(project=connection_info.gcp_project_id)

    @lru_cache
    def dataset(self) -> bigquery.Dataset:
        """Get the BigQuery Dataset object.

        **Returns**:
        - The [BigQuery Dataset](https://cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset) object.
        """
        self._validate_installation()

        connection_info = self.connect()
        return bigquery.Dataset(f"{connection_info.gcp_project_id}.{connection_info.dataset_name}")

    # TODO: Explore generating schema from a dataclass
    def create_table(self, table_name: str, *, schema: Optional[List[bigquery.SchemaField]] = None) -> bigquery.Table:
        """Create a table in the dataset.

        **Arguments**:
        - `schema`: The schema of the table. Not required and defaults to None.

        **Returns**:
        - The [BigQuery Table](https://cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table) object.
        """
        self._validate_installation()

        # Create the table. It's OK to pass along None as the schema.
        table = bigquery.Table(self.get_table_uuid(table_name), schema)
        table = self.client().create_table(table)

        return table

    def delete_table(self, table_name: str) -> None:
        """Delete a table from the dataset.

        **Arguments**:
        - `table_name`: The name of the table to delete.
        """
        self._validate_installation()

        table = bigquery.Table(self.get_table_uuid(table_name))
        self.client().delete_table(table)

    # TODO: Support more file formats
    def load_table_data_from_csv(self, table_name: str, file_path: Path) -> None:
        """Load data from a CSV file into a table.

        **Arguments**:
        - `table_name`: The name of the table to load the data into.
        - `file_path`: The path to the CSV file to load.
        """
        self._validate_installation()

        table = self.client().get_table(self.get_table_uuid(table_name))

        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, schema=table.schema
        )
        with open(file_path, "rb") as f:
            job = self.client().load_table_from_file(f, table, job_config=job_config)

        # Wait for the data loading to complete.
        job.result()

    def insert_table_data(self, table_name: str, rows_to_insert: List[Dict[Any, Any]]) -> None:
        """Insert in-memory data into a table.
        There's seems to be a bug in bigquery where if a table name is re-used (created and then deleted
        recently), streaming to it won't work. If you encounter an unexpected 404 error, try changing
        the table name.

        **Arguments**:
        - `table_name`: The name of the table to insert the data into.
        - `rows_to_insert`: The data to insert into the table.

        **Raises**: ValueError if there were errors when inserting the data.
        """
        self._validate_installation()
        self.client().insert_rows_json(self.get_table_uuid(table_name), rows_to_insert)
