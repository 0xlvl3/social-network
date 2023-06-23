from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the social network"


@app.route("/test")
def test():
    return render_template("test.html", title="Social network", heading="Test heading")


if __name__ == "__main__":
    app.run(debug=True)
