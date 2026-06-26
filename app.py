from langchain_groq.chat_models import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from  langchain_core.prompts  import ChatPromptTemplate
from  langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
import warnings

warnings.filterwarnings("ignore")


# load the Documents
pdf=PyPDFLoader(
    "deep-learning-material-dept-ece-ase-blr-1.pdf"
)

data=pdf.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " ", ""]
)

chunk_data=splitter.split_documents(data)

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db=Chroma.from_documents(
    documents=chunk_data,
    embedding=embeddings,
    persist_directory="ChromaDb"   
)


llm=ChatGroq(
    model="llama-3.3-70b-versatile"
)

retrivers=db.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)  





prompt = ChatPromptTemplate.from_template("""
You are an AI-powered Document Assistant.

Use ONLY the provided context to answer the user's question.

Instructions:
- Do not use outside knowledge.
- If the answer is present in the context, explain it clearly in one or more well-structured paragraphs.
- If the answer is not present in the context, reply exactly:

"The requested information is not available in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
""")


chain= prompt | llm | StrOutputParser()

# from rich import print

from rich import print

print("__" * 100)

while True:
    user = input("Enter your question (type 'exit' to quit): ").strip()

    if user.lower() == "exit":
        print("Goodbye 👋")
        break

    print("\nSearching document...\n")

    # Retrieve relevant documents
    docs = retrivers.invoke(user)

    if not docs:
        print("No relevant context found.")
        continue

    # Show retrieved chunks (Debug)
    print(f"Retrieved {len(docs)} document(s)\n")

    for i, doc in enumerate(docs, start=1):
        print(f"========== Chunk {i} ==========")
        print(doc.page_content[:400])
        print()

    # Build context
    context = "\n\n".join(doc.page_content for doc in docs)

    # Generate answer
    response = chain.invoke(
        {
            "context": context,
            "question": user,
        }
    )

    print("=" * 100)
    print("Answer:\n")
    print(response)
    print("=" * 100)





