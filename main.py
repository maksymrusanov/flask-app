from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemyg


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text)
    status = db.Column(db.Boolean)


@app.route("/")
def main_page(methods=["GET"]):
    if request.method == "GET":
        if not Note.query.all():
            return render_template("main.html")
    notes = Note.query.all()
    return render_template("main.html", notes=notes)


@app.route("/create", methods=["GET", "POST"])
def create_new_task():
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]
        status = False
        new_note = Note(title=title, text=text, status=status)
        db.session.add(new_note)
        db.session.commit()
        return render_template("create_task.html", message="Note saved successfully!")

    return render_template("create_task.html")


@app.route("/delete/<int:note_id>", methods=["POST", "GET"])
def delete_task(note_id):
    note = Note.query.get(note_id)
    if note:
        db.session.delete(note)
        db.session.commit()
    return redirect(url_for("main_page"))


@app.route("/mark_done/<int:note_id>", methods=["POST", "GET"])
def mark_done(note_id):
    note = Note.query.get(note_id)
    if not note:
        return redirect(url_for("main_page"))
    note.status = True
    db.session.commit()
    return redirect(url_for("marked_done"))


@app.route("/marked_done")
def marked_done():
    notes = Note.query.filter_by(status=True).all()
    return render_template("marked_done.html", notes=notes)


@app.route("/not_finished")
def not_finished():
    notes = Note.query.filter_by(status=False).all()
    return render_template("not_finished.html", notes=notes)


if __name__ == "__main__":
    app.run(debug=True)
