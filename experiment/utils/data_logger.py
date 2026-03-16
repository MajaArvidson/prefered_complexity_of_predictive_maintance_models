import os
import json

def save_response(response, filename="data/responses.json"):
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(response)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)