from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/discography')
def discography():
    return render_template("discography.html")

@app.route('/members')
def members():
    return render_template("members.html")

@app.route('/videos')
def videos():
    return render_template("videos.html")

@app.route('/label')
def label():
    return render_template("label.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
    