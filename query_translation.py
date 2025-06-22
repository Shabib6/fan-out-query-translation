#Query Translation Phase - Parallel Query (Fan Out) Retrieval
#This script generates semantically diverse sub-queries from a user query using OpenAI's GPT-4o model.
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_qdrant import QdrantVectorStore

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = """
You are a helpful assistant that follows Parallel Query (Fan Out) Retrieval.
Given a user query, your task is to generate 3 semantically diverse sub-queries that can be used to retrieve relevant documents.
Return the output as a JSON object with the format:
{
    "queries": [
        "First sub-query",
        "Second sub-query",
        "Third sub-query"
    ]
}
"""
messages = [
    {"role" : "system" , "content": system_prompt}
]

while True:
    user_query = input(">>")
    messages.append(
    {"role":"user" , "content": user_query}
        )
    
    response = client.chat.completions.create(
        model = "gpt-4o",
        response_format={"type": "json_object"},
        messages=messages
    )
    parsed_response = json.loads(response.choices[0].message.content) # gives a dict with 3 queries splitted
    messages.append(
        {"role": "assistant", "content": response.choices[0].message.content}
        )
    sub_queries = parsed_response["queries"]
    docs = [Document(page_content=q) for q in sub_queries]

    #Embeddding
    embedder = OpenAIEmbeddings(
    model= "text-embedding-3-large",
    api_key=os.getenv("OPENAI_API_KEY")
    )

    #Storing the embeddings in Qdrant
    vector_store = QdrantVectorStore.from_documents(
        documents=docs,
        url="http://localhost:6333",
        collection_name="query_subqueries",
        embedding=embedder
    )
    #vector_store.add_documents(documents = split_docs)

    retriever = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="query_subqueries",
    embedding=embedder
    )

    #Using retriever to get relevant documents for each sub-query
    all_chunks = []
    for q in sub_queries:
        results = retriever.similarity_search(query=q, k=3)
        all_chunks.extend(results)  # collect all chunks here
        print(f"Sub-query: {q}")
        for res in results:
            print(res.page_content)
        print("\n---\n")

    print("Sub-queries generated and documents retrieved successfully.")

    #Combining all the relevant chunks to get the final response
    system_prompt2 = """
    You are a helpful assistant. You have been provided with relevant context chunks retrieved from a knowledge base in response to a user's question. 
    Using only this information, answer the user's query as accurately and concisely as possible. If the answer is not found in the context, respond accordingly.
    """
    # Step 1: Combine all chunks
    context_chunks = "\n\n".join([chunk.page_content for chunk in all_chunks])

    # Step 2: Create a new message list
    final_messages = [
        {"role": "system", "content": system_prompt2},
        {"role": "user", "content": f"User Query: {user_query}\n\nRelevant Chunks:\n{context_chunks}"}
    ]

    final_reponse = client.chat.completions.create(
        model="gpt-4o",
        messages=final_messages)

    print(f"Final Response: {final_reponse.choices[0].message.content}")