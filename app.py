#!/usr/bin/env python3
from flask import Flask, request, jsonify
import random

# Initialize Flask app
app = Flask(__name__)

# Mock endpoint for OpenAI's completion API
@app.route('/v1/completions', methods=['POST'])
def completions():
    data = request.json

    # Validate required fields
    required_fields = ["model", "prompt"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Mocked response
    response = {
        "id": f"mock-{random.randint(1000, 9999)}",
        "object": "text_completion",
        "created": 1234567890,
        "model": data["model"],
        "choices": [
            {
                "text": f"Mocked response for prompt: {data['prompt']}",
                "index": 0,
                "logprobs": None,
                "finish_reason": "length"
            }
        ],
        "usage": {
            "prompt_tokens": len(data["prompt"].split()),
            "completion_tokens": 5,
            "total_tokens": len(data["prompt"].split()) + 5
        }
    }

    return jsonify(response)

# Mock endpoint for OpenAI's chat API
@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    data = request.json

    # Validate required fields
    required_fields = ["model", "messages"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Mocked response
    response = {
        "id": f"mock-{random.randint(1000, 9999)}",
        "object": "chat_completion",
        "created": 1234567890,
        "model": data["model"],
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "Mocked response to your chat input."
                },
                "finish_reason": "stop",
                "index": 0
            }
        ],
        "usage": {
            "prompt_tokens": sum(len(msg['content'].split()) for msg in data["messages"]),
            "completion_tokens": 7,
            "total_tokens": sum(len(msg['content'].split()) for msg in data["messages"]) + 7
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)



