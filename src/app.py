from flask import flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from my application!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)