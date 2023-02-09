from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def index():
    return f"Hello from my application!\n{os.uname()}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
