from flask import Flask, render_template, request, redirect
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

def get_room_names():
    rooms = []
    for room in mongo.db.collection_names():
        if not room.startswith("system."):
            rooms.append(room)
    return rooms


@app.route("/")
def show_contents_list():
    rooms = get_room_names()
    
    items_by_room = {}
    for room in rooms:
        items_by_room[room] = mongo.db[room].find()
    
    return render_template("contents_list.html", items_by_room=items_by_room)
    

@app.route("/room/<room>")
def show_room_detail(room):
    
    items = mongo.db[room].find()
    
    return render_template("room_detail.html", items=items, room=room)
    

@app.route("/room/<room>/<item_id>")
def show_item_detail(room, item_id):
    
    item = mongo.db[room].find_one({"_id": ObjectId(item_id)})
    
    return render_template("item_detail.html", item=item)


@app.route("/add_room", methods=["GET", "POST"])
def add_room():
    if request.method == "POST":
        room_name = request.form["room_name"]
        mongo.db.create_collection(room_name)
        
        return redirect("/")
    else:
        rooms = get_room_names()
    
        return render_template("add_room.html", rooms=rooms)


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)