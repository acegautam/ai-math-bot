# 📚 MathBot - AI Math Tutor

A powerful Streamlit application that transforms your PDF math books into an intelligent AI tutor. Upload your math textbooks and get personalized, contextual help powered by cutting-edge AI technology.

## 🚀 Features

- **📖 PDF Upload & Management**: Easy drag-and-drop PDF upload with custom naming
- **🤖 Intelligent Tutoring**: AI-powered explanations using your specific math books
- **🔍 Smart Search**: Vector-based search across all your uploaded materials
- **💬 Interactive Chat**: Natural language conversation with source citations
- **🎨 Dark Theme UI**: Modern, elegant interface optimized for learning
- **⚡ Fast Responses**: Powered by OpenAI GPT-4 and Qdrant vector database

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: OpenAI GPT-4
- **Vector Database**: Qdrant
- **Embeddings**: SentenceTransformers
- **AI Framework**: Agno
- **Language**: Python 3.8+

## 📁 Project Structure

```
mathbot/
├── app.py                    # Main Streamlit application
├── config/
│   └── settings.py          # Configuration settings
├── components/
│   ├── pdf_manager.py       # PDF upload and management UI
│   ├── chat_interface.py    # Chat interface components
│   └── sidebar.py           # Sidebar navigation
├── core/
│   ├── agent_manager.py     # AI agent management
│   └── knowledge_manager.py # PDF knowledge base management
├── utils/
│   └── helpers.py          # Utility functions
├── docs/                   # PDF storage directory
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Qdrant Cloud account (or local Qdrant instance)
- OpenAI API key

### 1. Clone the Repository
```bash
git clone <repository-url>
cd mathbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env` with your actual API keys:
```env
QDRANT_URL=https://your-qdrant-cluster.qdrant.io
QDRANT_API_KEY=your-qdrant-api-key
OPENAI_API_KEY=sk-your-openai-api-key
```

### 4. Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🎯 Usage

### Getting Started
1. **Upload PDFs**: Use the sidebar to upload your math textbooks
2. **Name Your Books**: Give each PDF a descriptive name for easy reference
3. **Start Chatting**: Ask questions about mathematical concepts
4. **Get Smart Answers**: Receive AI-powered explanations with source citations

### Example Questions
- "What are polynomial equations?"
- "Explain the quadratic formula step by step"
- "How do I solve systems of linear equations?"
- "What's the difference between mean and median?"

## 🔐 API Keys Setup

### Qdrant Cloud
1. Sign up at [Qdrant Cloud](https://cloud.qdrant.io/)
2. Create a new cluster
3. Get your cluster URL and API key

### OpenAI
1. Sign up at [OpenAI](https://platform.openai.com/)
2. Create an API key in your dashboard
3. Add credits to your account

## 🚀 Deployment

### Hugging Face Spaces
1. Create a new Space on [Hugging Face](https://huggingface.co/spaces)
2. Upload your code
3. Add your environment variables in the Space settings
4. Deploy!

### Local Development
```bash
# Run with hot reload
streamlit run app.py --server.runOnSave=true

# Run on specific port
streamlit run app.py --server.port=8080
```

## 🐛 Troubleshooting

### Common Issues

**"Missing environment variables"**
- Make sure your `.env` file contains all required variables
- Check that variable names match exactly

**"Error adding PDF"**
- Ensure PDF is not password-protected
- Check file size (max 50MB by default)
- Verify Qdrant connection

**"Agent not initialized"**
- Make sure at least one PDF has been successfully uploaded
- Check OpenAI API key validity

### Debug Mode
Run with debug logging:
```bash
streamlit run app.py --logger.level=debug
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Agno](https://github.com/agno-ai/agno) - AI agent framework
- [Qdrant](https://qdrant.tech/) - Vector database
- [OpenAI](https://openai.com/) - GPT-4 model
- [Streamlit](https://streamlit.io/) - Web app framework

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Search existing issues
3. Create a new issue with detailed information

---

Built with ❤️ using Agno, Qdrant & OpenAI
