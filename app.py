import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_challenges")
def get_challenges():
    challenges = mongo.db.challenges.find()
    return render_template("challenges.html", challenges=challenges)


@app.route("/home")
def home():
    challenges = list(mongo.db.challenges.find({"activated": "true"}))
    return render_template("home.html", challenges=challenges)


@app.route("/search", methods=["GET"])
def search():
    query = request.form.get("query")
    challenges = list(mongo.db.challenges.find({"$text": {"$search": query}}))
    return render_template("challenges.html", challenges=challenges)


@app.route("/add_challenge", methods=["GET", "POST"])
def add_challenge():
    if request.method == "POST":
        challenge = {
            "challenge_title": request.form.get("challenge_title"),
            "challenge_description": request.form.get("challenge_description"),
            "time": request.form.get("timetocomplete"),
            "activated": "true",
        }
        mongo.db.challenges.insert_one(challenge)
        flash("Task Successully Added")
        return redirect(url_for("get_challenges"))
        
    return render_template("add_challenge.html", times=[1, 2, 5, 10])


@app.route("/edit_challenge/<challenge_id>", methods = ["GET", "POST"])
def edit_challenge(challenge_id):
    challenge = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})

    checkedTime = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})
    # checkedTime = challenge.time
    if request.method == "POST":
        submit = {
            "challenge_title": request.form.get("challenge_title"),
            "challenge_description": request.form.get("challenge_description"),
            "time": request.form.get("timetocomplete"),
            "activated": "true",
        }
        mongo.db.challenges.update({"_id": ObjectId(challenge_id)}, submit)
        flash("Challenge Successfully Updated")
        return redirect(url_for("get_challenges"))

    challenge = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})
    return render_template("edit_challenge.html", value=checkedTime, challenge=challenge, times=[1, 2, 5, 10], checked=checkedTime)


@app.route("/activated_challenge/<challenge_id>")
def activated_challenge(challenge_id):
    challenge = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})

    submit = {
        "challenge_title": challenge["challenge_title"],
        "challenge_description": challenge["challenge_description"],
        "time": challenge["time"],
        "activated": "true",
    }
    mongo.db.challenges.update({"_id": ObjectId(challenge_id)}, submit)
    flash("Challenge Activated")
    return redirect(url_for("get_challenges"))


@app.route("/deactivated_challenge/<challenge_id>")
def deactivated_challenge(challenge_id):
    challenge = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})

    submit = {
        "challenge_title": challenge["challenge_title"],
        "challenge_description": challenge["challenge_description"],
        "time": challenge["time"],
        "activated": "false",
    }
    mongo.db.challenges.update({"_id": ObjectId(challenge_id)}, submit)
    flash("Challenge Completed")
    return redirect(url_for("get_challenges"))


@app.route("/delete_challenge/<challenge_id>")
def delete_challenge(challenge_id):
    mongo.db.challenges.remove({"_id": ObjectId(challenge_id)})
    flash("Challenge Successully Deleted")
    return redirect(url_for("get_challenges"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
            debug=True)
