import streamlit as st
from components.pdf_manager import render_pdf_uploader, render_pdf_list

def render_sidebar(knowledge_manager):
    """Render the main sidebar with navigation and PDF management."""
    
    with st.sidebar:
        st.title("📚 MathBot")
        st.write("*Your AI Math Tutor*")
        st.divider()
        
        # PDF Management Section
        render_pdf_uploader(knowledge_manager)
        st.divider()
        render_pdf_list(knowledge_manager)
        
        # Footer
        st.divider()
        render_sidebar_footer()

def render_sidebar_footer():
    """Render the sidebar footer with info and stats."""
    
    st.subheader("ℹ️ About")
    
    with st.expander("How it works"):
        st.write("""
        1. **Upload** your math PDF books using the file uploader above
        2. **Name** each book for easy reference  
        3. **Chat** with MathBot about concepts from your books
        4. **Learn** with AI-powered explanations and examples
        
        MathBot uses advanced AI to understand your math books and provide personalized tutoring.
        """)
    
    with st.expander("Features"):
        st.write("""
        • 🔍 **Intelligent Search** - Finds relevant content across all your books
        • 📖 **Source Citations** - References specific books in responses
        • 💡 **Step-by-step** - Breaks down complex problems
        • 🎯 **Contextual** - Understands mathematical relationships
        • 🚀 **Fast Response** - Powered by OpenAI GPT-4
        """)
    
    with st.expander("Tech Stack"):
        st.write("""
        • **Frontend**: Streamlit
        • **AI Model**: OpenAI GPT-4
        • **Vector DB**: Qdrant
        • **Embeddings**: SentenceTransformers
        • **Framework**: Agno AI
        """)
    
    st.caption("Built with ❤️ using Agno, Qdrant & OpenAI")
