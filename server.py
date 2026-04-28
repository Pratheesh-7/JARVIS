# from flask import Flask, jsonify, send_file
# from flask_cors import CORS
# from livekit.api import AccessToken, VideoGrants
# from dotenv import load_dotenv
# import os

# load_dotenv()

# app = Flask(__name__)
# CORS(app)


# @app.route("/token")
# def get_token():
#     token = AccessToken(
#         api_key=os.getenv('LIVEKIT_API_KEY'),
#         api_secret=os.getenv('LIVEKIT_API_SECRET')
#     )
#     token.identity = "user"
#     token.name = "User"
#     token.add_grants(VideoGrants(room_join=True, room="jarvis-room"))
    
#     return jsonify({
#         "token": token.to_jwt(),
#         "url": os.getenv('LIVEKIT_URL')
#     })

# @app.route("/")
# def index():
#     return send_file("jarvis.html")

# if __name__ == "__main__":
#     print("\n✅ Jarvis server running → http://localhost:3000\n")
#     app.run(port=3000, debug=True)  # debug=True so you see errors


# from flask import Flask, jsonify, render_template
# from flask_cors import CORS
# from livekit.api import AccessToken, VideoGrants
# from dotenv import load_dotenv
# import os

# load_dotenv()

# app = Flask(__name__)
# CORS(app)


# @app.route("/")
# def index():
#     return render_template("jarvis.html")

# @app.route("/token")
# def get_token():
#     try:
#         api_key = os.getenv("LIVEKIT_API_KEY")
#         api_secret = os.getenv("LIVEKIT_API_SECRET")
#         url = os.getenv("LIVEKIT_URL")

#         if not api_key or not api_secret or not url:
#             return jsonify({"error": "Missing env vars"}), 500

#         token = AccessToken(api_key, api_secret)

#         token.identity = "user"
#         token.name = "User"

#         # ✅ safer modern method
#         token.add_grants(VideoGrants(
#             room_join=True,
#             room="jarvis-room"
#         ))

#         return jsonify({
#             "token": token.to_jwt(),
#             "url": url
#         })

#     except Exception as e:
#         print("TOKEN ERROR:", e)
#         return jsonify({"error": str(e)}), 500

#     except Exception as e:
#         print("TOKEN ERROR:", e)
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     print("\n🚀 Jarvis server running → http://localhost:3000\n")
#     app.run(port=3000, debug=True)



# from flask import Flask, jsonify, render_template
# from flask_cors import CORS
# from livekit.api import AccessToken, VideoGrants
# from dotenv import load_dotenv
# import os

# load_dotenv()

# app = Flask(__name__)
# CORS(app)


# @app.route("/")
# def index():
#     return render_template("jarvis.html")

# @app.route("/token")
# def get_token():
#     try:
#         api_key = os.getenv("LIVEKIT_API_KEY")
#         api_secret = os.getenv("LIVEKIT_API_SECRET")
#         url = os.getenv("LIVEKIT_URL")

#         print("DEBUG VALUES:", api_key, api_secret, url)

#         if not api_key or not api_secret or not url:
#             return jsonify({"error": "Missing env vars"}), 500

#         token = AccessToken(api_key, api_secret)

#         token.identity = "user"
#         token.name = "User"

#         token.add_grants(VideoGrants(
#             room_join=True,
#             room="jarvis-room"
#         ))

#         return jsonify({
#             "token": token.to_jwt(),
#             "url": url
#         })

#     except Exception as e:
#         print("🔥 TOKEN ERROR FULL TRACE:", repr(e))
#         return jsonify({"error": str(e)}), 500


# import os
# from flask import Flask, jsonify
# import google.generativeai as genai

# print("🔥 SERVER FILE LOADED")

# app = Flask(__name__)

# # ── AI SETUP (MUST BE BEFORE app.run) ──
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel("gemini-1.5-flash")

# def ask_ai(prompt):
#     response = model.generate_content(prompt)
#     return response.text


# # ── ROUTES ──
# @app.route("/")
# def home():
#     return "Jarvis is running"


# @app.route("/token")
# def get_token():
#     return jsonify({"status": "LiveKit route reached"})


# @app.route("/ai/<message>")
# def ai(message):
#     try:
#         reply = ask_ai(message)
#         return jsonify({"response": reply})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# # ── START SERVER ──
# if __name__ == "__main__":
#     print("SERVER STARTING...")
#     app.run(port=3000, debug=True)



# from flask import Flask, jsonify, render_template
# from flask_cors import CORS
# from livekit.api import AccessToken, VideoGrants
# from dotenv import load_dotenv
# import os

# load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# app = Flask(__name__)
# CORS(app)

# @app.route("/")
# def home():
#     return render_template("jarvis.html")   

# @app.route("/token")
# def token():
#     api_key = os.getenv("LIVEKIT_API_KEY")
#     api_secret = os.getenv("LIVEKIT_API_SECRET")
#     url = os.getenv("LIVEKIT_URL")

#     if not api_key or not api_secret or not url:
#         return jsonify({"error": "Missing env vars"}), 500

#     at = AccessToken(api_key, api_secret)
#     at.identity = "user"

#     at.add_grants(VideoGrants(
#         room_join=True,
#         room="jarvis-room"
#     ))

#     return jsonify({
#         "token": at.to_jwt(),
#         "url": url
#     })

# if __name__ == "__main__":
#     print("🔥 Server running at http://localhost:3000")
#     app.run(port=3000, debug=True)



from flask import Flask, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os

from livekit.api import AccessToken, VideoGrants

load_dotenv()

app = Flask(__name__, template_folder="templates")

# allow frontend calls
CORS(app, origins=["http://127.0.0.1:3000", "http://localhost:3000"])


# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("jarvis.html")


# ---------------- LIVEKIT TOKEN ----------------
@app.route("/token")
def token():
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")
    url = os.getenv("LIVEKIT_URL")

    if not api_key or not api_secret or not url:
        return jsonify({"error": "Missing env vars"}), 500

    try:
        at = AccessToken(api_key, api_secret)

        # ✅ correct way (new SDK safe method)
        at.identity = "user"
        at.name = "user"

        at.with_grants(VideoGrants(
            room_join=True,
            room="jarvis-room"
        ))

        return jsonify({
            "token": at.to_jwt(),
            "url": url
        })

    except Exception as e:
        print("TOKEN ERROR:", e)
        return jsonify({"error": str(e)}), 500

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    print("🔥 Jarvis running → http://localhost:3000")
    app.run(port=3000, debug=True)

