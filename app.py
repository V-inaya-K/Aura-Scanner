# from flask import Flask, render_template, request, jsonify
# from utils.linkedin import fetch_linkedin_data, format_profile
# from utils.rag import create_vectorstore
# from utils.groq import ask_groq

# app = Flask(__name__)

# db_store = {}  # temporary in-memory storage

# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/load_profile", methods=["POST"])
# def load_profile():
#     data = request.json
#     url = data.get("linkedin_url")

#     if "linkedin.com" not in url:
#         return jsonify({"error": "Invalid LinkedIn URL"}), 400

#     profile = fetch_linkedin_data(url)

#     if not profile:
#         return jsonify({"error": "Failed to fetch profile"}), 500

#     text = format_profile(profile)
#     db = create_vectorstore(text)

#     db_store["db"] = db

#     return jsonify({"message": "Profile loaded successfully"})


# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.json
#     query = data.get("query")

#     if "db" not in db_store:
#         return jsonify({"error": "Load profile first"}), 400

#     docs = db_store["db"].similarity_search(query, k=3)
#     answer = ask_groq(query, docs)

#     return jsonify({"answer": answer})


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from utils.linkedin import fetch_linkedin_data, format_profile
from utils.rag import create_vectorstore
from utils.groq import ask_groq

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
        if profile_text:
            text = profile_text
        else:
            if "linkedin.com" not in linkedin_url:
                return jsonify({"error": "Invalid LinkedIn URL"}), 400

            profile = fetch_linkedin_data(linkedin_url)
            text = format_profile(profile)

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

    docs = db_store["db"].similarity_search(query, k=3)

    answer = ask_groq(query, docs, chat_history)

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)