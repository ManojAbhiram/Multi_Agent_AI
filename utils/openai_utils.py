import os
import requests

AIML_API_KEY = os.getenv("AIML_API_KEY")

def detect_intent(prompt, model="gpt-4o-mini"):
    url = "https://api.aimlapi.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer 417c93a52af34fe985efe1c9bfbb5a06",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")
