import streamlit as st
import os
import hashlib
import warnings
from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser

warnings.filterwarnings("ignore")
load_dotenv()

st.set_page_config(page_title=" AI Document Assistant", page_icon="📖", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0F1419;
    color: #E6E8EB;
}

section[data-testid="stSidebar"] {
    background: #12161C;
    border-right: 1px solid #232A33;
}

section[data-testid="stSidebar"] * {
    color: #E6E8EB;
}

h1, h2, h3 {
    font-family: 'Fraunces', serif;
    color: #F2E8D5;
    letter-spacing: -0.01em;
}

.doc-hero {
    border-bottom: 1px solid #232A33;
    padding-bottom: 1.2rem;
    margin-bottom: 1.5rem;
}

.doc-hero h1 {
    font-size: 2.1rem;
    margin-bottom: 0.2rem;
}

.doc-hero p {
    color: #8B949E;
    font-size: 0.95rem;
    margin: 0;
}

.status-pill {
    display: inline-block;
    background: rgba(212, 165, 55, 0.12);
    border: 1px solid rgba(212, 165, 55, 0.35);
    color: #D4A537;
    padding: 0.3rem 0.8rem;
    border-radius: 999px;
    font-size: 0.82rem;
    font-family: 'Inter', sans-serif;
}

[data-testid="stChatMessage"] {
    background: #161B22;
    border: 1px solid #232A33;
    border-radius: 14px;
    padding: 0.4rem 0.6rem;
}

div[data-testid="stChatInput"] textarea {
    background: #161B22 !important;
    color: #E6E8EB !important;
    border: 1px solid #2A323D !important;
}

.source-note {
    border-left: 3px solid #D4A537;
    background: #161B22;
    padding: 0.6rem 0.9rem;
    margin-bottom: 0.6rem;
    border-radius: 0 8px 8px 0;
    font-family: 'Fraunces', serif;
    font-size: 0.9rem;
    color: #C9CDD3;
}

.source-note span {
    display: block;
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #D4A537;
    margin-bottom: 0.25rem;
}

.stButton button {
    background: #D4A537;
    color: #0F1419;
    border: none;
    font-weight: 600;
    border-radius: 8px;
}

.stButton button:hover {
    background: #E5B94A;
    color: #0F1419;
}
</style>
""", unsafe_allow_html=True)

PROMPT = ChatPromptTemplate.from_template("""
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

@st.cache_resource(show_spinner=False)
def load_llm():
    return ChatGroq(model="llama-3.3-70b-versatile")

@st.cache_resource(show_spinner=False)
def build_vectorstore(file_path, file_hash):
    pdf = PyPDFLoader(file_path)
    data = pdf.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    chunk_data = splitter.split_documents(data)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(
        documents=chunk_data,
        embedding=embeddings,
        persist_directory=os.path.join("ChromaDb", file_hash)
    )
    return db

def get_chain(llm):
    return PROMPT | llm | StrOutputParser()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "doc_name" not in st.session_state:
    st.session_state.doc_name = None

with st.sidebar:
    st.markdown("### 📖AI Document Assistant ")
    st.caption("AI Document Assistant")
    st.divider()
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    process_clicked = st.button("Process Document", use_container_width=True)
    st.divider()
    show_chunks = st.toggle("Show source passages", value=True)
    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

st.markdown("""
<div class="doc-hero">
<h1>AI Power Documents</h1>
<p>Ask questions about your document. Answers are grounded strictly in its content.</p>
</div>
""", unsafe_allow_html=True)

if process_clicked and uploaded_file is not None:
    with st.spinner("Reading and indexing document..."):
        file_bytes = uploaded_file.getvalue()
        file_hash = hashlib.md5(file_bytes).hexdigest()
        os.makedirs("uploaded_docs", exist_ok=True)
        file_path = os.path.join("uploaded_docs", f"{file_hash}.pdf")
        with open(file_path, "wb") as f:
            f.write(file_bytes)
        st.session_state.vectorstore = build_vectorstore(file_path, file_hash)
        st.session_state.doc_name = uploaded_file.name
    st.success(f"'{uploaded_file.name}' is indexed and ready.")

if st.session_state.vectorstore is not None:
    st.markdown(f'<span class="status-pill">Active document: {st.session_state.doc_name}</span>', unsafe_allow_html=True)
else:
    st.info("Upload a PDF in the sidebar and click 'Process Document' to begin.")

st.write("")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and show_chunks and msg.get("chunks"):
            with st.expander("Source passages"):
                for i, chunk in enumerate(msg["chunks"], start=1):
                    st.markdown(f'<div class="source-note"><span>Passage {i}</span>{chunk[:400]}</div>', unsafe_allow_html=True)

user_input = st.chat_input("Ask a question about the document...")

if user_input:
    if st.session_state.vectorstore is None:
        st.warning("Please upload and process a document first.")
    else:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        retriever = st.session_state.vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult": 0.5}
        )

        with st.chat_message("assistant"):
            with st.spinner("Searching document..."):
                docs = retriever.invoke(user_input)

            if not docs:
                answer = "No relevant context found in the document."
                st.markdown(answer)
                chunks = []
            else:
                context = "\n\n".join(doc.page_content for doc in docs)
                llm = load_llm()
                chain = get_chain(llm)
                with st.spinner("Generating answer..."):
                    answer = chain.invoke({"context": context, "question": user_input})
                st.markdown(answer)
                chunks = [doc.page_content for doc in docs]

                if show_chunks:
                    with st.expander("Source passages"):
                        for i, chunk in enumerate(chunks, start=1):
                            st.markdown(f'<div class="source-note"><span>Passage {i}</span>{chunk[:400]}</div>', unsafe_allow_html=True)

        st.session_state.messages.append({"role": "assistant", "content": answer, "chunks": chunks})
