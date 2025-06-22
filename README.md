# 🔍 fan-out-query-translation

A Query Translation module that splits a user query into semantically diverse sub-queries for high-recall document retrieval in RAG pipelines.  
Built using **OpenAI GPT-4o**, **LangChain**, and **Qdrant**.

---

## 🚀 Features

- ✅ Converts a user query into **3 semantically diverse sub-queries**
- ✅ Uses **OpenAI GPT-4o** to generate structured JSON output
- ✅ Embeds the sub-queries with `text-embedding-3-large`
- ✅ Stores and retrieves embeddings from **Qdrant (Dockerized)**
- ✅ Performs **parallel fan-out retrieval**
- ✅ Combines relevant chunks and generates a **final AI response**

---

## 🛠️ Tech Stack

| Component         | Tool/Library              |
|------------------|---------------------------|
| LLM               | OpenAI GPT-4o             |
| Embeddings        | OpenAI `text-embedding-3-large` |
| Vector Store      | Qdrant                    |
| Framework         | LangChain                |
| Runtime           | Docker, Python            |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fan-out-query-translation.git
cd fan-out-query-translation
```

---

### 2. Set up the Environment

Create a `.env` file in the root directory with the following content:

```env
OPENAI_API_KEY=your-openai-api-key-here
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Run Qdrant using Docker

If you have Docker installed, run Qdrant like this:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

Or use the included `docker-compose-db.yml` if available:

```bash
docker-compose -f docker-compose-db.yml up
```

---

## ▶️ Usage

Run the script:

```bash
python query_translation.py
```

Then enter your query in the terminal prompt:

```
>> How can AI help improve education in rural areas?
```

---

### 🧠 What It Does

1. Takes your query
2. Splits it into 3 diverse sub-queries using GPT-4o
3. Embeds and stores them in Qdrant
4. Retrieves relevant context for each
5. Combines the context and gives a **final answer**

---

## 💡 Example Output

```json
User Query: How can AI help improve education in rural areas?

Sub-Queries:
- Applications of AI in rural school systems
- Educational tools powered by AI for low-connectivity areas
- Case studies of AI improving rural education

Final Response:
AI can improve education in rural areas through intelligent tutoring systems, low-bandwidth learning tools, and localized content delivery supported by NLP.
```

---

## 📂 Folder Structure

```
fan-out-query-translation/
├── query_translation.py
├── docker-compose-db.yml
├── .env
├── requirements.txt
└── README.md
```

---

## 🤝 Acknowledgements

- [OpenAI](https://openai.com/)
- [LangChain](https://www.langchain.com/)
- [Qdrant](https://qdrant.tech/)
- [Docker](https://www.docker.com/)

---

## 👨‍💻 Author

**Syed Shabib Ahamed**  
Aspiring GenAI Developer | BTech AI & DS | Class of 2026  
🔗 [GitHub](https://github.com/Shabib6)  
🔗 [LinkedIn](https://www.linkedin.com/in/syed-shabib-ahamed-b673b0225/)

---

## ⭐️ Support

If you find this repo useful, please consider leaving a ⭐️ and sharing it with your GenAI friends!
