import os

from flask import Flask, jsonify

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def hello_world():
    recipient = os.getenv("RECIPIENT", "unknown")

    return jsonify({"message": "Hello", "recipient": recipient, "result": "ok"})

if __name__ == "__main__":
    app.run()
