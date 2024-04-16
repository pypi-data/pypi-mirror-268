import logging
import requests
import json
import logging
import pandas as pd
import requests
import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import uuid

# Configure basic logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class pyDataverseOps:
    """Handles operations with Dataverse.

    This class is responsible for initializing connection parameters to Dataverse,
    including acquiring an access token for authentication and setting up headers for HTTP requests.
    """

    def __init__(self, domain, tenant_id, client_id, client_secret) -> None:
        """Initializes the DataverseOps object.

        Args:
            domain: The domain of the Dataverse server.
            tenant_id: Tenant ID for OAuth authentication.
            client_id: Client ID for OAuth authentication.
            client_secret: Client Secret for OAuth authentication.
        """
        self.domain = domain
        try:
            self.access_token = self.get_access_token(
                tenant_id, client_id, client_secret
            )
            self.headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json",
            }
            self.base_url = f"https://{self.domain}/api/data/v9.2/"
            logger.info("DataverseOps object initialized successfully.")
        except Exception as e:
            logger.error("Failed to initialize DataverseOps object: %s", e)
            raise e  # Reraising exception to ensure the caller is aware of the failure.

    def get_access_token(self, tenant_id, client_id, client_secret):
        """Retrieves access token for authentication with Dataverse.

        Args:
            tenant_id: Tenant ID for OAuth authentication.
            client_id: Client ID for OAuth authentication.
            client_secret: Client Secret for OAuth authentication.

        Returns:
            A string representing the access token.

        Raises:
            Exception: If the request for an access token fails.
        """
        token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        payload = {
            "client_id": client_id,
            "scope": f"https://{self.domain}/.default",
            "client_secret": client_secret,
            "grant_type": "client_credentials",
        }
        try:
            response = requests.post(token_url, data=payload)
            response.raise_for_status()  # This will raise an exception for HTTP error responses.
            logger.info("Access token retrieved successfully.")
            return response.json()["access_token"]
        except requests.RequestException as e:
            logger.error("Failed to retrieve access token: %s", e)
            raise Exception("Failed to retrieve access token") from e

    def build_filter_query(self, filters: dict) -> str:
        """Builds an OData filter query string from a dictionary of filters.

        Args:
            filters: A dictionary where keys are column names and values are the conditions. Conditions can be a single value (for equality) or a tuple (for other comparisons).

        Returns:
            A string representing the OData filter query.
        """
        filter_parts = []
        for column_name, value in filters.items():
            if isinstance(value, tuple):
                # Handle complex conditions using tuples like ('lt', 100)
                comparator, val = value
                filter_parts.append(f"{column_name} {comparator} {val}")
            else:
                # Default to 'eq' if just a single value is provided, assuming string values
                filter_parts.append(
                    f"{column_name} eq {value}"
                )  # Assuming string values need to be quoted
        return " and ".join(filter_parts)

    def read_data(
        self, table_logical_name: str, filters: dict = {}, pagination: bool = False
    ):
        """Fetches data from a specified Dataverse table with optional filtering and pagination.

        Args:
            table_logical_name: The logical name of the table in Dataverse.
            filters: A dictionary of filters to apply to the query.
            pagination: If True, paginates through all results.

        Returns:
            A pandas DataFrame containing the fetched data.

        Raises:
            Exception: If the request to Dataverse fails.
        """
        try:
            filter_query = self.build_filter_query(filters)
            url = f"{self.base_url}{table_logical_name}"
            if filters:
                url += f"?$filter={filter_query}"

            if pagination:
                dfs = []  # List to hold data frames from each page
                while url:
                    response = requests.get(url, headers=self.headers)
                    response.raise_for_status()  # Check for HTTP request errors
                    data = json.loads(response.content.decode("utf-8"))
                    dfs.append(pd.json_normalize(data["value"]))
                    url = data.get(
                        "@odata.nextLink"
                    )  # Update URL for the next page, if any
                result = pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
            else:
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()  # Check for HTTP request errors
                data = json.loads(response.content.decode("utf-8"))
                result = pd.json_normalize(data["value"])

            logger.info("Data read successfully from %s", table_logical_name)
            return result
        except requests.RequestException as e:
            logger.error("Failed to read data from %s: %s", table_logical_name, e)
            raise Exception(f"Failed to read data from {table_logical_name}") from e

    def write_single_record(self, table_logical_name: str, data: dict):
        """Posts a single record to the specified Dataverse table.

        Args:
            table_logical_name: The logical name of the table in Dataverse.
            row: A pandas Series object representing the record to post.

        Note:
            If the posting fails, an error message is logged with the record's ID (if available) or 'Unknown ID'.
        """
        url = f"{self.base_url}{table_logical_name}"
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(data))
            if response.status_code != 204:
                logger.error("Error processing record, Error: %s", response.text)
        except Exception as e:
            logger.error("Error processing record, Exception: %s", e)

    def write_data(self, table_logical_name: str, data_df: pd.DataFrame):
        """Writes a DataFrame of records to the specified Dataverse table using concurrent requests.

        Args:
            table_logical_name: The logical name of the table in Dataverse.
            data_df: A pandas DataFrame where each row represents a record to post.

        Returns:
            A string indicating the completion status.

        Note:
            This function utilizes a ThreadPoolExecutor to post records concurrently for improved efficiency.
        """
        try:
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = [
                    executor.submit(
                        self.write_single_record, table_logical_name, row.to_dict()
                    )
                    for _, row in data_df.iterrows()
                ]
                for future in as_completed(futures):
                    # Ensuring any exception raised during post_record execution is handled
                    future.result()
            logger.info("All data written successfully to %s", table_logical_name)
            return "Done"
        except Exception as e:
            logger.error("Failed to write data to %s: %s", table_logical_name, e)
            return "Failed"

    def write_data_batch(self, table_logical_name, data_df):
        """Writes a DataFrame of records to the specified Dataverse table in a single batch request.

        Args:
            table_logical_name: The logical name of the table in Dataverse.
            data_df: A pandas DataFrame where each row represents a record to be included in the batch request.

        Returns:
            The response object from the batch request.

        Raises:
            Exception: If an error occurs during the batch request.
        """
        try:
            batch_id = uuid.uuid4()
            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "OData-MaxVersion": "4.0",
                "OData-Version": "4.0",
                "Accept": "application/json",
                "Content-Type": f"multipart/mixed;boundary=batch_{batch_id}",
            }

            # Start building the batch request payload
            batch_body = ""
            for index, record in data_df.iterrows():
                changeset_id = uuid.uuid4()
                record_json = record.to_json(date_format="iso")
                batch_body += f"--batch_{batch_id}\n"
                batch_body += "Content-Type: application/http\n"
                batch_body += "Content-Transfer-Encoding: binary\n\n"
                batch_body += f"POST {self.base_url}{table_logical_name} HTTP/1.1\n"
                batch_body += "Content-Type: application/json\n\n"
                batch_body += f"{record_json}\n\n"

            batch_body += f"--batch_{batch_id}--"

            # Perform the batch request

            response = requests.post(
                f"{self.base_url}$batch",
                headers=headers,
                data=batch_body,
            )
            if response.status_code == 200:
                logger.info(f"Batch data write successful to {table_logical_name}")
            else:
                logger.error(
                    f"Batch data write error: Status Code: {response.status_code}"
                )

            return response
        except Exception as e:
            logger.exception(
                f"Exception occurred while writing batch data to {table_logical_name}: {e}"
            )
            raise  # Reraising the exception after logging

    def update_single_record(
        self, table_logical_name: str, unique_column: str, data: dict
    ):
        """Updates a record in the specified Dataverse table using PATCH request.

        Args:
            table_logical_name: The logical name of the table in Dataverse where the record exists.
            unique_column: The name of the column that uniquely identifies the record to be updated.
            data: A dictionary representing the record's data. The unique column's value should be included in this dictionary.

        Note:
            The method logs a message if the unique column's value is missing, or if the update operation fails.
        """
        # Construct the URL for the update operation
        record_id = data.get(unique_column)
        if not record_id:
            logger.warning("Record ID is missing from the data provided.")
            return

        update_url = f"{self.base_url}{table_logical_name}({record_id})"

        # Exclude the ID field from the data to be updated
        data.pop(unique_column, None)

        try:
            response = requests.patch(
                update_url, headers=self.headers, data=json.dumps(data)
            )
            if response.status_code != 204:
                logger.error(
                    "Failed to update record %s. Status code: %s, Response: %s",
                    record_id,
                    response.status_code,
                    response.text,
                )
        except Exception as e:
            logger.exception(
                "Exception occurred while updating record %s: %s", record_id, e
            )

    def update_records(
        self, table_logical_name: str, unique_column: str, data_df: pd.DataFrame
    ):
        """Updates multiple records in a specified Dataverse table concurrently.

        This method uses a thread pool to update records in parallel, improving efficiency for large datasets.

        Args:
            table_logical_name: The logical name of the table in Dataverse where the records exist.
            unique_column: The name of the column that uniquely identifies each record to be updated.
            data_df: A pandas DataFrame where each row represents the data for a record, including the unique column value.

        Note:
            The method logs the progress and handles exceptions raised by the `update_record` method calls.
        """
        # Use a ThreadPoolExecutor to update records in parallel
        with ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(
                    self.update_single_record,
                    table_logical_name,
                    unique_column,
                    row.to_dict(),
                ): index
                for index, row in data_df.iterrows()
            }
            for future in as_completed(futures):
                index = futures[future]
                try:
                    # Attempt to get the result of the future, which will raise exceptions if any occurred
                    future.result()
                    logger.info(f"Record at index {index} updated successfully.")
                except Exception as e:
                    # Log the exception details including the index of the row that caused it
                    logger.exception(
                        f"Exception occurred while updating record at index {index}: {e}"
                    )

    def update_records_batch(
        self, table_logical_name: str, unique_column: str, data_df: pd.DataFrame
    ):
        """Performs a batch update of records in a specified Dataverse table.

        This method constructs a batch request to update multiple records in a single HTTP request,
        which is more efficient for updating large numbers of records.

        Args:
            table_logical_name: The logical name of the table in Dataverse.
            unique_column: The name of the column that uniquely identifies each record.
            data_df: A pandas DataFrame where each row represents the data for a record, including the unique column value.

        Note:
            The method logs the result of the batch operation, indicating success or failure.
        """

        batch_url = f"{self.base_url}/$batch"
        batch_id = str(uuid.uuid4())
        changeset_id = str(uuid.uuid4())

        # Initialize the batch request payload
        batch_body = f"--batch_{batch_id}\r\n"
        batch_body += (
            f"Content-Type: multipart/mixed; boundary=changeset_{changeset_id}\r\n\r\n"
        )

        # Initialize Content-ID counter
        content_id = 1

        for index, row in data_df.iterrows():
            record_id = row[unique_column]  # Extract the record identifier
            data = row.to_dict()
            data.pop(
                unique_column, None
            )  # Remove the unique column from the data to be updated

            # Construct each request within the changeset, including Content-ID header
            batch_body += f"--changeset_{changeset_id}\r\n"
            batch_body += "Content-Type: application/http\r\n"
            batch_body += f"Content-ID: {content_id}\r\n"  # Add Content-ID header
            batch_body += "Content-Transfer-Encoding: binary\r\n\r\n"
            batch_body += f"PATCH {table_logical_name}({record_id}) HTTP/1.1\r\n"
            batch_body += "Content-Type: application/json\r\n\r\n"
            batch_body += json.dumps(data) + "\r\n\r\n"

            content_id += 1  # Increment Content-ID for the next request

        # Close the changeset and batch
        batch_body += f"--changeset_{changeset_id}--\r\n"
        batch_body += f"--batch_{batch_id}--\r\n"

        # Set headers for the batch request
        batch_headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": f"multipart/mixed; boundary=batch_{batch_id}",
        }
        try:
            # Send the batch request
            response = requests.post(
                batch_url, headers=batch_headers, data=batch_body.encode("utf-8")
            )

            if response.ok or response.status_code == 202:
                logger.info("Batch update successful.")
            else:
                logger.error(
                    f"Batch update failed: {response.status_code}, {response.text}"
                )
        except Exception as e:
            logger.exception(f"Exception occurred during batch update: {e}")
            raise

    def get_all_record_ids(self, table_logical_name, unique_column):
        """Fetches all record IDs from the specified Dataverse table.

        Args:
            table_logical_name: The logical name of the table from which to fetch records.
            unique_column: The unique column (usually an ID) to select in the query.

        Returns:
            A list of record IDs if the request is successful; otherwise, an empty list.
        """
        url = f"{self.base_url}{table_logical_name}?$select={unique_column}"

        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return [record[unique_column] for record in response.json()["value"]]
            else:
                logger.error(f"Failed to fetch records: {response.text}")
                return []
        except Exception as e:
            logger.exception(f"Exception occurred while fetching record IDs: {e}")
            return []

    def batch_delete_records(self, table_logical_name, unique_column):
        """Deletes all records from the specified Dataverse table in a batch operation.

        Args:
            table_logical_name: The logical name of the table from which to delete records.
            unique_column: The unique column (usually an ID) used to identify records to delete.
        """
        record_ids = self.get_all_record_ids(table_logical_name, unique_column)
        batch_id = str(uuid.uuid4())
        batch_headers = self.headers.copy()
        batch_headers["Content-Type"] = f"multipart/mixed; boundary=batch_{batch_id}"

        batch_body = ""
        for record_id in record_ids:
            batch_body += f"--batch_{batch_id}\r\n"
            batch_body += "Content-Type: application/http\r\n"
            batch_body += "Content-Transfer-Encoding: binary\r\n\r\n"
            batch_body += (
                f"DELETE {self.base_url}{table_logical_name}({record_id}) HTTP/1.1\r\n"
            )
            batch_body += "If-Match: *\r\n\r\n"

        batch_body += f"--batch_{batch_id}--\r\n"

        batch_url = f"{self.base_url}$batch"

        try:
            response = requests.post(
                batch_url, headers=batch_headers, data=batch_body.encode("utf-8")
            )
            if response.ok:
                logger.info("Batch deletion successful.")
            else:
                logger.error(
                    f"Batch deletion failed: {response.status_code}, {response.text}"
                )
        except Exception as e:
            logger.exception(f"Exception occurred during batch deletion: {e}")
