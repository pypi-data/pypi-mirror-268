from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain import hub
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain_openai import ChatOpenAI
from promptflow import tool

from typing import List, Dict

models={
    'mistralai': [ChatMistralAI, MistralAIEmbeddings],
    'openai': [ChatOpenAI, OpenAIEmbeddings],
}
loaders={
    'csv': CSVLoader,
}

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def list_model_names(group: str = 'embeddings') -> List[Dict[str, str]]:
    models = ['openai', 'mistralai', group]
    result = []
    for model in models:
        item = {
            "value": model,
            # "display_value": model,
            # # external link to jump to the endpoint page.
            # "hyperlink": hyperlink,
            # "description": f"this is endpoint: {ep.name}",
        }
        result.append(item)
        
    return result

# model: opanenai or mistralai  # for mistral need os.environ['MISTRAL_API_KEY']
@tool
def rag_answer(
                query:str,
                file_path:str,
                model_name:str = 'openai', # mistralai
                chunk_size:int = 1000,
                chunk_overlap:int = 200
            ):
    file_format = file_path.split('.')[-1]
    loader_class = loaders.get(file_format)
    loader = loader_class(file_path=file_path)
    data = loader.load()
    
    model_group = models[model_name]
    model_llm = model_group[0]
    model_emb = model_group[1]
    llm = model_llm()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    splits = text_splitter.split_documents(data)
    vectorstore = Chroma.from_documents(documents=splits, embedding=model_emb())
    

    retriever = vectorstore.as_retriever()
    prompt = hub.pull("rlm/rag-prompt") # to explore



    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )


    result = rag_chain.invoke(query)
    return result

