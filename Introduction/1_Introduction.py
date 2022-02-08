from flask import Flask, redirect, url_for

app = Flask(__name__)


# The main reasoning behind Flask is to define a function
# for each page and a route strarting from the filesystem
# to define pages.

# homepage: specify the route and the page.
# The root must be defined.
# L'API predefinita apre sempre la connessione rispetto alla root.
@app.route("/")
def home():
    return "Hello! This is the main page :)"


# you should define the name in the dns.
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    # redirect to the specified page -> the argv is the name of the function.
    # it could be possible to specify even the argv of the function.
    return redirect(url_for("user", name="Admin!"))


@app.route("/my_personal")
def my_personal_page():
    return "My name is Lucy."


if __name__ == "__main__":
    app.run(debug=True)
