from flask import Flask, render_template, request, redirect, url_for
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.context_processor
def utility_processor():
    def spaces_to_underscores(s):
        return s.replace(" ", "_").lower()
    return {"spaces_to_underscores": spaces_to_underscores}

# Get Room Names Function
def get_room_names():
    rooms = []
    for room in mongo.db.collection_names():
        if not room.startswith("system."):
            rooms.append(room)
    return rooms


# Show Contents List App Route
@app.route("/")
def show_contents_list():
    rooms = get_room_names()
    
    items_by_room = {}
    for room in rooms:
        items_by_room[room] = mongo.db[room].find()
    
    return render_template("contents_list.html", items_by_room=items_by_room)

    
# Show Room Detail App Route
@app.route("/room/<room>")
def show_room_detail(room):
    
    items = mongo.db[room].find()
    
    return render_template("room_detail.html", items=items, room=room)
    

# Show Item Detail App Route
@app.route("/room/<room>/<item_id>")
def show_item_detail(room, item_id):
    
    item = mongo.db[room].find_one({"_id": ObjectId(item_id)})
    
    return render_template("item_detail.html", room=room, item=item)


# Add Room App Route
@app.route("/add_room", methods=["GET", "POST"])
def add_room():
    if request.method == "POST":
        room_name = request.form["room_name"]
        mongo.db.create_collection(room_name)
        
        return redirect("/")
    else:
        rooms = get_room_names()
    
        return render_template("add_room.html", rooms=rooms)
        

# Edit Room App Route
@app.route("/room/<room>/edit_room", methods=["GET", "POST"])
def edit_room(room):
    if request.method == "POST":
        room_name = request.form["room_name"]
        mongo.db[room].rename(room_name)
        
        return redirect(url_for("show_room_detail", room=room_name))
    else:
        rooms = get_room_names()
        
        return render_template("edit_room.html", rooms=rooms, room_room=room)
        

# Add Item App Route
@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        form_values = request.form.to_dict()
        room = form_values["room_name"]
        mongo.db[room].insert_one(form_values)
        
        return redirect("/")
    else:
        rooms = get_room_names()
        
        return render_template ("add_item.html", rooms=rooms)
        

# Edit Item App Route
@app.route("/item/<room>/<item_id>/edit_item", methods=["GET", "POST"])
def edit_item(room, item_id):
    if request.method == "POST":
        form_values = request.form.to_dict()
        mongo.db[room].update({"_id": ObjectId(item_id)}, form_values)
        
        if form_values["room_name"] != room:
            item = mongo.db[room].find_one({"_id": ObjectId(item_id)})
            mongo.db[room].remove(item)
            mongo.db[form_values["room_name"]].insert(item)
        
        return redirect(url_for("show_item_detail", room=form_values["room_name"], item_id=item_id))    
    else:
        item = mongo.db[room].find_one({"_id": ObjectId(item_id)})
        rooms = get_room_names()
        
        return render_template("edit_item.html", item=item, rooms=rooms, item_room=room)


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)