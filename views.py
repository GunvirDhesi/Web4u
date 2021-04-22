from flask import Flask, render_template, url_for

app = Flask(__name__)
port = 2000


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/aboutus")
def about():
    return render_template("about.html")


@app.route("/error")
def error():
    return "<html> <h1>ERROR</h1> </html>"

if __name__ == "__main__":
    app.run(debug=True,port=port);
