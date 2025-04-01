from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure Google API Key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)


# Use a supported model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_input = data.get("message", "")
        personality = data.get("personality", "a helpful AI assistant")

        if not user_input:
            return jsonify({"error": "Message is required"}), 400

        # Create prompt with user's custom personality
        full_prompt = f"Act as {personality}. Respond accordingly.\n\nUser: {user_input}"

        # Generate response
        response = model.generate_content(full_prompt)

        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)