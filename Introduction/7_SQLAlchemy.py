
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICAIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    # each model has a id as the key which must ne an integer and unique.
    _id = db.Column("id", db.Integer, primary_key=True) 
    name = db.Column(db.String(100))
    email  = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email        

@app.route("/")
def home():
    return render_template("3_index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name = user).first() 
        if found_user:
            session["email"] = found_user.email 
        else:
            # create a new user.
            usr = users(user, "")
            # add it to the db.
            db.session.add(usr)
            # every time there is a modification.
            db.session.commit()

        flash("Login succesfull!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already login!")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user", methods={"POST", "GET"})
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            # save the email.
            found_user = users.query.filter_by(name = user).first() 
            found_user.email = email
            db.session.commit()
            flash("Email was saved.")
        else:
            if "email" is session:
                email = session["email"]
            
        return render_template("user.html", email=email)
    else:
        flash("Not log in.")
        # If the session doesn't exist as well.
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash(f"You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)