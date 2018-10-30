from flask import Flask, render_template
import os
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

def get_category_names():
    categories = []
    for category in mongo.db.collection_names():
        if not category.startswith("system."):
            categories.append(category)
    return categories

@app.route("/")
def show_contents_list():
    categories = get_category_names()
    return render_template("contents_list.html", categories=categories)

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)