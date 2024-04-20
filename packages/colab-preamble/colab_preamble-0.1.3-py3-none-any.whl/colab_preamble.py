# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from google.colab import auth, drive

def run(google_cloud_project: str=None, mount_drive: bool=True):
    if mount_drive:
        print("Mounting google drive...", file=sys.stderr)
        drive.mount('/content/drive')        

    if google_cloud_project is not None:
        print(f"Setting default google cloud project as {google_cloud_project}...", file=sys.stderr)
        subprocess.run(["gcloud", "config", "set", "project", google_cloud_project])
        os.environ["GOOGLE_CLOUD_PROJECT"] = google_cloud_project
        print(f"Authenticating user...", file=sys.stderr)
        auth.authenticate_user()

        print("To use bigquery magic, try:\n\n%load_ext bq\n%bq SELECT 1")
