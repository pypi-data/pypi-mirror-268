
import os
from typing import Dict
from azure.storage.blob import BlobServiceClient
from urllib.parse import urlparse, unquote_plus
from office365.sharepoint.client_context import ClientContext
from requests_ntlm import HttpNtlmAuth
import requests, tempfile

from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

from azure.storage.blob import BlobClient
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


SHAREPOINT_SITE_URL = os.getenv("SHAREPOINT_SITE_URL")
SHAREPOINT_USERNAME = os.getenv("SHAREPOINT_USERNAME")
SHAREPOINT_PASSWORD = os.getenv("SHAREPOINT_PASSWORD")
BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")


def sharepoint_auth(SHAREPOINT_SITE_URL, SHAREPOINT_USERNAME, SHAREPOINT_PASSWORD):
    ctx = ClientContext(SHAREPOINT_SITE_URL).with_credentials(UserCredential(f"{SHAREPOINT_USERNAME}", f"{SHAREPOINT_PASSWORD}"))
    return ctx



def download_sharepoint_file(ctx, file_url):
        
    download_path = os.path.join(tempfile.mkdtemp(), os.path.basename(file_url))
    with open(download_path, "wb") as local_file:
        file = (
            ctx.web.get_file_by_server_relative_path(file_url)
            .download(local_file)
            .execute_query()
        )
        logging.info("[Ok] file has been downloaded into: {0}".format(download_path))
        # print("[Ok] file has been downloaded into: {0}".format(download_path))
    return download_path



def upload_file_to_blob_container(download_path, blob_name, BLOB_CONNECTION_STRING, BLOB_CONTAINER_NAME):

    blob = BlobClient.from_connection_string(conn_str=BLOB_CONNECTION_STRING, container_name=BLOB_CONTAINER_NAME, blob_name=blob_name)

    with open(download_path, "rb") as data:
        blob.upload_blob(data, overwrite=True)

        logging.info("[Ok] file has been uploaded to: {0}".format(blob_name))
        # print("[Ok] file has been uploaded to: {0}".format(blob_name))
    return blob_name

