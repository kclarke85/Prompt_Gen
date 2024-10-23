import os
from dotenv import load_dotenv
import dropbox

# Load environment variables
load_dotenv()

# Get Dropbox access token from environment variable
DROPBOX_ACCESS_TOKEN = os.getenv('DROPBOX_TOKEN')

# Check if token exists
if DROPBOX_ACCESS_TOKEN is None:
    raise ValueError("Dropbox access token not found in environment variables!")

# Initialize Dropbox client
try:
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    print("Successfully connected to Dropbox!")
except Exception as e:
    print(f"Error connecting to Dropbox: {e}")

# Example upload function
def upload_to_dropbox(local_file_path, dropbox_file_path):
    try:
        with open(local_file_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_file_path)
        print(f"Successfully uploaded {local_file_path} to Dropbox!")
    except Exception as e:
        print(f"Error uploading to Dropbox: {e}")
