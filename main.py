from flask import Flask, request, jsonify, render_template_string
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyC7JD7HyqgGD9gjDTeCpuUuVPGI_FJuOOI")

# Initialize Flask
app = Flask(__name__)

# Load your index.html file content
with open("index.html", "r", encoding="utf-8") as f:
    html_template = f.read()

# Route to serve the chatbot page
@app.route("/")
def home():
    return render_template_string(html_template)

# Route to process chat messages
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Empty input"}), 400

    model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")
    response = model.generate_content(user_input)
    return jsonify({"response": response.text})


if __name__ == "__main__":
    app.run(debug=True)

     
