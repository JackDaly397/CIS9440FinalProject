import pandas as pd
from io import StringIO
from azure.storage.blob import BlobServiceClient

def extract_and_upload_data(data_source_urls, connection_string_azure_storage, container_azure):
    for idx, data_source_url in enumerate(data_source_urls, start=1):
        df_raw = pd.read_csv(data_source_url)
        output = StringIO()
        df_raw.to_csv(output, index=False)
        data = output.getvalue()
        output.close()

        # Blob name based on index
        blob_name = f"public_up_to_150k_{idx}_230930.csv"

        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(connection_string_azure_storage)

        # Get a blob client using the container name and blob name
        blob_client = blob_service_client.get_blob_client(container=container_azure, blob=blob_name)

        # Upload the CSV data
        blob_client.upload_blob(data, overwrite=True)
        print(f"Uploaded {blob_name} to Azure Blob Storage in container {container_azure}.")
