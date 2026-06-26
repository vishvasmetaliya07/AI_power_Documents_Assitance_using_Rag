````markdown
# 📄 AI-Powered Documents Assistant using RAG

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-success?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

An AI-powered document assistant that enables users to upload PDF files and ask questions in natural language. The application uses **Retrieval-Augmented Generation (RAG)** to retrieve the most relevant information from uploaded documents and generate accurate, context-aware responses using Large Language Models (LLMs).

---

## 🚀 Live Demo

### 🌐 Web Application

🔗 **https://vishvasmetaliya.streamlit.app/**

---

## 🎥 Video Demo

Watch the complete working demonstration of the project.

🔗 **https://youtu.be/F06QQRH2s1A**

---

## ✨ Features

- 📄 Upload PDF documents
- 💬 Ask questions in natural language
- 🔍 Semantic search using vector embeddings
- 🤖 AI-powered question answering with RAG
- ⚡ Fast and accurate responses
- 🧠 Context-aware document retrieval
- 🎨 Clean and interactive Streamlit interface
- 🔒 Secure API key management using `.env`

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | User Interface |
| LangChain | RAG Pipeline |
| Groq LLM | Response Generation |
| ChromaDB | Vector Database |
| HuggingFace Embeddings | Semantic Embeddings |
| PyPDF | PDF Processing |
| python-dotenv | Environment Variables |

---

## 📁 Project Structure

```text
AI_power_Documents_Assitance_using_Rag/
│
├── app.py
├── main.py
├── requirements.txt
├── .env
├── README.md
└── ChromaDB/
````

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vishvasmetaliya07/AI_power_Documents_Assitance_using_Rag.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd AI_power_Documents_Assitance_using_Rag
```

### 3️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

### 6️⃣ Run the Application

```bash
streamlit run main.py
```

---

## 📷 Screenshots

> Add screenshots or GIFs here to showcase the application interface.

Example:

* Home Page
* Upload PDF
* Chat Interface
* Generated Responses

---

## 📌 How It Works

1. Upload a PDF document.
2. The document is split into smaller chunks.
3. Chunks are converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. User asks a question.
6. Relevant chunks are retrieved using semantic search.
7. Groq LLM generates an accurate response based on the retrieved context.

---

## 🔮 Future Improvements

* 📚 Multiple PDF support
* 💾 Persistent chat history
* 📑 Source citations
* 🖼 OCR support for scanned PDFs
* 🎤 Voice interaction
* 🌍 Multi-language support
* ☁ Cloud database integration
* 📱 Mobile-friendly UI

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Create a Pull Request.

---

## 👨‍💻 Author

### Vishvas Metaliya

* GitHub: https://github.com/vishvasmetaliya07
* LinkedIn: https://www.linkedin.com/in/vishvas-metaliya/

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ **Star** on GitHub.

It helps others discover the project and motivates future improvements.

---

**Made with ❤️ using Python, Streamlit, LangChain, ChromaDB, and Groq LLM**

```
```
