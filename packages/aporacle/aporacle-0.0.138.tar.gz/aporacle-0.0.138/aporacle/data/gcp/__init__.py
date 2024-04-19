# [START storage_list_files]
import pickle

import pandas as pd
from google.cloud import storage
from google.oauth2.service_account import Credentials
from io import StringIO
from io import BytesIO


# 0. List all buckets.
def list_buckets():
    """Lists all buckets in your GCP project."""
    try:
        storage_client = storage.Client()
        buckets = list(storage_client.list_buckets())
        return [bucket.name for bucket in buckets]

    except Exception as err:
        print(f"Error listing buckets: {err}")


# 1. Create bucket if not exist. Map bucket to feed.
def create_bucket(bucket_name, location=None):
    """Creates a bucket in Google Cloud Storage.

    Args:
      bucket_name: The name of the bucket to create.
      location: The location to store the bucket data (optional). Defaults to None (US multi-region).

    Returns:
      The newly created bucket object, or None on error.
    """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        bucket.create(location=location)
        print(f"Bucket '{bucket_name}' created successfully.")
        return bucket
    except Exception as err:
        print(f"Error creating bucket: {err}")
        return None


def list_bucket_files(bucket_name: str):
    """Lists all files (blobs) within a bucket in Google Cloud Storage.

  Args:
      bucket_name: The name of the bucket to list files from.
  """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blobs = bucket.list_blobs()
        return [blob.name for blob in blobs]

    except Exception as err:
        print(f"Error listing bucket files: {err}")


# 2. List files by feed/bucket.
def list_files_by_feed(feed: str):
    return list_bucket_files(bucket_name=feed)


# 3. Upload file to bucket by feed.
def upload_file_to_bucket(bucket_name: str, source_file_path: str, destination_blob_name: str):
    """Uploads a file to GCP storage.

      Args:
        bucket_name: The name of the bucket to upload the file to.
        source_file_path: The local path of the file to upload.
        destination_blob_name: The name of the file in the bucket (optional).
      """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        if destination_blob_name:
            blob = bucket.blob(destination_blob_name)
        else:
            blob = bucket.blob(source_file_path.split('/')[-1])  # Use filename by default
        blob.upload_from_filename(source_file_path)
        print(f"File uploaded to {bucket_name}/{blob.name}")
    except Exception as err:
        print(f"Error uploading file: {err}")


# 4. Download file from bucket by file_name name.
def download_file_from_bucket(bucket_name: str, object_name: str, local_path: str):
    """Downloads a file from GCP storage and returns the local path.

      Args:
          bucket_name: The name of the bucket containing the file.
          object_name: The name of the file to download.
          local_path: The local path to save the downloaded file.

      Returns:
          The local path of the downloaded file, or None on error.
      """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(object_name)
        blob.download_to_filename(local_path)
        return local_path
    except Exception as err:
        print(f"Error downloading file: {err}")
        return None


# 5. Delete file from bucket by file_name name.
def delete_file_from_bucket(bucket_name: str, object_name: str):
    """Deletes a file (blob) from a bucket in Google Cloud Storage.

      Args:
          bucket_name: The name of the bucket containing the file.
          object_name: The name of the file (blob) to delete.

      Returns:
          True on successful deletion, False otherwise.
      """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(object_name)
        blob.delete()
        print(f"File '{object_name}' deleted from bucket '{bucket_name}'.")
        return True
    except Exception as err:
        print(f"Error deleting file: {err}")
        return False


# 6. Delete bucket by feed or bucket name.
def delete_bucket(bucket_name):
    """Deletes a bucket in Google Cloud Storage.

    Args:
      bucket_name: The name of the bucket to delete.

    Returns:
      True on successful deletion, False otherwise.
    """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        bucket.delete()
        print(f"Bucket '{bucket_name}' deleted successfully.")
        return True
    except Exception as err:
        print(f"Error deleting bucket: {err}")
        return False


# 7. Upload dataframe to GCP
def upload_df_to_gcp(bucket_name: str, symbol: str, df: pd.DataFrame):
    destination_blob_name = f"{symbol}.csv".lower()

    # Convert DataFrame to a CSV string in memory
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)  # Set index=False to exclude the index column

    # Upload the CSV string to GCP bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(csv_buffer.getvalue())


