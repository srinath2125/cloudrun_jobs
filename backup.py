import os
import datetime
import shutil
import subprocess
from google.cloud import storage
from dotenv import load_dotenv  # Import dotenv to load .env file

# Load environment variables from the .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")  # Fix: Correct variable name
BACKUP_DIR = "/tmp/mongo_backup"
ZIP_PATH = "/tmp/mongo_backup.zip"

# Debugging prints to verify env variables
print(f"MONGO_URI: {MONGO_URI}")
print(f"GCS_BUCKET_NAME: {GCS_BUCKET_NAME}")

# Debug: Print the content of the .env file to confirm loading
with open(".env", "r") as env_file:
    print("Contents of .env file:")
    print(env_file.read())

def backup_mongo():
    """Perform a MongoDB backup and upload to GCS."""
    try:
        print("Starting MongoDB backup...")

        # Ensure clean backup directory
        if os.path.exists(BACKUP_DIR):
            shutil.rmtree(BACKUP_DIR)
        os.makedirs(BACKUP_DIR)

        # Generate backup filename
        today = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        backup_filename = f"mongo_backup_{today}.zip"

        # Run mongodump
        dump_command = ["mongodump", f"--uri={MONGO_URI}", "--out", BACKUP_DIR]
        subprocess.run(dump_command, check=True)

        # Compress backup folder
        shutil.make_archive("/tmp/mongo_backup", 'zip', BACKUP_DIR)

        # Upload to Google Cloud Storage
        gcs_client = storage.Client()
        bucket = gcs_client.bucket(GCS_BUCKET_NAME)
        blob = bucket.blob(backup_filename)
        blob.upload_from_filename(ZIP_PATH)

        print(f"Backup uploaded: {backup_filename}")

        # Cleanup local files
        shutil.rmtree(BACKUP_DIR)
        os.remove(ZIP_PATH)

        print("MongoDB backup completed successfully!")

        # Exit the service after backup
        exit(0)

    except Exception as e:
        print(f"Backup failed: {e}")
        exit(1)

if __name__ == "__main__":
    backup_mongo()
