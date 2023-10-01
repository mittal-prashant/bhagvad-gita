# Bhagvad Gita GPT

### Author: Prashant Mittal

Ask questions to Lord Krishna using the power of Meta's Llama 2 7b LLM. You can download it and ask questions without an internet connection!

Built with [LangChain](https://github.com/hwchase17/langchain), [LlamaCpp](https://github.com/ggerganov/llama.cpp), [Chroma](https://www.trychroma.com/) and [SentenceTransformers](https://www.sbert.net/).

## Deployment on GCP(Google Cloud Platform)

The application is deployed using Google Cloud Platform in `asia-south1` region on a Kubernetes cluster with 4 pods. The resources are only of Free Tier so it may be slow than running at Localhost.

Link to the website: http://34.93.219.52:5000/home

## Running Container on Docker

### Environment Setup

### A. System Requirements

Latest version of Docker should be installed.

### B. Run container

In order to run a container, we have to pull the [mittalprashant/bhagvad-gita-gpt](https://hub.docker.com/r/mittalprashant/bhagvad-gita-gpt) from Docker Hub.

```shell
docker pull mittalprashant/bhagvad-gita-gpt
```

Run the container using following command:

```shell
docker run -p 5000:5000 --name bhagvad-gita-gpt bhagvad-gita-gpt
```

And the service would be running on https://localhost:5000.

### C. Run using Bash command

Make sure that run.sh is present in the working directory.

Run the following command to make bash file exectuable.

```shell
chmod +x run.sh
```

Then run the bash file to create a container.

```shell
./run.sh
```

Open https://localhost:5000 to ask question to Lord Krishna.

## Running Locally

### A. System Requirements

#### Python Version

To use this software, you must have Python 3.10 or later installed. Earlier versions of Python will not compile.

### B. Environment Setup

In order to set your environment up to run the code here, first install all requirements:

```shell
pip3 install -r requirements.txt
```

Then, download the LLM model and place it inside models directory:

- LLM: default to [llama-2-7b-chat.ggmlv3.q8_0.bin](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin). If you prefer a different compatible model, just download it and reference it in your `.env` file.

Run ingest.py file to extract the information from documents.

```shell
python ingest.py
```

### C. Ask questions to Lord Krishna !!

In order to ask a question, run a command like:

```shell
python app.py
```

And wait for the script to load the web page.

- Enter your query.
- Hit send and wait.
- Hit reset to clear output.

You'll need to wait 100-120 seconds (depending on your machine) while the LLM model consumes the prompt and prepares the answer.

## Running on Kubernetes Cluster

### A. Environment Setup

Make sure the Kubernetes cluster is running and kubectl command is available.

If run locally using minikube then use the command to start the server.

```shell
minikube start
```

### B. Deployment on cluster

Make sure the deployment.yaml file is present inside the working directory.

To deploy the service on the Kubernetes cluster locally use the following command:

```shell
kubectl apply -f deployment.yaml
```

If it has to be deployed on a cloud service, make sure you change the service type to LoadBalancer for better performance before using above command.

On local sytem, you can ask questions to Lord Krishna, exposing the service using command:

```
minikube service bhagvad-gita-service
```

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

## How does it work?

- `app.py` uses Flask to create APIs for asking queries to Lord Krishna which runs `ask_krishna` function from `askKrishna.py`.
- `ingest.py` uses `LangChain` tools to parse the document and create embeddings locally using `HuggingFaceEmbeddings` (`SentenceTransformers`). It then stores the result in a local vector database using `Chroma` vector store.
- `askKrishna.py` uses a local LLM based on `LlamaCpp` to understand questions and create answers. The context for the answers is extracted from the local vector store using a similarity search to locate the right piece of context from the docs.
- `Dockerfile` holds the meta data of how the container image has to be created and what commands need to be run.
- `.github/workflows/deploy.yml` tells the Github actions to run a workflow based on the steps mentioned inside the deploy.yml, then it creates an image and push it on Docker Hub.
- `run.sh` file is a bash file, which can be easily run in the Linux to avoid any errors in commands and directly run docker container.
- `deployment.yaml` is a manifest file for Kubernetes cluster, it stores the no of replica count, type of service and other meta data for running a service on Kubernetes cluster.

## Learnings

You can find answer to every problem inside Bhagvat Gita, you just have to be look inside it and be patient.
