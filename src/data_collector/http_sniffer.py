from flask import Flask, request
from src.model.predict import is_malicious

app = Flask(__name__)

@app.route("/api/scan", methods=["POST"])
def scan_request():
    data = request.get_json()
    payload = data.get("payload", "")

    if is_malicious(payload):
        return {"alert": True, "message": "Possible attack detected!"}, 200
    else:
        return {"alert": False, "message": "No threat found."}, 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
