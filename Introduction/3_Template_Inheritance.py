from flask import Flask, render_template

app = Flask(__name__)

# Flask is able to provide a front-end website without
# using the complexity of React or Angular.

# Bootstrap https://getbootstrap.com/ offers template
# to avoid the repetition of the same lines of code.


@app.route("/")
def home():
    return render_template("2_index.html", content="Testing")


@app.route("/test")
def test():
    return render_template("3_index.html", content="Testing")


if __name__ == "__main__":
    # detect the chnges and update the website.
    app.run(debug=True)
