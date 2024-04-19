from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    HnswParameters,
    VectorSearchAlgorithmMetric,
    ExhaustiveKnnAlgorithmConfiguration,
    ExhaustiveKnnParameters,
    VectorSearchProfile,
    AzureOpenAIVectorizer,
    AzureOpenAIParameters,
    SemanticConfiguration,
    SemanticSearch,
    SemanticPrioritizedFields,
    SemanticField,
    SearchIndex
)

from azure.search.documents.indexes.models import (
    SearchIndexer,
    FieldMapping
)
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
import os

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



# folder_url = 'Shared Documents/AITesting/'

# AZURE_SEARCH_SERVICE_ENDPOINT = "https://rag-aisearch-test.search.windows.net"
# AZURE_SEARCH_ADMIN_KEY = "MSIbbDLsRnn7vvp5Tmb03ITGjn7Kx5wx5MrwMIrrw3AzSeAw9fSk"
# # AZURE_SEARCH_INDEX = "new-index-amash"
# BLOB_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=chamcoragchatbotsa;AccountKey=9aXdSdzNS77p8Nk0NeLHG0gPMxt+VFsmfnKj7dZgWoO49NTN/KB2dvWCNPgj30H+oNGKr/OkOUBj+ASttmWcbw==;EndpointSuffix=core.windows.net"
# BLOB_CONTAINER_NAME = "ragchatbotcontainer"
# BLOB_FOLDER_NAME = folder_url
# AZURE_OPENAI_KEY = "5ddadda601e449109964b963f93a2d91"
# AZURE_OPENAI_EMBEDDING_DEPLOYMENT = "embeddingmodel"
# AZURE_OPENAI_MODEL_DEPLOYMENT = "opnaimodel"
# AZURE_OPENAI_ENDPOINT = "https://rag-example.openai.azure.com/"


# azure_openai_endpoint = AZURE_OPENAI_ENDPOINT
# azure_openai_embedding_deployment = AZURE_OPENAI_EMBEDDING_DEPLOYMENT
# azure_openai_model_deployment = AZURE_OPENAI_MODEL_DEPLOYMENT
# azure_openai_key = AZURE_OPENAI_KEY

# endpoint = AZURE_SEARCH_SERVICE_ENDPOINT

AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
AZURE_SEARCH_SERVICE_ENDPOINT = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
AZURE_SEARCH_ADMIN_KEY = os.getenv("AZURE_SEARCH_ADMIN_KEY")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_MODEL_DEPLOYMENT = os.getenv("AZURE_OPENAI_MODEL_DEPLOYMENT")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")



credential = AzureKeyCredential(AZURE_SEARCH_ADMIN_KEY) if len(AZURE_SEARCH_ADMIN_KEY) > 0 else DefaultAzureCredential()


# Create a search index
index_client = SearchIndexClient(endpoint=AZURE_SEARCH_SERVICE_ENDPOINT, credential=credential)
FIELDS = [
    SearchField(name="parent_id", type=SearchFieldDataType.String, sortable=True, filterable=True, facetable=True),
    SearchField(name="title", type=SearchFieldDataType.String),
    SearchField(name="chunk_id", type=SearchFieldDataType.String, key=True, sortable=True, filterable=True, facetable=True, analyzer_name="keyword"),
    SearchField(name="chunk", type=SearchFieldDataType.String, sortable=False, filterable=False, facetable=False),
    SearchField(name="vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single), vector_search_dimensions=1536, vector_search_profile_name="myHnswProfile"),
]



def create_index(index_name):

    # # Create a search index
    # index_client = SearchIndexClient(endpoint=endpoint, credential=credential)
    # fields = [
    #     SearchField(name="parent_id", type=SearchFieldDataType.String, sortable=True, filterable=True, facetable=True),
    #     SearchField(name="title", type=SearchFieldDataType.String),
    #     SearchField(name="chunk_id", type=SearchFieldDataType.String, key=True, sortable=True, filterable=True, facetable=True, analyzer_name="keyword"),
    #     SearchField(name="chunk", type=SearchFieldDataType.String, sortable=False, filterable=False, facetable=False),
    #     SearchField(name="vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single), vector_search_dimensions=1536, vector_search_profile_name="myHnswProfile"),
    # ]

    # index_name = file_url.split('/')[-2].lower()

    # Configure the vector search configuration
    vector_search = VectorSearch(
        algorithms=[
            HnswAlgorithmConfiguration(
                name="myHnsw",
                parameters=HnswParameters(
                    m=4,
                    ef_construction=400,
                    ef_search=500,
                    metric=VectorSearchAlgorithmMetric.COSINE,
                ),
            ),
            ExhaustiveKnnAlgorithmConfiguration(
                name="myExhaustiveKnn",
                parameters=ExhaustiveKnnParameters(
                    metric=VectorSearchAlgorithmMetric.COSINE,
                ),
            ),
        ],
        profiles=[
            VectorSearchProfile(
                name="myHnswProfile",
                algorithm_configuration_name="myHnsw",
                vectorizer="myOpenAI",
            ),
            VectorSearchProfile(
                name="myExhaustiveKnnProfile",
                algorithm_configuration_name="myExhaustiveKnn",
                vectorizer="myOpenAI",
            ),
        ],
        vectorizers=[
            AzureOpenAIVectorizer(
                name="myOpenAI",
                kind="azureOpenAI",
                azure_open_ai_parameters=AzureOpenAIParameters(
                    resource_uri=AZURE_OPENAI_ENDPOINT,
                    deployment_id=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
                    api_key=AZURE_OPENAI_KEY,
                ),
            ),
        ],
    )

    semantic_config = SemanticConfiguration(
        name="my-semantic-config",
        prioritized_fields=SemanticPrioritizedFields(
            content_fields=[SemanticField(field_name="chunk")]
        ),
    )

    # Create the semantic search with the configuration
    semantic_search = SemanticSearch(configurations=[semantic_config])

    # Create the search index
    index = SearchIndex(name=index_name, fields=FIELDS, vector_search=vector_search, semantic_search=semantic_search)
    logging.info(f"[Ok] {index_name} created")

    result = index_client.create_or_update_index(index)
    logging.info(f"[Ok] index client created or updated")

    return result


