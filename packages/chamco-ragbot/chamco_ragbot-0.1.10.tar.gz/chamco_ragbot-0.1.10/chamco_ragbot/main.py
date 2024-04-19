import os
import asyncio

from dotenv import load_dotenv
load_dotenv()

import sys
sys.path.append('/home/azureuser/projects/rag_chatbot/src/chamco_ragbot')


import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


from chamco_ragbot.filetransfer import sharepoint_auth, download_sharepoint_file, upload_file_to_blob_container
from chamco_ragbot.utils import parse_file_url
from chamco_ragbot.acl import get_departments_group_ids
from chamco_ragbot.dept import process_departments

SHAREPOINT_SITE_URL = os.getenv("SHAREPOINT_SITE_URL")
SHAREPOINT_USERNAME = os.getenv("SHAREPOINT_USERNAME")
SHAREPOINT_PASSWORD = os.getenv("SHAREPOINT_PASSWORD")

BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")



import asyncio

async def update_rag(file_url):
    folder_full, folder_name, file_name = parse_file_url(file_url)
    dept_name = folder_name
    blob_name = os.path.join(folder_name, file_name)
    ctx = sharepoint_auth(SHAREPOINT_SITE_URL, SHAREPOINT_USERNAME, SHAREPOINT_PASSWORD)
    download_path = download_sharepoint_file(ctx, file_url)
    blob_name = upload_file_to_blob_container(download_path, blob_name, BLOB_CONNECTION_STRING, BLOB_CONTAINER_NAME)

    # Initialize depts_dict outside the conditional blocks
    depts_dict = None

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        logging.info("Async event loop already running. Adding coroutine to the event loop.'")
        # print('Async event loop already running. Adding coroutine to the event loop.')
        tsk = loop.create_task(get_departments_group_ids())
        await tsk
        depts_dict = tsk.result()
        logging.info(f'Task done with depts_dict={depts_dict}')
            # Move subsequent code here
        process_departments(depts_dict, dept_name, file_url, BLOB_CONTAINER_NAME)

    else:
        logging.info(f'Starting new event loop')
        # print('Starting new event loop')
        depts_dict =  await get_departments_group_ids()  # Await the task completion
        # print(f'Task done with depts_dict={depts_dict}')
        logging.info(f'Task done with depts_dict={depts_dict}')
        # Move subsequent code here
        process_departments(depts_dict, dept_name, file_url, BLOB_CONTAINER_NAME)

    

# file_url = "/Shared Documents/GPTKB_HRTest/sample.txt"
# asyncio.run(update_rag(file_url))
# asyncio.gather(update_rag(file_url))

