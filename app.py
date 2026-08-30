from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Home page - ATS Checker
@app.route("/")
def home():
    return render_template("index.html")


# Chatbot page
@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")


# Simple ATS Checker
@app.route("/check-ats", methods=["POST"])
def check_ats():

    resume = request.files.get("resume")
    job_description = request.form.get("job_description", "")

    if not resume:
        return jsonify({"error": "Please upload a resume"}), 400

    if not job_description:
        return jsonify({"error": "Please enter a job description"}), 400

    # Basic keyword analysis
    job_words = job_description.lower().split()

    # Remove duplicate words
    keywords = list(set(job_words))

    # For now, demo scoring
    score = min(len(keywords) * 2, 100)

    return jsonify({
        "score": score,
        "message": "Resume uploaded successfully!",
        "keywords_found": keywords[:10]
    })


# Simple AI Chatbot
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data.get("message", "").lower()

    if "hello" in message or "hi" in message:
        response = "Hello! I am your AI Career Assistant. How can I help you?"

    elif "resume" in message:
        response = "I can help you improve your resume and check its ATS compatibility."

    elif "interview" in message:
        response = "I can help you prepare for interviews. Ask me any interview question!"

    elif "job" in message:
        response = "I can help you with job searching, resumes, and career preparation."

    elif "bye" in message:
        response = "Goodbye! Best of luck with your career!"

    else:
        response = "I'm still learning. Try asking me about resumes, jobs, or interviews."

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)