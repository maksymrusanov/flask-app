from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
