# Bhagvad Gita GPT

Ask questions to Lord Krishna using the power of Meta's Llama 2 7b LLM. You can download it and ask questions without an internet connection!

Built with [LangChain](https://github.com/hwchase17/langchain), [LlamaCpp](https://github.com/ggerganov/llama.cpp), [Chroma](https://www.trychroma.com/) and [SentenceTransformers](https://www.sbert.net/).

## Environment Setup

In order to set your environment up to run the code here, first install all requirements:

```shell
pip3 install -r requirements.txt
```

Then, download the LLM model and place it in a directory of your choice:

- LLM: default to [llama-2-7b-chat.ggmlv3.q8_0.bin](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin). If you prefer a different compatible model, just download it and reference it in your `.env` file.

## Ask questions to Lord Krishna !!

In order to ask a question, run a command like:

```shell
python app.py
```

And wait for the script to load the web page.

- Enter your query.

- Hit send and wait.

- Hit reset to clear output.

You'll need to wait 100-120 seconds (depending on your machine) while the LLM model consumes the prompt and prepares the answer.

## Data persistence

In order to save the queries to not vanish after running server again:

- Queries and answers are saved in `queries/queries.txt`.

- Click reset to clear `queries/queries.txt`.

## Add data to Lord Krishna directory

Put any and all your Gita pdf files into the `source_documents` directory.

Run the following command to ingest all the data.

```shell
python ingest.py
```

#### Note: You could ingest without an internet connection, except for the first time you run the ingest script, when the embeddings model is downloaded.

#### Note: you could turn off your internet connection, and the script inference would still work.

# How does it work?

- `app.py` uses Flask to create APIs for asking queries to Lord Krishna which runs `ask_krishna` function from `askKrishna.py`.
- `ingest.py` uses `LangChain` tools to parse the document and create embeddings locally using `HuggingFaceEmbeddings` (`SentenceTransformers`). It then stores the result in a local vector database using `Chroma` vector store.
- `askKrishna.py` uses a local LLM based on `LlamaCpp` to understand questions and create answers. The context for the answers is extracted from the local vector store using a similarity search to locate the right piece of context from the docs.

# System Requirements

## Python Version

To use this software, you must have Python 3.10 or later installed. Earlier versions of Python will not compile.
