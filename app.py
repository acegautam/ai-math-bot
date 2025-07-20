"""
MathBot - AI Math Tutor Streamlit App
=====================================

A modular Streamlit application that allows users to upload PDF math books
and interact with an AI tutor powered by Agno, Qdrant, and OpenAI.
"""

import streamlit as st
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add project root to path for imports
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from utils.helpers import (
    setup_page_config, 
    setup_custom_css, 
    check_environment_variables,
    render_header,
    create_docs_directory,
    display_status_indicator
)
from components.sidebar import render_sidebar
from components.chat_interface import (
    initialize_chat_history, 
    render_chat_interface, 
    render_sample_questions,
    handle_pending_question
)
from core.agent_manager import get_agent_manager
from core.knowledge_manager import get_knowledge_manager

def main():
    """Main application entry point."""
    
    # Setup page configuration and styling
    setup_page_config()
    setup_custom_css()
    
    # Check environment variables
    if not check_environment_variables():
        st.stop()
    
    # Ensure docs directory exists
    create_docs_directory()
    
    # Initialize chat history
    initialize_chat_history()
    
    # Get managers
    agent_manager = get_agent_manager()
    knowledge_manager = get_knowledge_manager(agent_manager)
    
    # Handle any pending questions
    handle_pending_question(agent_manager)
    
    # Render sidebar
    render_sidebar(knowledge_manager)
    
    # Main content area
    render_header()
    
    # Status indicator
    has_pdfs = knowledge_manager.has_pdfs()
    display_status_indicator(has_pdfs)
    
    # Main chat interface
    if has_pdfs:
        render_chat_interface(agent_manager, knowledge_manager)
    else:
        # Show sample questions when no PDFs are loaded
        st.write("## Welcome to MathBot! 👋")
        st.write("""
        I'm your AI math tutor, ready to help you understand mathematical concepts 
        from your own textbooks and study materials.
        
        **To get started:**
        1. Upload your math PDF books using the sidebar ←
        2. Give each book a descriptive name
        3. Start asking me questions!
        
        Once you've uploaded your books, here are some example questions you can ask:
        """)
        render_sample_questions()

if __name__ == "__main__":
    main()
