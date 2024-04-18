from sidradataquality.sdk.databricks.utils import Utils
from datetime import datetime, timedelta
from operator import attrgetter
import re
from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ResourceTypes, AccountSasPermissions, generate_account_sas, ContainerSasPermissions, generate_container_sas
import sidradataquality.sdk.constants as const

class StorageService():
    def __init__(self, spark):
        self.spark = spark
        self.databricks_utils = Utils(spark)

    def get_blob_data_lake_service_client(self):
        return self._get_blob_service('resources', const.SECRET_STORAGE_ACCOUNT_NAME, const.SECRET_STORAGE_ACCOUNT_KEY)
    
    def get_blob_service_client(self):
        return self._get_blob_service(const.SECRET_DATABRICKS_SCOPE, const.SECRET_STORAGE_ACCOUNT_NAME, const.SECRET_STORAGE_ACCOUNT_KEY)

    def get_or_create_container(self, blob_service_client, destination_container) -> str:
        if not [ container for container in blob_service_client.list_containers(destination_container) if container.name == destination_container ]:
            try:
                blob_service_client.create_container(destination_container.lower())
            except ResourceExistsError as e:
                # Ignore error if the container already exists because it could happen due a race condition and if the container already exists simply return the destination container
                if e.error_code != 'ContainerAlreadyExists':
                    raise e    
        return destination_container

    def upload_file_to_datalake(self, name, path, content, destination_container = const.STORAGE_DEFAULT_CONTAINER):
        blob_service = self.get_blob_data_lake_service_client()
        self._upload_file(blob_service, name, path, content, destination_container)

    def upload_file_to_data_quality_storage(self, name, path, content, destination_container = const.STORAGE_DEFAULT_CONTAINER):
        blob_service = self.get_blob_service_client()
        self._upload_file(blob_service, name, path, content, destination_container)

    def _upload_file(self, blob_service, name, path, content, destination_container):
        container = self.get_or_create_container(blob_service, destination_container)
        blob_client = blob_service.get_blob_client(container, f"{path}/{name}")
        blob_client.upload_blob(content, overwrite=True)

    def _get_blob_service(self, databricks_scope, storage_account_name_secret, storage_account_key_secret):
        storage_account_name = self.databricks_utils.get_databricks_secret(databricks_scope, storage_account_name_secret)
        storage_account_key = self.databricks_utils.get_databricks_secret(databricks_scope, storage_account_key_secret)
        service = BlobServiceClient(account_url='https://{addsto}.blob.core.windows.net/'.format(addsto = storage_account_name), credential=storage_account_key)
        return service
