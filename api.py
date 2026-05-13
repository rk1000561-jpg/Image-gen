from flask import Flask, request, jsonify
import urllib.parse

app = Flask(__name__)

# Author info
AUTHOR = "r3xtron"
API_KEY = "ansh"

BASE_URL = "https://image.pollinations.ai/prompt/"

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "author": AUTHOR,
        "message": "R3XTRON Image Gen API",
        "usage": "/api/seedream?key=ansh&prompt=dog"
    })

@app.route("/api/seedream", methods=["GET"])
def generate_image():

    key = request.args.get("key")
    prompt = request.args.get("prompt")

    if key != API_KEY:
        return jsonify({
            "success": False,
            "error": "Invalid API key",
            "author": AUTHOR
        }), 403

    if not prompt:
        return jsonify({
            "success": False,
            "error": "Prompt is required",
            "author": AUTHOR
        }), 400

    encoded = urllib.parse.quote(prompt)
    image_url = BASE_URL + encoded

    return jsonify({
        "success": True,
        "author": AUTHOR,
        "prompt": prompt,
        "image": image_url
    })

# Vercel needs this
def handler(environ, start_response):
    return app(environ, start_response)
