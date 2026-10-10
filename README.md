# Gen-AI

My learning log for **Generative AI engineering** and the **Python data/ML stack** behind it. Each folder holds small, runnable examples (scripts and notebooks).

## What's Inside

| Folder | Topics |
|---|---|
| `LangChain/` | Prompts, output parsers, chains, runnables (LCEL), text splitters, embeddings, vector stores (Chroma, Pinecone), retrievers, tools, RAG |
| `Langgraph/` | Stateful workflows: sequential, parallel, and conditional graphs, plus an essay evaluator |
| `Skit-Learn/` | Linear and logistic regression from scratch: cost function, gradient descent, feature scaling |
| `numpy/`, `pandas/`, `mathplotlib/` | Data handling and visualisation basics |
| `practise/` | Python practice |

**Featured:** a **YouTube RAG chatbot** (`LangChain/Rag/yt_chatbot.ipynb`) that fetches a transcript, chunks and embeds it into Chroma, retrieves relevant context, and answers with Gemini.

## Getting Started

```bash
git clone https://github.com/anshdev44/Gen-AI.git
cd Gen-AI
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r LangChain/requirements.txt
pip install langgraph langchain-community langchain-chroma langchain-pinecone \
            pinecone youtube-transcript-api duckduckgo-search pandas matplotlib jupyter
```

Create a `.env` file (never commit it):

```env
GOOGLE_API_KEY=your_key
PINECONE_API_KEY=your_key
HF_TOKEN=your_key
```

## Tech Stack

LangChain · LangGraph · Google Gemini · Hugging Face · Chroma · Pinecone · NumPy · Pandas · scikit-learn · Jupyter

## Author

**Ansh Ahuja**: [GitHub](https://github.com/anshdev44) 
