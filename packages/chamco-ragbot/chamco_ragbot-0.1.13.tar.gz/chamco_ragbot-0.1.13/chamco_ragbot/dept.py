import logging
from chamco_ragbot.indexer import create_indexer, indexer_client

# from .filetransfer import sharepoint_auth, download_sharepoint_file, upload_file_to_blob_container
from chamco_ragbot.datasource import create_datasource
# from .chat import chat, get_context, get_response
from chamco_ragbot.index import create_index
from chamco_ragbot.indexer import create_indexer, indexer_client
from chamco_ragbot.skillset import create_skill_set
from chamco_ragbot.utils import parse_file_url, sanitize_folder_name
from chamco_ragbot.acl import update_file_metadata



def process_departments(depts_dict, dept_name, file_url, BLOB_CONTAINER_NAME):
    folder_full, folder_name, file_name = parse_file_url(file_url)

    if depts_dict is not None:
        department_group_id = depts_dict.get(dept_name)
        if department_group_id is not None:
            update_file_metadata(file_name, dept_name, department_group_id, BLOB_CONTAINER_NAME)
            
            folder_name = sanitize_folder_name(folder_name)


            index = create_index(folder_name)

            data_source = create_datasource(folder_name, index_name=index.name)
            skillset = create_skill_set(index_name=index.name)
            indexer_result = create_indexer(index.name, data_source, skillset.name)

            logging.info(f"[Ok] {indexer_result.name} indexer update completed")

            logging.info(f"[Ok] running indexer {indexer_result.name}")
            indexer_client.run_indexer(indexer_result.name)

            logging.info("[Ok] RAG update completed")
        else:
            logging.error(f"Department group ID not found for {dept_name}.")
    else:
        logging.error("Error: Departments dictionary not populated.")
