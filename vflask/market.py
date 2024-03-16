from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello_world</h1>"

#Dynamic routes demonstrated here.
@app.route("/about/<username>")
def about_page(username):
    return f"<h1>This is the about Page of {username}.</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)