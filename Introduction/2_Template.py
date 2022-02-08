from flask import Flask, render_template

app = Flask(__name__)


# Put the template folder in the same folder of these .py scripts.

# Render a html page.
@app.route("/<name>")
def home(name):
    # content is a value passed to the html page.
    return render_template(
        "1_index.html", content=name, r=2, content_2=["anna", "giulia", "francesca"]
    )


if __name__ == "__main__":
    app.run(debug=True)
