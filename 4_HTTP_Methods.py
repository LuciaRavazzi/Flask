from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# HTTP methods:
#       - GET: insicure way of getting information.
#       - POST: sicure way of getting information (encripted).


@app.route("/")
def home():
    return "Home page"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # data given by the user.
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
