from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def home():
    return jsonify({"message": "Hello from app3.py!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)  # Ubah port sesuai app (5001, 5002, dst.)
