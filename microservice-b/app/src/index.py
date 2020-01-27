from flask import Flask, request

app = Flask(__name__)

@app.route("/reverse", methods=["POST"])
def reverse():
    message = request.json["message"]
    return message[::-1]

@app.route("/liveness")
def liveness():
    return "Service is live!"

@app.route("/readiness")
def readiness():
    return "Service is ready!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
