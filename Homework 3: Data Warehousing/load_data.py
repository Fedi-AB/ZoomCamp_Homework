import os
from concurrent.futures import ThreadPoolExecutor
from google.cloud import storage
from google.api_core.exceptions import GoogleAPIError
import time

# ==========================================================
# Configuration Section
# ==========================================================
# BUCKET_NAME:
# Name of the existing Google Cloud Storage bucket
# where parquet files will be uploaded.
BUCKET_NAME = "de_bucket_dtc"

# CREDENTIALS_FILE:
# Path to the service account JSON key file used
# for authenticating with Google Cloud.
# The file must exist locally.
CREDENTIALS_FILE = "secret/gcp_key.json"

# LOCAL_DIRECTORY:
# Local folder containing the parquet files to upload.
LOCAL_DIRECTORY = "Document"

# CHUNK_SIZE:
# Defines upload chunk size (8MB here).
# Chunking improves reliability and performance
# for large file uploads.
CHUNK_SIZE = 8 * 1024 * 1024  # 8MB

# MAX_RETRIES:
# Number of retry attempts if upload fails.
MAX_RETRIES = 3


# ==========================================================
# Initialize Google Cloud Storage Client
# ==========================================================
# Create a GCS client using explicit service account credentials.
# This method is useful when running locally or in non-GCP environments.
client = storage.Client.from_service_account_json(CREDENTIALS_FILE)

# Get a reference to the target bucket.
bucket = client.bucket(BUCKET_NAME)


# ==========================================================
# Upload Verification Function
# ==========================================================
def verify_gcs_upload(blob_name):
    """
    Checks whether a file (blob) exists in the bucket
    after upload to ensure data integrity.

    Args:
        blob_name (str): Name of the file inside the bucket.

    Returns:
        bool: True if file exists in GCS, False otherwise.
    """
    blob = bucket.blob(blob_name)
    return blob.exists(client)


# ==========================================================
# Upload Function
# ==========================================================
def upload_to_gcs(file_path):
    """
    Uploads a single parquet file to Google Cloud Storage.

    Features:
    - Uses chunked upload for better reliability
    - Implements retry logic
    - Verifies upload after completion

    Args:
        file_path (str): Full path to local parquet file
    """

    # Extract only the filename (without local directory path)
    blob_name = os.path.basename(file_path)

    # Create a blob object in the bucket
    blob = bucket.blob(blob_name)

    # Set chunk size for large file upload optimization
    blob.chunk_size = CHUNK_SIZE

    # Retry mechanism
    for attempt in range(MAX_RETRIES):
        try:
            print(f"Uploading {file_path} (Attempt {attempt + 1})...")

            # Upload file from local filesystem
            blob.upload_from_filename(file_path)

            print(f"Uploaded: gs://{BUCKET_NAME}/{blob_name}")

            # Verify upload integrity
            if verify_gcs_upload(blob_name):
                print(f"Verification successful: {blob_name}")
                return
            else:
                print(f"Verification failed, retrying...")

        except GoogleAPIError as e:
            print(f"Upload error: {e}")

        # Wait before retrying
        time.sleep(3)

    print(f"Failed after {MAX_RETRIES} attempts: {file_path}")


# ==========================================================
# Main Execution Block
# ==========================================================
if __name__ == "__main__":

    # Ensure local directory exists
    if not os.path.exists(LOCAL_DIRECTORY):
        raise Exception(f"Directory '{LOCAL_DIRECTORY}' not found.")

    # Collect all parquet files from the local directory
    parquet_files = [
        os.path.join(LOCAL_DIRECTORY, f)
        for f in os.listdir(LOCAL_DIRECTORY)
        if f.endswith(".parquet")
    ]

    if not parquet_files:
        print("No parquet files found.")
    else:
        print(f"Found {len(parquet_files)} parquet files.")

        # Use multithreading to upload multiple files in parallel
        # This improves throughput for batch uploads.
        with ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(upload_to_gcs, parquet_files)

    print("All files processed.")
