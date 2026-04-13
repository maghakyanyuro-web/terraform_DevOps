from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "this web_site is actually fixed and ready for work 🔥🔥💻",
        "status": "running",
        "server": os.environ.get("SERVER_NAME", "server-1")
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/info")
def info():
    return jsonify({
        "app": "Flask DevOps App",
        "version": "1.0.0",
        "environment": os.environ.get("ENV", "production")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
