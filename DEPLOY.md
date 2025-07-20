# 🚀 Deployment Guide

## Hugging Face Spaces Deployment

### Prerequisites
- Hugging Face account
- OpenAI API key
- Qdrant Cloud account with cluster

### Steps

1. **Create a new Space**
   - Go to [Hugging Face Spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose "Streamlit" as the SDK
   - Name your space (e.g., "mathbot-ai-tutor")

2. **Upload files**
   - Upload all Python files and the requirements.txt
   - Use `app_hf.py` as the main entry point (rename to `app.py` in the Space)

3. **Set environment variables**
   - In your Space settings, go to "Variables and secrets"
   - Add the following secrets:
     ```
     OPENAI_API_KEY=your_openai_api_key
     QDRANT_URL=your_qdrant_cluster_url
     QDRANT_API_KEY=your_qdrant_api_key
     ```

4. **Deploy**
   - Your Space will automatically build and deploy
   - Check the logs for any issues

### File Structure for HF Spaces
```
your-space/
├── app.py              # Rename app_hf.py to this
├── requirements.txt    # Dependencies
├── config/
├── components/
├── core/
├── utils/
└── README.md
```

## Local Development

### Quick Start
```bash
# Set up environment
cp .env.example .env
# Edit .env with your API keys

# Install dependencies  
pip install -r requirements.txt

# Run the app
python run.py
# OR
streamlit run app.py
```

### Using Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
```

## Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key
- `QDRANT_URL`: Your Qdrant cluster URL (e.g., https://xyz.qdrant.io)  
- `QDRANT_API_KEY`: Your Qdrant API key

### Customization
You can customize the app by modifying:
- `config/settings.py`: Configuration settings
- `utils/helpers.py`: UI styling and helper functions
- `components/`: Individual UI components

## Troubleshooting

### Common Issues

1. **"Missing environment variables"**
   - Ensure all API keys are set correctly
   - Check variable names match exactly

2. **"Error adding PDF"**
   - Verify PDF is not password-protected
   - Check file size limits
   - Ensure Qdrant connection is working

3. **Slow loading**
   - Large PDFs take time to process
   - Consider splitting very large documents

### Support
- Check the main README.md for detailed troubleshooting
- Review application logs for specific error messages
