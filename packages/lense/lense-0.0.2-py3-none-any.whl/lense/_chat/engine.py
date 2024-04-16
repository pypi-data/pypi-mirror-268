
from langchain.llms import HuggingFaceHub
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.core import VectorStoreIndex
import re
import os
import openai
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core.query_pipeline import (QueryPipeline as QP,Link,InputComponent,)
from llama_index.experimental.query_engine.pandas import PandasInstructionParser
from llama_index.core import PromptTemplate
from llama_index.llms.azure_openai import AzureOpenAI

def embed_and_run_mistral(documents):
    
    pattern = r"Answer: (.*)"
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
    llm = HuggingFaceHub(huggingfacehub_api_token='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',
                        repo_id=repo_id, model_kwargs={"temperature":0.5, "max_new_tokens":100})
 
    embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    index = VectorStoreIndex.from_documents(documents, embed_model = embed_model, show_progress=True)
    query_engine = index.as_query_engine(similarity_top_k=3,llm=llm)
    while True:
        query = input("Query:")
        response = query_engine.query(query)
        response = str(response)
        match = re.search(pattern, response)
        answer = match.group(1)
        print(answer)

def embed_and_run_openai(documents):
    
    os.environ["OPENAI_API_KEY"] = "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"
    openai.api_key = os.environ["OPENAI_API_KEY"]
    index = VectorStoreIndex.from_documents(documents, show_progress=True)#, embed_model = embed_model, show_progress=True,)
    llm = OpenAI(model="gpt-3.5-turbo")
    query_engine = index.as_query_engine(similarity_top_k=3,llm=llm)
    while True:
        query = input("Query:")
        response = query_engine.query(query)
        print(str(response))
    

def embed_and_run_azureopenai(documents):
    



    api_key= "17b15c9c0c3643368bb8e9e2c5ada06f" 
    api_version="2023-07-01-preview"
    azure_endpoint="https://covalenseopenaieastus2.openai.azure.com/"

    llm = AzureOpenAI(
        model="gpt-35-turbo-16k",
        deployment_name="gpt-35-turbo-16k",
        api_key=api_key,
        azure_endpoint=azure_endpoint,
        api_version=api_version,
    )

    # You need to deploy your own embedding model as well as your own chat completion model
    embed_model = AzureOpenAIEmbedding(
        model="text-embedding-ada-002",
        deployment_name="text-embedding-ada-002",
        api_key=api_key,
        azure_endpoint=azure_endpoint,
        api_version=api_version,
    )

    from llama_index.core import Settings
    Settings.llm = llm
    Settings.embed_model = embed_model

    index = VectorStoreIndex.from_documents(documents, show_progress=True)#, embed_model = embed_model, show_progress=True,)
    query_engine = index.as_query_engine(similarity_top_k=3,llm=llm)
    while True:
        query = input("Query:")
        response = query_engine.query(query)
        print(str(response))

def csv_engine(df):
    print(df)
    

    api_key= "17b15c9c0c3643368bb8e9e2c5ada06f" 
    api_version="2023-07-01-preview"
    azure_endpoint="https://covalenseopenaieastus2.openai.azure.com/"

    llm = AzureOpenAI(
        model="gpt-35-turbo-16k",
        deployment_name="gpt-35-turbo-16k",
        api_key=api_key,
        azure_endpoint=azure_endpoint,
        api_version=api_version,
    )

    instruction_str = (
    "1. Convert the query to executable Python code using Pandas.\n"
    "2. The final line of code should be a Python expression that can be called with the `eval()` function.\n"
    "3. The code should represent a solution to the query.\n"
    "4. PRINT ONLY THE EXPRESSION.\n"
    "5. Do not quote the expression.\n"
    f"6. Strictly use column names mentioned below {df.head(1)}")

    pandas_prompt_str = (
        "You are working with a pandas dataframe in Python.\n"
        "The name of the dataframe is `df`.\n"
        "This is the result of `print(df.head())`:\n"
        "{df_str}\n\n"
        "Follow these instructions:\n"
        "{instruction_str}\n"
        "Query: {query_str}\n\n"
        "Expression:")
    
    response_synthesis_prompt_str = (
        "Given an input question, synthesize a response from the query results.\n"
        "Query: {query_str}\n\n"
        "Pandas Instructions (optional):\n{pandas_instructions}\n\n"
        "Pandas Output: {pandas_output}\n\n"
        "Response: ")

    pandas_prompt = PromptTemplate(pandas_prompt_str).partial_format(
        instruction_str=instruction_str, df_str=df.head(5))
    
    pandas_output_parser = PandasInstructionParser(df)
    response_synthesis_prompt = PromptTemplate(response_synthesis_prompt_str)
    # llm = OpenAI(model="gpt-3.5-turbo")

    qp = QP(
    modules={
        "input": InputComponent(),
        "pandas_prompt": pandas_prompt,
        "llm1": llm,
        "pandas_output_parser": pandas_output_parser,
        "response_synthesis_prompt": response_synthesis_prompt,
        "llm2": llm,
    },
    verbose=True,
    )
    qp.add_chain(["input", "pandas_prompt", "llm1", "pandas_output_parser"])
    qp.add_links(
        [
            Link("input", "response_synthesis_prompt", dest_key="query_str"),
            Link(
                "llm1", "response_synthesis_prompt", dest_key="pandas_instructions"
            ),
            Link(
                "pandas_output_parser",
                "response_synthesis_prompt",
                dest_key="pandas_output",
            ),
        ]
    )
    # add link from response synthesis prompt to llm2
    qp.add_link("response_synthesis_prompt", "llm2")

    while True:
        query_str = input("Query:")
        response = qp.run(query_str=query_str,)
        print(response.message.content)

def embed_and_run(embeddings):
    while True:
        choice = input("Please choose the prefered engine: \n1. Azure Openai \n2.Mistral-Ai \n3.CSV engine\n Your Choice (1/2/3): ")
        if choice == '1':
            embed_and_run_azureopenai(embeddings)
        elif choice == '2':
            embed_and_run_mistral(embeddings)
        elif choice == '3':
            csv_engine(embeddings)
        else:
            print("please choose one of the options mentioned")



