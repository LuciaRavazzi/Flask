from datetime import timedelta

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
# it is used to encrypt sessions.
app.secret_key = "hello"

# Session data stored information in a temporary directory. Each time the browser get closed, sessions are lost.
# However, it's possible to store it for a longer time.
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def home():
    return "Home page"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        # data given by the user.
        user = request.form["nm"]
        # create session and store data.
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        # If the session doesn't exist as well.
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove data. None -> message.
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