# 8. Download CSV from GCP and return as DataFrame
def download_csv_from_gcp_return_df(bucket_name: str, file_name: str):
    file_path = f"{file_name}.csv".lower()

    # Download the CSV file from GCP bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_path)

    # Download data as a byte stream
    csv_data = blob.download_as_string()

    # Convert byte stream to in-memory file-like object
    csv_buffer = BytesIO(csv_data)

    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(csv_buffer)

    # Return the DataFrame
    return df


# 9. Upload a pickled data to GCP bucket
def upload_pickle_to_gcs(bucket_name, object_name, pickle_data):
    """Uploads pickle data from memory to a file in GCP storage.

  Args:
      bucket_name: The name of the bucket to upload the file to.
      object_name: The name of the file in the bucket.
      pickle_data: The pickled data object in memory.
  """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(object_name)

        # Use a StringIO object to write pickle data in memory
        with BytesIO() as buffer:
            pickle.dump(pickle_data, buffer)
            buffer.seek(0)  # Move pointer to beginning for upload
            blob.upload_from_string(buffer.getvalue(), content_type='application/octet-stream')

        print(f"Pickle data uploaded to {bucket_name}/{object_name}")
    except Exception as err:
        print(f"Error uploading pickle data: {err}")


# 10. Download a pickled data from GCP bucket and convert to sklearn Ridge model
def download_and_load_pickle(bucket_name: str, object_name: str):
    """Downloads a pickle file from GCP storage and loads the data.

  Args:
      bucket_name: The name of the bucket containing the file.
      object_name: The name of the pickle file to download.

  Returns:
      The loaded data from the pickle file, or None on error.
  """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(object_name)
        pickle_data = blob.download_as_string()

        # Load data from pickle
        data = pickle.loads(pickle_data)
        return data
    except Exception as err:
        print(f"Error downloading/loading pickle data: {err}")
        return None


# 11. Upload a dataframe to GCP BigQuery
def upload_df_to_bigquery_gbq(project_id, dataset_id, table_name, dataframe, credentials_path=None):
    """Uploads a pandas DataFrame to a BigQuery table using pandas-gbq.

  Args:
      project_id: Your GCP project ID.
      dataset_id: The ID of the BigQuery dataset to upload to.
      table_name: The name of the BigQuery table to create or update.
      dataframe: The pandas DataFrame to upload.
      credentials_path: Path to a service account credentials file (optional).
  """
    if credentials_path:
        credentials = Credentials.from_service_account_file(credentials_path)
    else:
        credentials = None  # Use application default credentials

    try:
        dataframe.to_gbq(destination_table=f"{project_id}.{dataset_id}.{table_name}",
                         if_exists='replace',  # Options: 'replace', 'append'
                         credentials=credentials)
        print(f"Data uploaded to {project_id}.{dataset_id}.{table_name}")
    except Exception as err:
        print(f"Error uploading data: {err}")


# 12. Download from BigQuery to dataframe
def download_bigquery_data_to_dataframe(project_id, dataset_id, table_name, query=None, credentials_path=None):
    """Downloads data from BigQuery to a pandas DataFrame using pandas-gbq.

  Args:
      project_id: Your GCP project ID.
      dataset_id: The ID of the BigQuery dataset to query.
      table_name: The name of the BigQuery table to query (optional if using a query).
      query: A SQL query to retrieve data (optional, replaces table download).
      credentials_path: Path to a service account credentials file (optional).

  Returns:
      A pandas DataFrame containing the downloaded data, or None on error.
  """
    if credentials_path:
        credentials = Credentials.from_service_account_file(credentials_path)
    else:
        credentials = None  # Use application default credentials

    try:
        if query:
            # Download using query
            dataframe = pd.read_gbq(query, project_id=project_id, credentials=credentials)
        else:
            # Download entire table
            dataframe = pd.read_gbq(f"{project_id}.{dataset_id}.{table_name}", credentials=credentials)
        return dataframe
    except Exception as err:
        print(f"Error downloading data: {err}")
        return None
