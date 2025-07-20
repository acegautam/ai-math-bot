import streamlit as st
import os
from pathlib import Path

def setup_page_config():
    """Configure the Streamlit page with theme and layout."""
    from config.settings import STREAMLIT_CONFIG
    
    st.set_page_config(
        page_title=STREAMLIT_CONFIG["page_title"],
        page_icon=STREAMLIT_CONFIG["page_icon"],
        layout=STREAMLIT_CONFIG["layout"],
        initial_sidebar_state=STREAMLIT_CONFIG["initial_sidebar_state"]
    )

def setup_custom_css():
    """Apply custom CSS for dark theme and styling."""
    st.markdown("""
    <style>
    /* Main theme colors */
    .main {
        background-color: #0E1117;
    }
    
    /* Chat messages styling */
    .stChatMessage {
        background-color: #1E1E1E;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #262730;
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 8px;
        border: none;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 500;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #5a67d8 0%, #6b46c1 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    
    /* File uploader styling */
    .stFileUploader > div {
        background-color: #1E1E1E;
        border: 2px dashed #667eea;
        border-radius: 10px;
        padding: 20px;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background-color: #1E1E1E;
        border: 1px solid #667eea;
        border-radius: 8px;
        color: white;
    }
    
    /* Success/Error messages */
    .stSuccess {
        background-color: rgba(34, 197, 94, 0.1);
        border-left: 4px solid #22c55e;
    }
    
    .stError {
        background-color: rgba(239, 68, 68, 0.1);
        border-left: 4px solid #ef4444;
    }
    
    .stInfo {
        background-color: rgba(59, 130, 246, 0.1);
        border-left: 4px solid #3b82f6;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #1E1E1E;
        border-radius: 8px;
    }
    
    /* Title and header styling */
    h1, h2, h3 {
        color: #F0F2F6;
    }
    
    /* Custom gradient text for title */
    .gradient-text {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Card-like containers */
    .card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #333;
        margin: 10px 0;
    }
    
    /* Loading spinner customization */
    .stSpinner > div {
        border-top-color: #667eea;
    }
    </style>
    """, unsafe_allow_html=True)

def check_environment_variables():
    """Check if required environment variables are set."""
    required_vars = ['QDRANT_URL', 'QDRANT_API_KEY', 'OPENAI_API_KEY']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        st.error(f"❌ Missing environment variables: {', '.join(missing_vars)}")
        st.write("Please set the following environment variables:")
        for var in missing_vars:
            st.code(f"export {var}=your_value_here")
        return False
    
    return True

def render_header():
    """Render the main header with gradient text."""
    st.markdown("""
    <div class="gradient-text">
        📚 MathBot - AI Math Tutor
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p style='text-align: center; color: #A0AEC0; font-size: 1.2rem; margin-bottom: 2rem;'>
        Upload your math books and get personalized AI tutoring
    </p>
    """, unsafe_allow_html=True)

def create_docs_directory():
    """Ensure the docs directory exists."""
    docs_path = Path("docs")
    docs_path.mkdir(exist_ok=True)
    return docs_path

def display_status_indicator(has_pdfs: bool):
    """Display connection status indicator."""
    if has_pdfs:
        st.success("🟢 MathBot is ready to help!")
    else:
        st.warning("🟡 Add some math books to get started")

def format_markdown_response(response: str) -> str:
    """Format the AI response with better markdown."""
    # Add some basic formatting improvements
    if "```" not in response:
        # If no code blocks, try to format math expressions
        import re
        response = re.sub(r'\*\*(.*?)\*\*', r'**\1**', response)  # Bold
        response = re.sub(r'\*(.*?)\*', r'*\1*', response)  # Italic
    
    return response
