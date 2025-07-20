import streamlit as st
from typing import List, Dict
from config.settings import UPLOAD_CONFIG

def render_pdf_uploader(knowledge_manager):
    """Render the PDF upload interface."""
    st.subheader("📚 Add Math Books")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=UPLOAD_CONFIG["allowed_extensions"],
        help=f"Maximum file size: {UPLOAD_CONFIG['max_file_size']}MB"
    )
    
    # PDF name input
    pdf_name = st.text_input(
        "Book Name/Title",
        placeholder="e.g., Algebra Grade 8, Geometry Basics",
        help="Give your PDF a descriptive name for easy reference"
    )
    
    # Upload button
    if st.button("Add Book", type="primary"):
        if uploaded_file is None:
            st.error("Please select a PDF file")
        elif not pdf_name.strip():
            st.error("Please enter a book name")
        elif pdf_name in [pdf["name"] for pdf in knowledge_manager.get_pdf_list()]:
            st.error("A book with this name already exists")
        else:
            with st.spinner("Adding book to knowledge base..."):
                success = knowledge_manager.add_pdf(uploaded_file, pdf_name.strip())
                if success:
                    st.success(f"✅ Successfully added '{pdf_name}'")
                    st.rerun()

def render_pdf_list(knowledge_manager):
    """Render the list of added PDFs."""
    pdf_list = knowledge_manager.get_pdf_list()
    
    if not pdf_list:
        st.info("No books added yet. Upload your first math book to get started!")
        return
    
    st.subheader("📖 Your Math Library")
    
    for idx, pdf_info in enumerate(pdf_list):
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.write(f"**{pdf_info['name']}**")
                st.caption(f"📄 {pdf_info['filename']} • {format_file_size(pdf_info['size'])}")
            
            with col2:
                # Status indicator
                st.success("✓ Active")
            
            with col3:
                # Remove button
                if st.button("🗑️", key=f"remove_{idx}", help="Remove this book"):
                    if st.session_state.get(f"confirm_remove_{idx}", False):
                        success = knowledge_manager.remove_pdf(pdf_info['name'])
                        if success:
                            st.success("Book removed successfully")
                            st.rerun()
                        st.session_state[f"confirm_remove_{idx}"] = False
                    else:
                        st.session_state[f"confirm_remove_{idx}"] = True
                        st.rerun()
                
                # Confirmation dialog
                if st.session_state.get(f"confirm_remove_{idx}", False):
                    if st.button("Confirm", key=f"confirm_{idx}", type="secondary"):
                        success = knowledge_manager.remove_pdf(pdf_info['name'])
                        if success:
                            st.success("Book removed successfully")
                        st.session_state[f"confirm_remove_{idx}"] = False
                        st.rerun()
            
            st.divider()

def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
