
from azure.search.documents.indexes.models import (
    SplitSkill,
    InputFieldMappingEntry,
    OutputFieldMappingEntry,
    AzureOpenAIEmbeddingSkill,
    SearchIndexerIndexProjections,
    SearchIndexerIndexProjectionSelector,
    SearchIndexerIndexProjectionsParameters,
    IndexProjectionMode,
    SearchIndexerSkillset
)
from azure.search.documents.indexes import SearchIndexerClient
from azure.search.documents.indexes.models import (
    SearchIndexerDataContainer,
    SearchIndexerDataSourceConnection
)
from azure.search.documents.indexes._generated.models import NativeBlobSoftDeleteDeletionDetectionPolicy

from azure.core.credentials import AzureKeyCredential
import os
from azure.identity import DefaultAzureCredential


from azure.search.documents.indexes.models import (
    SearchIndexer,
    FieldMapping
)

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")


AZURE_SEARCH_SERVICE_ENDPOINT = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
AZURE_SEARCH_ADMIN_KEY = os.getenv("AZURE_SEARCH_ADMIN_KEY")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_MODEL_DEPLOYMENT = os.getenv("AZURE_OPENAI_MODEL_DEPLOYMENT")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")


credential = AzureKeyCredential(AZURE_SEARCH_ADMIN_KEY) if len(AZURE_SEARCH_ADMIN_KEY) > 0 else DefaultAzureCredential()
indexer_client = SearchIndexerClient(AZURE_SEARCH_SERVICE_ENDPOINT, credential)





def create_indexer(index_name, data_source, skillset_name):

    # Create an indexer
    indexer_name = f"{index_name}-indexer"

    indexer = SearchIndexer(
        name=indexer_name,
        description="Indexer to index documents and generate embeddings",
        skillset_name=skillset_name,
        target_index_name=index_name,
        data_source_name=data_source.name,
        # Map the metadata_storage_name field to the title field in the index to display the PDF title in the search results
        field_mappings=[FieldMapping(source_field_name="metadata_storage_name", target_field_name="title")]
    )

    indexer_result = indexer_client.create_or_update_indexer(indexer)
    logging.info(f"[Ok] {indexer_result.name} indexer update completed")

    return indexer_result
