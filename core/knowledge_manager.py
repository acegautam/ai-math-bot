from agno.knowledge.pdf import PDFKnowledgeBase
import streamlit as st
import os
import json
from pathlib import Path
from typing import Dict, List, Optional
from config.settings import UPLOAD_CONFIG

class KnowledgeManager:
    """Manages PDF knowledge bases and metadata."""
    
    def __init__(self, agent_manager):
        self.agent_manager = agent_manager
        self.metadata_file = "docs/pdf_metadata.json"
        self.knowledge_bases = {}
        
    def load_metadata(self) -> Dict:
        """Load PDF metadata from file."""
        if os.path.exists(self.metadata_file):
            try:
                with open(self.metadata_file, 'r') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}
    
    def save_metadata(self, metadata: Dict):
        """Save PDF metadata to file."""
        os.makedirs(os.path.dirname(self.metadata_file), exist_ok=True)
        with open(self.metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
    
    def add_pdf(self, uploaded_file, pdf_name: str) -> bool:
        """Add a PDF to the knowledge base."""
        try:
            # Ensure docs directory exists
            os.makedirs(UPLOAD_CONFIG["upload_dir"], exist_ok=True)
            
            # Save uploaded file
            file_path = os.path.join(UPLOAD_CONFIG["upload_dir"], uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Initialize vector DB and embedder
            vector_db = self.agent_manager.initialize_vector_db()
            embedder = self.agent_manager.initialize_embedder()
            
            # Create knowledge base
            kb = PDFKnowledgeBase(
                path=file_path,
                vector_db=vector_db,
                embedder=embedder,
                metadata={"source": pdf_name, "filename": uploaded_file.name}
            )
            
            # Load the knowledge base
            kb.load(recreate=False)
            
            # Store in our local registry
            self.knowledge_bases[pdf_name] = {
                "knowledge_base": kb,
                "file_path": file_path,
                "filename": uploaded_file.name
            }
            
            # Update metadata
            metadata = self.load_metadata()
            metadata[pdf_name] = {
                "filename": uploaded_file.name,
                "file_path": file_path,
                "size": uploaded_file.size
            }
            self.save_metadata(metadata)
            
            # Reinitialize agent with the knowledge base
            self.agent_manager.initialize_agent(kb)
            
            return True
            
        except Exception as e:
            st.error(f"Error adding PDF: {str(e)}")
            return False
    
    def remove_pdf(self, pdf_name: str) -> bool:
        """Remove a PDF from the knowledge base."""
        try:
            metadata = self.load_metadata()
            if pdf_name in metadata:
                # Remove file if it exists
                file_path = metadata[pdf_name].get("file_path")
                if file_path and os.path.exists(file_path):
                    os.remove(file_path)
                
                # Remove from metadata
                del metadata[pdf_name]
                self.save_metadata(metadata)
                
                # Remove from local registry
                if pdf_name in self.knowledge_bases:
                    del self.knowledge_bases[pdf_name]
                
                return True
        except Exception as e:
            st.error(f"Error removing PDF: {str(e)}")
        return False
    
    def get_pdf_list(self) -> List[Dict]:
        """Get list of added PDFs with metadata."""
        metadata = self.load_metadata()
        return [
            {
                "name": name,
                "filename": info["filename"],
                "size": info["size"]
            }
            for name, info in metadata.items()
        ]
    
    def load_existing_pdfs(self):
        """Load existing PDFs from metadata on startup."""
        metadata = self.load_metadata()
        vector_db = self.agent_manager.initialize_vector_db()
        embedder = self.agent_manager.initialize_embedder()
        
        latest_kb = None
        
        for pdf_name, info in metadata.items():
            file_path = info["file_path"]
            if os.path.exists(file_path):
                try:
                    kb = PDFKnowledgeBase(
                        path=file_path,
                        vector_db=vector_db,
                        embedder=embedder,
                        metadata={"source": pdf_name, "filename": info["filename"]}
                    )
                    # Don't recreate, just connect to existing
                    kb.load(recreate=False)
                    
                    self.knowledge_bases[pdf_name] = {
                        "knowledge_base": kb,
                        "file_path": file_path,
                        "filename": info["filename"]
                    }
                    latest_kb = kb
                    
                except Exception as e:
                    st.warning(f"Could not load {pdf_name}: {str(e)}")
        
        # Initialize agent with the latest knowledge base
        if latest_kb:
            self.agent_manager.initialize_agent(latest_kb)
    
    def has_pdfs(self) -> bool:
        """Check if any PDFs are loaded."""
        return len(self.get_pdf_list()) > 0

@st.cache_resource
def get_knowledge_manager(_agent_manager):
    """Get cached knowledge manager instance."""
    km = KnowledgeManager(_agent_manager)
    km.load_existing_pdfs()
    return km
