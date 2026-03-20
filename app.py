from flask import Flask, render_template, request, jsonify
from utils.linkedin import fetch_linkedin_data, format_profile # using fetch_linkedin_data(), format_profile() from linkeding.py 
from utils.rag import create_vectorstore # using create_vectorstore() from rag.py
from utils.groq import ask_groq # using ask_groq() groq.py 
from utils.twitter import fetch_twitter_data # using fetch_twitter_data() from twitter.py
app = Flask(__name__)

db_store = {}
chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/load_profile", methods=["POST"])
def load_profile():
    data = request.json
    linkedin_url = data.get("linkedin_url")
    profile_text = data.get("profile_text")

    if not linkedin_url and not profile_text:
        return jsonify({"error": "Provide LinkedIn URL or profile text"}), 400

    try:
        profile = fetch_linkedin_data(linkedin_url)
        linkedin_text = format_profile(profile)
        twitter_handle = data.get("twitter")
        twitter_text = ""
        if twitter_handle: # Feature to fetch twitter data using twitter handle (if given)
            twitter_text = fetch_twitter_data(twitter_handle) # using fetch_twitter_data() from twitter.py
        text = linkedin_text + "\n\nTWITTER DATA:\n" + twitter_text
        db = create_vectorstore(text)
        db_store["db"] = db

        return jsonify({"message": "Profile loaded successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data.get("query")

    if "db" not in db_store:
        return jsonify({"error": "Load profile first"}), 400

    docs = db_store["db"].similarity_search(query, k=8)
    answer = ask_groq(query, docs, chat_history)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)