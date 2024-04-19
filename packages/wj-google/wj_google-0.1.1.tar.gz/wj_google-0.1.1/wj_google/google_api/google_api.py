from typing import List, Optional
import os
import io
from .Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload


class GoogleApi:

    def __init__(
        self, client_secret_file: str, api_name: str, api_version, scopes: List[str]
    ) -> None:
        self.api_service = Create_Service(
            client_secret_file, api_name, api_version, scopes
        )

    def upload_files_to_drive(
        self, folder_id: str, file_paths: List[str], mime_types: List[str]
    ) -> None:
        for file_path, mime_type in zip(file_paths, mime_types):
            file_metadata = {"name": file_path.split("/")[-1], "parents": [folder_id]}

            media = MediaFileUpload(file_path, mime_type)

            self.api_service.files().create(
                body=file_metadata, media_body=media, fields="id"
            ).execute()

    def download_files_drive(
        self,
        file_ids: List[str],
        file_names: List[str],
        destination_path: Optional[str] = None,
    ) -> None:

        for file_id, file_name in zip(file_ids, file_names):
            request = self.api_service.files().get_media(fileId=file_id)

            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fd=fh, request=request)
            done = False

            while not done:
                status, done = downloader.next_chunk()
                print("Download progress {0}".format(status.progress() * 100))

            fh.seek(0)
            path = destination_path if destination_path else "./"
            with open(os.path.join(path, file_name), "wb") as f:
                f.write(fh.read())
                f.close()

    def create_directory_drive(self, directory_name: str):
        file_metadata = {
            "name": directory_name,
            "mimeType": "application/vnd.google-apps.folder",
        }

        self.api_service.files().create(body=file_metadata).execute()
