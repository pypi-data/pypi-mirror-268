import os
import openai
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage, SimpleDirectoryReader, PromptTemplate

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.environ["OPENAI_API_KEY"]

def get_index( data, index_name):
    index = None
    print("building index", index_name)
    index = VectorStoreIndex.from_documents(data, show_progress=True)
    index.storage_context.persist(persist_dir=index_name)
    return index

def load_index(index_name):
    index = None
    index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index

def load_data(folder):
    reader = SimpleDirectoryReader(folder)
    documents = reader.load_data()
    print(type(documents))
    print(documents)
    return documents

if not os.path.exists("test_data_embeddings"):
    report_pdf = load_data('C:/Users/vamsi.bonamukkala/Desktop/Work/SDK/data')
    report_index, time_stamp = get_index(report_pdf, "test_data_embeddings")
else:
    report_index, time_stamp = load_index( "test_data_embeddings")