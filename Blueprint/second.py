from flask import Blueprint, render_template

# Blueprint define a template for each flask project.
second = Blueprint("main", __name__, static_folder="static", template_folder="templates")


@second.route("/home")
@second.route("/")
def home():
    return render_template("home.html")

@second.route("/test")
def test():
    return "<h1> Test </h1>"