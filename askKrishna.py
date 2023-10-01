# Author: Prashant Mittal

#!/usr/bin/env python3
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import LlamaCpp
import os
import time

from constants import CHROMA_SETTINGS

load_dotenv()

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get("PERSIST_DIRECTORY")

model_type = os.environ.get("MODEL_TYPE")
model_path = os.environ.get("MODEL_PATH")
model_n_ctx = os.environ.get("MODEL_N_CTX")
model_n_batch = int(os.environ.get("MODEL_N_BATCH", 8))
target_source_chunks = int(os.environ.get("TARGET_SOURCE_CHUNKS", 4))


def ask_question(query):
    query = (
        "Respond to query in this manner - Insightful answers as per the teachings of Lord Krishna in Bhagvad Gita, also provide quote by Him. Query: "
        + query
    )
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
        client_settings=CHROMA_SETTINGS,
    )
    retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})

    # Prepare the LLM
    llm = LlamaCpp(
        model_path=model_path,
        n_ctx=model_n_ctx,
        n_batch=model_n_batch,
        callbacks=[],
        verbose=False,
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False,
    )

    # Get the answer from the chain
    start = time.time()
    res = qa(query)
    answer = res["result"]
    end = time.time()

    # Print the result
    print("\n\n> Question:")
    print(query)
    print(f"\n> Answer (took {round(end - start, 2)} s.):")
    print(answer)

    return answer


if __name__ == "__main__":
    query = input("> Query: ")
    ask_question(query)
