````markdown
# 📄 AI-Powered Documents Assistant using RAG

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-RAG-00C853?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-7B1FA2?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-F9A825?style=for-the-badge)

</p>

<p align="center">

<a href="https://vishvasmetaliya.streamlit.app/" target="_blank">
<img src="https://img.shields.io/badge/🚀%20Live%20Demo-Visit%20App-FF4B4B?style=for-the-badge">
</a>

<a href="https://youtu.be/F06QQRH2s1A" target="_blank">
<img src="https://img.shields.io/badge/🎥%20Watch-Demo-red?style=for-the-badge&logo=youtube&logoColor=white">
</a>

<a href="https://github.com/vishvasmetaliya07/AI_power_Documents_Assitance_using_Rag" target="_blank">
<img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github">
</a>

</p>

---

## 📖 Overview

**AI-Powered Documents Assistant** is a Retrieval-Augmented Generation (**RAG**) application that allows users to upload PDF documents and interact with them using natural language.

Instead of searching manually through lengthy documents, users can simply ask questions, and the AI retrieves the most relevant information before generating accurate, context-aware answers using a Large Language Model.

---

## 🚀 Live Application

🌐 **Web App**

👉 **https://vishvasmetaliya.streamlit.app/**

---

## 🎥 Video Demonstration

Watch the complete working demo on YouTube.

▶️ **https://youtu.be/F06QQRH2s1A**

---

# ✨ Features

- 📄 Upload PDF documents
- 💬 Chat with uploaded documents
- 🔍 Semantic search using embeddings
- 🤖 Retrieval-Augmented Generation (RAG)
- ⚡ Fast and accurate AI responses
- 🧠 Context-aware document retrieval
- 📚 ChromaDB Vector Store
- 🔒 Secure API key management with `.env`
- 🎨 Simple and responsive Streamlit UI

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | User Interface |
| LangChain | RAG Pipeline |
| Groq LLM | AI Response Generation |
| ChromaDB | Vector Database |
| HuggingFace Embeddings | Semantic Search |
| PyPDF | PDF Parsing |
| python-dotenv | Environment Variables |

---

# 📁 Project Structure

```text
AI_power_Documents_Assitance_using_Rag/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .env
└── ChromaDB/
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/vishvasmetaliya07/AI_power_Documents_Assitance_using_Rag.git
```

### Navigate to Project

```bash
cd AI_power_Documents_Assitance_using_Rag
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Application

```bash
streamlit run main.py
```

---

# 📌 How It Works

```text
Upload PDF
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
Ask Question
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Groq LLM
      │
      ▼
Generate Accurate Answer
```

---

# 🔮 Future Improvements

- 📂 Multiple PDF support
- 💾 Persistent Chat History
- 📑 Source Citations
- 🖼 OCR for Scanned PDFs
- 🎙 Voice-based Chat
- 🌍 Multi-language Support
- ☁ Cloud Database Integration
- 📱 Mobile Responsive UI

---

# 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repository

# Create a feature branch
git checkout -b feature-name

# Commit your changes
git commit -m "Added new feature"

# Push changes
git push origin feature-name
```

Then open a Pull Request.

---

# 👨‍💻 Author

## Vishvas Metaliya

🐙 GitHub  
https://github.com/vishvasmetaliya07

💼 LinkedIn  
https://www.linkedin.com/in/vishvas-metaliya/

---

# ⭐ Support

If you like this project, consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates future improvements.

---

<p align="center">

### ❤️ Made with Python • Streamlit • LangChain • ChromaDB • Groq LLM

**Thanks for visiting! ⭐**

</p>
````
