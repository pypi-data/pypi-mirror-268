



from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizableTextQuery

from azure.search.documents.models import (
    QueryType,
    QueryCaptionType,
    QueryAnswerType
)

import os
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential

AZURE_SEARCH_SERVICE_ENDPOINT = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
AZURE_SEARCH_ADMIN_KEY = os.getenv("AZURE_SEARCH_ADMIN_KEY")

credential = AzureKeyCredential(AZURE_SEARCH_ADMIN_KEY) if len(AZURE_SEARCH_ADMIN_KEY) > 0 else DefaultAzureCredential()


def vector_query(query, index_name):

    # Pure Vector Search
    # query = "Which is more comprehensive, Northwind Health Plus vs Northwind Standard?"
    # index_name = "azureblob-index"
    search_client = SearchClient(AZURE_SEARCH_SERVICE_ENDPOINT, index_name, credential=credential)
    vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=1, fields="content", exhaustive=True)
    # vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=1, fields="vector", exhaustive=True)
    # Use the below query to pass in the raw vector query instead of the query vectorization
    # vector_query = RawVectorQuery(vector=generate_embeddings(query), k_nearest_neighbors=3, fields="vector")

    results = search_client.search(
        search_text=None,
        vector_queries= [vector_query],
        # select=["parent_id", "chunk_id", "chunk"],
        top=1
    )

    print(results)
    return results


# for result in results:
#   print(result)
    # print(f"parent_id: {result['parent_id']}")
    # print(f"chunk_id: {result['chunk_id']}")
    # print(f"Score: {result['@search.score']}")
    # print(f"Content: {result['chunk']}")



def hybrid_query(query, index_name):

    # Hybrid Search
    # query = "Which is more comprehensive, Northwind Health Plus vs Northwind Standard?"

    search_client = SearchClient(AZURE_SEARCH_SERVICE_ENDPOINT, index_name, credential=credential)
    vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=1, fields="vector", exhaustive=True)

    results = search_client.search(
        search_text=query,
        vector_queries= [vector_query],
        select=["parent_id", "chunk_id", "chunk"],
        top=1
    )

    return results

    # for result in results:
    #     print(f"parent_id: {result['parent_id']}")
    #     print(f"chunk_id: {result['chunk_id']}")
    #     print(f"Score: {result['@search.score']}")
    #     print(f"Content: {result['chunk']}")
    


def hybrid_semantic_query(query, index_name):
    
    # Semantic Hybrid Search
    # query = "Which is more comprehensive, Northwind Health Plus vs Northwind Standard?"

    search_client = SearchClient(AZURE_SEARCH_SERVICE_ENDPOINT, index_name, credential)
    vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=1, fields="vector", exhaustive=True)

    results = search_client.search(
        search_text=query,
        vector_queries=[vector_query],
        select=["parent_id", "chunk_id", "chunk"],
        query_type=QueryType.SEMANTIC,
        semantic_configuration_name='my-semantic-config',
        query_caption=QueryCaptionType.EXTRACTIVE,
        query_answer=QueryAnswerType.EXTRACTIVE,
        top=1
    )

    semantic_answers = results.get_answers()
    if semantic_answers:
        for answer in semantic_answers:
            if answer.highlights:
                print(f"Semantic Answer: {answer.highlights}")
            else:
                print(f"Semantic Answer: {answer.text}")
            print(f"Semantic Answer Score: {answer.score}\n")

    return results


    # for result in results:
    #     print(f"parent_id: {result['parent_id']}")
    #     print(f"chunk_id: {result['chunk_id']}")
    #     print(f"Reranker Score: {result['@search.reranker_score']}")
    #     print(f"Content: {result['chunk']}")

    #     captions = result["@search.captions"]
    #     if captions:
    #         caption = captions[0]
    #         if caption.highlights:
    #             print(f"Caption: {caption.highlights}\n")
    #         else:
    #             print(f"Caption: {caption.text}\n")

