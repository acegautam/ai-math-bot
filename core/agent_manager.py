from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.vectordb.qdrant import Qdrant
import streamlit as st
from config.settings import QDRANT_CONFIG, OPENAI_CONFIG, EMBEDDER_CONFIG, CHAT_CONFIG
from typing import Optional

class AgentManager:
    """Manages the Agno Agent instance and its dependencies."""
    
    def __init__(self):
        self.vector_db: Optional[Qdrant] = None
        self.embedder: Optional[SentenceTransformerEmbedder] = None
        self.agent: Optional[Agent] = None
        
    def initialize_vector_db(self) -> Qdrant:
        """Initialize Qdrant vector database."""
        if self.vector_db is None:
            self.vector_db = Qdrant(
                collection=QDRANT_CONFIG["collection"],
                url=QDRANT_CONFIG["url"],
                api_key=QDRANT_CONFIG["api_key"],
            )
        return self.vector_db
    
    def initialize_embedder(self) -> SentenceTransformerEmbedder:
        """Initialize the sentence transformer embedder."""
        if self.embedder is None:
            self.embedder = SentenceTransformerEmbedder(
                dimensions=EMBEDDER_CONFIG["dimensions"]
            )
        return self.embedder
    
    def initialize_agent(self, knowledge_base=None) -> Agent:
        """Initialize the Agno agent with OpenAI model."""
        if self.agent is None or knowledge_base is not None:
            model = OpenAIChat(
                id=OPENAI_CONFIG["model_id"],
                api_key=OPENAI_CONFIG["api_key"]
            )
            
            self.agent = Agent(
                model=model,
                knowledge=knowledge_base,
                instructions=CHAT_CONFIG["system_prompt"]
            )
        return self.agent
    
    def get_response(self, query: str) -> str:
        """Get response from the agent."""
        if self.agent is None:
            raise ValueError("Agent not initialized. Please add some PDFs first.")
        
        try:
            # Get the response as a string instead of printing
            response = self.agent.run(query)
            return response.content if hasattr(response, 'content') else str(response)
        except Exception as e:
            return f"Error getting response: {str(e)}"

# Global agent manager instance
@st.cache_resource
def get_agent_manager():
    """Get cached agent manager instance."""
    return AgentManager()
