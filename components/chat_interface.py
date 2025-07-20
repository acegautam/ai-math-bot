import streamlit as st
from typing import List, Dict
from config.settings import CHAT_CONFIG

def initialize_chat_history():
    """Initialize chat history in session state."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def render_chat_interface(agent_manager, knowledge_manager):
    """Render the main chat interface."""
    
    # Check if PDFs are loaded
    if not knowledge_manager.has_pdfs():
        st.info("👈 Please add some math books in the sidebar to start chatting!")
        st.write("Once you've uploaded your math PDFs, I'll be able to help you with:")
        st.write("• 📊 Explaining mathematical concepts")
        st.write("• 🔍 Finding specific topics in your books") 
        st.write("• ❓ Answering questions about math problems")
        st.write("• 📖 Providing step-by-step solutions")
        return
    
    st.subheader("🤖 Ask MathBot")
    st.write("Ask me anything about the math books you've uploaded!")
    
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            render_message(message["role"], message["content"])
    
    # Chat input
    with st.container():
        user_input = st.chat_input("Type your math question here...")
        
        if user_input:
            # Add user message to history
            add_message("user", user_input)
            
            # Show user message immediately
            with chat_container:
                render_message("user", user_input)
            
            # Get AI response
            with st.spinner("🤔 Let me check your books..."):
                try:
                    response = agent_manager.get_response(user_input)
                    add_message("assistant", response)
                    
                    # Show assistant response
                    with chat_container:
                        render_message("assistant", response)
                        
                except Exception as e:
                    error_msg = f"Sorry, I encountered an error: {str(e)}"
                    add_message("assistant", error_msg)
                    with chat_container:
                        render_message("assistant", error_msg)
    
    # Clear chat button
    if st.session_state.chat_history:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🗑️ Clear Chat", type="secondary"):
                st.session_state.chat_history = []
                st.rerun()

def render_message(role: str, content: str):
    """Render a single chat message."""
    if role == "user":
        with st.chat_message("user", avatar="🧑‍🎓"):
            st.write(content)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(content)

def add_message(role: str, content: str):
    """Add a message to chat history."""
    st.session_state.chat_history.append({
        "role": role,
        "content": content
    })
    
    # Limit chat history length
    if len(st.session_state.chat_history) > CHAT_CONFIG["max_messages"]:
        st.session_state.chat_history = st.session_state.chat_history[-CHAT_CONFIG["max_messages"]:]

def render_sample_questions():
    """Render sample questions for users to try."""
    st.subheader("💡 Try asking me:")
    
    sample_questions = [
        "What are polynomial equations?",
        "Explain the quadratic formula step by step",
        "What is the Pythagorean theorem?",
        "How do I solve linear equations?",
        "What's the difference between mean and median?",
        "Explain the concept of limits in calculus"
    ]
    
    for i in range(0, len(sample_questions), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(sample_questions[i], key=f"sample_{i}"):
                st.session_state.pending_question = sample_questions[i]
                st.rerun()
        
        if i + 1 < len(sample_questions):
            with col2:
                if st.button(sample_questions[i + 1], key=f"sample_{i+1}"):
                    st.session_state.pending_question = sample_questions[i + 1]
                    st.rerun()

def handle_pending_question(agent_manager):
    """Handle a pending question from sample questions."""
    if "pending_question" in st.session_state:
        question = st.session_state.pending_question
        del st.session_state.pending_question
        
        # Add to chat history and get response
        add_message("user", question)
        
        with st.spinner("🤔 Let me check your books..."):
            try:
                response = agent_manager.get_response(question)
                add_message("assistant", response)
            except Exception as e:
                add_message("assistant", f"Sorry, I encountered an error: {str(e)}")
        
        st.rerun()
