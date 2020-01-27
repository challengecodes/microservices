from random import random

from flask import Flask, request
import requests

REVERSE_SERVICE_API = "http://microservice-b/reverse"

app = Flask(__name__)

@app.route("/api", methods=["POST"])
def api():
    message = request.json["message"]
    reverse = requests.post(REVERSE_SERVICE_API, json={"message": message})
    return {
        "message": reverse.text,
        "rand": random(),
    }

@app.route("/liveness")
def liveness():
    return "Service is live!"

@app.route("/readiness")
def readiness():
    return "Service is ready!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
