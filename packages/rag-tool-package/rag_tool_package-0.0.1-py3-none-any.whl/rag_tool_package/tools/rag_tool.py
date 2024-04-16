from promptflow.core import tool
from promptflow.connections import CustomConnection

from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
from llama_index.llms.mistralai import MistralAI
from llama_index.embeddings.mistralai import MistralAIEmbedding
from llama_index.core import Settings

llm = MistralAI(model="mistral-medium", temperature=0.1) # models: mistral-tiny, mistral-small, mistral-medium, mistral-large, open-mixtral-8x7b, open-mistral-7b, mistral-small-latest, mistral-medium-latest, mistral-large-latest
embed_model = MistralAIEmbedding(model_name="mistral-embed")

Settings.llm = llm
Settings.embed_model = embed_model

documents = SimpleDirectoryReader("tool_data").load_data()
index = VectorStoreIndex.from_documents(documents, show_progress=True)

query_engine = index.as_query_engine()

@tool
def rag_answer(connection: CustomConnection, input_text: str) -> str:
    response = query_engine.query(input_text)
    return response

    # Replace with your tool code.
    # Usually connection contains configs to connect to an API.
    # Use CustomConnection is a dict. You can use it like: connection.api_key, connection.api_base
    # Not all tools need a connection. You can remove it if you don't need it.
    # return "Hello " + input_text
