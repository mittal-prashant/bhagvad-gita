# Author: Prashant Mittal

from flask import Flask, render_template, request, redirect
import os
from askLLM import ask_question

app = Flask(__name__)


# List to store queries and responses
queries = []


@app.route("/")
def index():
    return redirect("/home")


def save_queries_to_file():
    with open(f"queries/queries.txt", "w") as file:
        for query_response in queries:
            query = query_response["query"]
            response = query_response["response"]
            file.write(f"Query: {query}\n")
            file.write(f"Response: {response}\n")


def load_queries_from_file():
    query = ""
    response = ""
    if os.path.isfile(f"queries/queries.txt"):
        queries.clear()
        with open(f"queries/queries.txt", "r") as file:
            is_query = False
            is_response = False
            for line in file:
                line = line.strip()
                if (
                    line.startswith("Response:") or is_response
                ) and not line.startswith("Query:"):
                    is_response = True
                    if line.startswith("Response:"):
                        response += line[10:]
                    else:
                        response += line
                elif line.startswith("Query:") or is_query:
                    if response != "":
                        queries.append({"query": query, "response": response})
                    response = ""
                    query = ""
                    is_query = True
                    if line.startswith("Query:"):
                        query += line[7:]
                    else:
                        query += line
            if response != "":
                queries.append({"query": query, "response": response})


@app.route("/home")
def home():
    load_queries_from_file()
    return render_template("index.html", queries=queries)


@app.route("/query", methods=["POST"])
def query():
    # Get the user query from the AJAX request
    user_query = request.form["query"]

    # Run the second function and capture its output
    output = ask_question(user_query)

    print(output)

    # Create a dictionary with query and response
    query_response = {"query": user_query, "response": output}

    # Add the query and response to the list
    queries.append(query_response)
    save_queries_to_file()

    return output


@app.route("/reset", methods=["POST"])
def reset_queries():
    queries.clear()
    save_queries_to_file()
    return redirect("/home")


if __name__ == "__main__":
    app.run(debug=True)
