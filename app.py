import os

from flask import Flask, render_template

from profile_data import PROFILE

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", p=PROFILE)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
