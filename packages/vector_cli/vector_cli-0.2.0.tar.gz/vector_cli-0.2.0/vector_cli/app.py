import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader


client = OpenAI()
embeddings = OpenAIEmbeddings()


def upsert_faiss_index(db):
    """Create and return a FAISS index if it does not exist."""
    if os.path.exists("faiss_index"):
        old_db = FAISS.load_local(
            "faiss_index", embeddings, allow_dangerous_deserialization=True
        )
        old_db.merge_from(db)
        old_db.save_local("faiss_index")
    else:
        db.save_local("faiss_index")


def get_openai_embedding(text):
    """Get embedding from OpenAI."""
    response = client.embeddings.create(
        input=[text],
        model="text-embedding-ada-002",  # You can choose other models like babbage or davinci
    )
    return response.data[0].embedding


def index_documents(folder_path):
    """Load documents, process embeddings, add to index, and save documents to file."""
    loader = DirectoryLoader(folder_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=60)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    upsert_faiss_index(db)


def query_index(query, k=5):
    """Query the FAISS index with a given string to find the top k similar items."""
    index = FAISS.load_local(
        "faiss_index", embeddings, allow_dangerous_deserialization=True
    )
    return index.similarity_search(query, k)


def get_openai_response(user_question):
    results = query_index(user_question)
    # Combine the question and the documents into a single prompt
    prompt = f"Answer users Question using SOURCES below.\n\nSOURCES:".join(
        [f"{doc.page_content}\n\n" for i, doc in enumerate(results)]
    ).join(
        f"\nQuestion: {user_question}\n\nFinal Answer:"
    )

    # print("Prompt: ", prompt)

    # Send the prompt to the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    # print(response)
    print(response.choices[0].message.content)
