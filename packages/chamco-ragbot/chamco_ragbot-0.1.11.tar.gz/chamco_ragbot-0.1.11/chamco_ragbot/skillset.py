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
import os
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")
# BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
# BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")


AZURE_SEARCH_SERVICE_ENDPOINT = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
AZURE_SEARCH_ADMIN_KEY = os.getenv("AZURE_SEARCH_ADMIN_KEY")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
# # AZURE_OPENAI_MODEL_DEPLOYMENT = os.getenv("AZURE_OPENAI_MODEL_DEPLOYMENT")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")


credential = AzureKeyCredential(AZURE_SEARCH_ADMIN_KEY) if len(AZURE_SEARCH_ADMIN_KEY) > 0 else DefaultAzureCredential()


def create_skill_set(index_name):
    # Create a skillset
    skillset_name = f"{index_name}-skillset"

    split_skill = SplitSkill(
        description="Split skill to chunk documents",
        text_split_mode="pages",
        context="/document",
        maximum_page_length=2000,
        page_overlap_length=500,
        inputs=[
            InputFieldMappingEntry(name="text", source="/document/content"),
        ],
        outputs=[
            OutputFieldMappingEntry(name="textItems", target_name="pages")
        ],
    )

    embedding_skill = AzureOpenAIEmbeddingSkill(
        description="Skill to generate embeddings via Azure OpenAI",
        context="/document/pages/*",
        resource_uri=AZURE_OPENAI_ENDPOINT,
        deployment_id=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        api_key=AZURE_OPENAI_KEY,
        inputs=[
            InputFieldMappingEntry(name="text", source="/document/pages/*"),
        ],
        outputs=[
            OutputFieldMappingEntry(name="embedding", target_name="vector")
        ],
    )

    index_projections = SearchIndexerIndexProjections(
        selectors=[
            SearchIndexerIndexProjectionSelector(
                target_index_name=index_name,
                parent_key_field_name="parent_id",
                source_context="/document/pages/*",
                mappings=[
                    InputFieldMappingEntry(name="chunk", source="/document/pages/*"),
                    InputFieldMappingEntry(name="vector", source="/document/pages/*/vector"),
                    InputFieldMappingEntry(name="title", source="/document/metadata_storage_name"),
                ],
            ),
        ],
        parameters=SearchIndexerIndexProjectionsParameters(
            projection_mode=IndexProjectionMode.SKIP_INDEXING_PARENT_DOCUMENTS
        ),
    )

    skillset = SearchIndexerSkillset(
        name=skillset_name,
        description="Skillset to chunk documents and generating embeddings",
        skills=[split_skill, embedding_skill],
        index_projections=index_projections,
    )

    client = SearchIndexerClient(AZURE_SEARCH_SERVICE_ENDPOINT, credential)
    client.create_or_update_skillset(skillset)

    logging.info(f"[Ok] {skillset.name} skillset update completed")

    print(f"{skillset.name} created")
    return skillset

