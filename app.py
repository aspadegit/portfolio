from flask import Flask, render_template, url_for
from markupsafe import Markup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/school')
def school():
    return render_template("school_projects.html")

if __name__ == "__main__":
    app.run(debug=True)