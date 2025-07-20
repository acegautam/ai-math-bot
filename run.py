#!/usr/bin/env python3
"""
Simple script to run the MathBot Streamlit app
"""

import subprocess
import sys
import os

def main():
    """Run the Streamlit app."""
    print("🚀 Starting MathBot - AI Math Tutor...")
    
    # Check if environment variables are set
    if not os.getenv('OPENAI_API_KEY') or not os.getenv('QDRANT_URL'):
        print("⚠️  Warning: Environment variables not set")
        print("Please set OPENAI_API_KEY, QDRANT_URL, and QDRANT_API_KEY")
        print("You can copy .env.example to .env and fill in your values")
    
    try:
        # Run streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port=8501",
            "--server.address=0.0.0.0"
        ], check=True)
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
