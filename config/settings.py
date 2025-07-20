import os
from typing import Dict, Any

# Qdrant Configuration
QDRANT_CONFIG = {
    "url": os.getenv('QDRANT_URL'),
    "api_key": os.getenv('QDRANT_API_KEY'),
    "collection": "mathbooks_streamlit"
}

# OpenAI Configuration
OPENAI_CONFIG = {
    "api_key": os.getenv('OPENAI_API_KEY'),
    "model_id": "gpt-4o"
}

# Embedder Configuration
EMBEDDER_CONFIG = {
    "dimensions": 384
}

# Streamlit Configuration
STREAMLIT_CONFIG = {
    "page_title": "MathBot - AI Math Tutor",
    "page_icon": "📚",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# File Upload Configuration
UPLOAD_CONFIG = {
    "max_file_size": 50,  # MB
    "allowed_extensions": [".pdf"],
    "upload_dir": "docs"
}

# Chat Configuration
CHAT_CONFIG = {
    "max_messages": 50,
    "system_prompt": """You are MathBot, an AI math tutor. You help students understand mathematical concepts by:
1. Explaining concepts clearly and step-by-step
2. Providing examples when helpful
3. Referencing specific sections from the uploaded math books
4. Encouraging learning and problem-solving

Always cite which book/document you're referencing when answering questions."""
}
