from datetime import timedelta

from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

# Message flashing helps to understand better what is going on
# between two pages when an action occur.


@app.route("/")
def home():
    return render_template("3_index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        # data given by the user.
        user = request.form["nm"]
        # create session and store data.
        session["user"] = user
        flash("Login succesfull!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already login!")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("Not log in.")
        # If the session doesn't exist as well.
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out, {user}!", "info")
    session.pop("user", None)
    # message and category.
    flash("You have logout.", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
