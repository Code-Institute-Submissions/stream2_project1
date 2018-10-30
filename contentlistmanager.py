from flask import Flask, render_template
import os
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/")
def show_contents_list():
    return render_template("contents_list.html")

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)