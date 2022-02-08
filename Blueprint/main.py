from flask import Flask, render_template
from second import second 

app = Flask(__name__)
# url_prefix: define the extra word to the path of blueprint
# otherwise, the function of blueprint will override the main.py function.
app.register_blueprint(second, url_prefix="admin/")

# Blueprint extend the psth with  and it is 
# useful to avoid the repetition of the same code.

@app.route("/")
def test():
    return "<h1> Test </h1>"

if __name__ == "__main__":
    app.run(debug = True)