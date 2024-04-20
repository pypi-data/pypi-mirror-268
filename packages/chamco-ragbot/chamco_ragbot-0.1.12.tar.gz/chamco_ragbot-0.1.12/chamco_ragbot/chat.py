
import os
import json
import openai
from dotenv import load_dotenv
load_dotenv()


# AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")
# BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
# BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")
# AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")


AZURE_SEARCH_SERVICE_ENDPOINT = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
AZURE_SEARCH_ADMIN_KEY = os.getenv("AZURE_SEARCH_ADMIN_KEY")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_MODEL_DEPLOYMENT = os.getenv("AZURE_OPENAI_MODEL_DEPLOYMENT")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")


client = openai.AzureOpenAI(
    base_url=f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_MODEL_DEPLOYMENT}/extensions",
    api_key=AZURE_OPENAI_KEY,
    api_version="2023-09-01-preview"
)


def chat(query, search_index):
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": query}],
        model=AZURE_OPENAI_MODEL_DEPLOYMENT,
        extra_body={
            "dataSources": [
                {
                    "type": "AzureCognitiveSearch",
                    "parameters": {
                        "endpoint": AZURE_SEARCH_SERVICE_ENDPOINT,
                        "key": AZURE_SEARCH_ADMIN_KEY,
                        "indexName": search_index,
                    }
                }
            ]
        }
    )

    return completion



def get_response(completion):

    role = completion.choices[0].message.role
    response = completion.choices[0].message.content

    return {role: response}

def get_context(completion):
    context = completion.choices[0].message.model_extra['context']['messages'][0]['content']
    parsed_context = parse_context(context)
    return parsed_context


def parse_context(context):
    json_context = json.loads(context)
    citations = json_context['citations']
    intent = json.loads(json_context['intent'])
    parsed_context = {"citations": citations, "intent": intent}
    return parsed_context