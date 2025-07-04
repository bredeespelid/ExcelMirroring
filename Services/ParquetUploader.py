from azure.storage.blob import BlobServiceClient

def upload_to_blob(local_file_path, blob_name, config):
    blob_service_client = BlobServiceClient.from_connection_string(config['blob_connection_string'])
    container_client = blob_service_client.get_container_client(config['blob_container_name'])
    with open(local_file_path, "rb") as data:
        container_client.upload_blob(name=blob_name, data=data, overwrite=True)
