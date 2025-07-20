"""
MathBot for Hugging Face Spaces deployment
This is the entry point for Hugging Face Spaces
"""

import os
import streamlit as st

# For HuggingFace Spaces, we need to set secrets differently
# These will be set in the Spaces settings
if 'OPENAI_API_KEY' not in os.environ and hasattr(st, 'secrets'):
    try:
        os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
        os.environ['QDRANT_URL'] = st.secrets['QDRANT_URL'] 
        os.environ['QDRANT_API_KEY'] = st.secrets['QDRANT_API_KEY']
    except KeyError:
        # Secrets not available, will be handled by the main app
        pass

# Import and run the main app
from app import main

if __name__ == "__main__":
    main()
