import os
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

os.environ["OPENAI_API_KEY"] = "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"

if not os.path.exists("./storage"):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist()
else:
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)


def get_response(question: str):
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    return response
