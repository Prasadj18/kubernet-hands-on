
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/about", methods=["GET"])
def about():
    return jsonify({
        "name": "Simple REST API",
        "version": "1.0",
        "description": "A REST API built with Flask."
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
