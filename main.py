from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text)


@app.route("/")
def main_page(methods=["GET"]):
    if request.method == "GET":
        notes = Note.query.all()

    return render_template("main.html", notes=notes)


@app.route("/create", methods=["GET", "POST"])
def create_new_task():
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]
        new_note = Note(title=title, text=text)
        db.session.add(new_note)
        db.session.commit()
        return render_template("create_task.html", message="Note saved successfully!")

    return render_template("create_task.html")


if __name__ == "__main__":
    app.run(debug=True)
