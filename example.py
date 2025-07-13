import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
try:
    load_dotenv()
except Exception as e:
    print(f"Warning: Could not load .env file: {e}")
    print("Make sure you have a .env file with CLAUDE_API_KEY=your_api_key")

def test_claude_api():
    """Test the Claude API key by making a simple request"""
    
    # Get API key from environment variable
    api_key = os.getenv('CLAUDE_API_KEY')
    
    if not api_key:
        print("Error: CLAUDE_API_KEY not found in .env file")
        return
    
    # API endpoint
    url = "https://api.anthropic.com/v1/messages"
    
    # Headers
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    
    # Request data
    data = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Hello, world"}
        ]
    }
    
    try:
        # Make the API request
        response = requests.post(url, headers=headers, json=data)
        
        # Check if request was successful
        if response.status_code == 200:
            result = response.json()
            print("✅ API Key is working!")
            print("Response:", result.get('content', []))
        else:
            print(f"❌ API request failed with status code: {response.status_code}")
            print("Response:", response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error making API request: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_claude_api()