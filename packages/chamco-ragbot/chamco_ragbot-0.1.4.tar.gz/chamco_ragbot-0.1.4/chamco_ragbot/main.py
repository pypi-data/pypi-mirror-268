import os
import asyncio

from dotenv import load_dotenv
load_dotenv()

# import sys
# sys.path.append('./chamco_ragbot')

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
import logging

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
        print('Async event loop already running. Adding coroutine to the event loop.')
        tsk = loop.create_task(get_departments_group_ids())

        def callback(t):
            nonlocal depts_dict
            depts_dict = t.result()
            print(f'Task done with depts_dict={depts_dict}')
            
            # Move subsequent code here
            process_departments(depts_dict, dept_name, file_url, BLOB_CONTAINER_NAME)

        tsk.add_done_callback(callback)
    else:
        print('Starting new event loop')
        depts_dict =  get_departments_group_ids()  # Await the task completion
        print(f'Task done with depts_dict={depts_dict}')
        
        # Move subsequent code here
        process_departments(depts_dict, dept_name, file_url, BLOB_CONTAINER_NAME)

    

# file_url = "/Shared Documents/GPTKB_HRTest/sample.txt"
# asyncio.run(update_rag(file_url))














# def update_rag(file_url):

#     folder_full, folder_name, file_name = parse_file_url(file_url)

#     dept_name = folder_name
#     ctx = sharepoint_auth(SHAREPOINT_SITE_URL, SHAREPOINT_USERNAME, SHAREPOINT_PASSWORD)
#     download_path = download_sharepoint_file(ctx, file_url)
#     blob_name = upload_file_to_blob_container(download_path, file_url, BLOB_CONNECTION_STRING, BLOB_CONTAINER_NAME)

#     try:
#         loop = asyncio.get_running_loop()
#     except RuntimeError:  # 'RuntimeError: There is no current event loop...'
#         loop = None
    
#     if loop and loop.is_running():
#         print('Async event loop already running. Adding coroutine to the event loop.')
#         tsk = loop.create_task(get_departments_group_ids())

#         def callback(t):
#             nonlocal depts_dict
#             depts_dict = t.result()
#             print(f'Task done with depts_dict={depts_dict}')

#         # Add the callback function to handle the result
#         tsk.add_done_callback(callback)
#     else:
#         print('Starting new event loop')
#         depts_dict = asyncio.run(get_departments_group_ids())
#     department_group_id = depts_dict[dept_name]

#     update_file_metadata(file_name, dept_name, department_group_id, BLOB_CONTAINER_NAME)

#     index = create_index(file_url)
#     data_source = create_datasource(folder_name, index_name=index.name)
#     skillset = create_skill_set(index_name=index.name)
#     indexer_result = create_indexer(index.name, data_source, skillset.name)
    
#     logging.info(f"[Ok] {indexer_result.name} indexer update completed")

#     logging.info(f"[Ok] running indexer {indexer_result.name}")
#     indexer_client.run_indexer(indexer_result.name)

#     logging.info(f"[Ok] RAG update completed")

#     # print(f"[Ok] {indexer_result.name} update completed")
#     # print(f"[Ok] RAG update completed")












# # async def update_rag_new(file_url):
# #     folder_full, folder_name, file_name = parse_file_url(file_url)
# #     dept_name = folder_name
# #     ctx = sharepoint_auth(SHAREPOINT_SITE_URL, SHAREPOINT_USERNAME, SHAREPOINT_PASSWORD)
# #     download_path = download_sharepoint_file(ctx, file_url)
# #     blob_name = upload_file_to_blob_container(download_path, file_url, BLOB_CONNECTION_STRING, BLOB_CONTAINER_NAME)

# #     # Initialize depts_dict outside the conditional blocks
# #     depts_dict = None
    
# #     try:
# #         loop = asyncio.get_running_loop()
# #     except RuntimeError:  # 'RuntimeError: There is no current event loop...'
# #         loop = None
    
# #     if loop and loop.is_running():
# #         print('Async event loop already running. Adding coroutine to the event loop.')
# #         tsk = loop.create_task(get_departments_group_ids())

# #         def callback(t):
# #             nonlocal depts_dict
# #             depts_dict = t.result()
# #             print(f'Task done with depts_dict={depts_dict}')
        
# #         # Add the callback function to handle the result
# #         tsk.add_done_callback(callback)
# #     else:
# #         print('Starting new event loop')
# #         depts_dict = await get_departments_group_ids()  # Await the task completion

# #     print("depts_dict: ", depts_dict)

# #     # Ensure depts_dict is available before accessing it
# #     if depts_dict is not None:
# #         department_group_id = depts_dict.get(dept_name)
# #         if department_group_id is not None:
# #             update_file_metadata(file_name, dept_name, department_group_id, BLOB_CONTAINER_NAME)

# #             index = create_index(file_url)
# #             data_source = create_datasource(folder_name, index_name=index.name)
# #             skillset = create_skill_set(index_name=index.name)
# #             indexer_result = create_indexer(index.name, data_source, skillset.name)
            
# #             logging.info(f"[Ok] {indexer_result.name} indexer update completed")

# #             logging.info(f"[Ok] running indexer {indexer_result.name}")
# #             indexer_client.run_indexer(indexer_result.name)

# #             logging.info(f"[Ok] RAG update completed")
# #             # Proceed with updating RAG status using department_group_id
            
# #         else:
# #             print(f"Department group ID not found for {dept_name}.")
# #     else:
# #         print("Error: Departments dictionary not populated.")
    

    
# #     # update_file_metadata(file_name, dept_name, department_group_id, BLOB_CONTAINER_NAME)

# #     # index = create_index(file_url)
# #     # data_source = create_datasource(folder_name, index_name=index.name)
# #     # skillset = create_skill_set(index_name=index.name)
# #     # indexer_result = create_indexer(index.name, data_source, skillset.name)
    
# #     # logging.info(f"[Ok] {indexer_result.name} indexer update completed")

# #     # logging.info(f"[Ok] running indexer {indexer_result.name}")
# #     # indexer_client.run_indexer(indexer_result.name)

# #     # logging.info(f"[Ok] RAG update completed")

# # # Call the function asynchronously
# # # asyncio.run(update_rag(file_url))






