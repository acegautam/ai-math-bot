from agno.agent import Agent
# from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.knowledge.pdf import PDFKnowledgeBase  # <-- Use this for local PDFs
from agno.embedder.sentence_transformer import SentenceTransformerEmbedder
# from agno.embedder.huggingface import HuggingfaceCustomEmbedder
from agno.vectordb.qdrant import Qdrant
# from agno.models.google import Gemini
from agno.models.openai import OpenAIChat

import os

# Qdrant Cloud configuration
vector_db = Qdrant(
    # collection="recipes",
    # collection="rsmmath",
    # collection="mathpdfs",
    collection="mathbooks",
    url=os.environ.get('QDRANT_URL'),
    api_key=os.environ.get('QDRANT_API_KEY'),
)

# Embedder setup
embedder = SentenceTransformerEmbedder(dimensions=384)  # Huggingface 

# embedder = HuggingfaceCustomEmbedder(api_key=os.environ.get('HUGGINGFACE_API_KEY'))
print("------ Model used ------:", embedder.prompt)

# Define multiple knowledge bases
books = [
    {"name": "RSM BYOM Grade 8", "path": "/Users/acegautam/batworld/play/aiml/agenticai/rag/docs/RSM_BYOM_Grade_8_Algebra.pdf"},
    {"name": "Geometry Vol 2 Ch 13.4", "path": "/Users/acegautam/batworld/play/aiml/agenticai/rag/docs/MathLessons.pdf"},
]

# Load all books into the shared vector store
for book in books:
    kb = PDFKnowledgeBase(
        path=book["path"],
        vector_db=vector_db,
        embedder=embedder,
        metadata={"source": book["name"]},  # metadata tagging
    )
    kb.load(recreate=False)  # set to True only for first time


print("All books indexed successfully into vector DB.")

# Knowledge base from a PDF URL
# knowledge_base = PDFUrlKnowledgeBase(
#     # urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
#     vector_db=vector_db,
#     embedder=embedder,
# )

# Knowledge Base: Load from local PDF
# knowledge_base = PDFKnowledgeBase(
#     path="/Users/acegautam/batworld/play/aiml/agenticai/rag/sorted_math_lesson.pdf",
#     vector_db=vector_db,
#     embedder=embedder,
# )
# Load the knowledge base (first run only)
# knowledge_base.load(recreate=True)

# Create an agent using Gemini
agent = Agent(
    # model=Gemini(id="gemini-2.0-flash", api_key=GEMINI_API_KEY),
    model=OpenAIChat(id="gpt-4o", api_key=os.environ.get('OPENAI_API_KEY')),
    knowledge=kb,
)

# Example query to test multiple pdfs
query = "What are Polynomial equations and where is it explained best among these books? Make sure you use the math books to answer this question first."
agent.print_response(query, markdown=True)

# Ask a question
# agent.print_response("What is the topic for Chapter 13.4?", markdown=True)
# agent.print_response("What is the topic for Lesson 2?", markdown=True)
# agent.print_response("How to make Thai curry?", markdown=True)
