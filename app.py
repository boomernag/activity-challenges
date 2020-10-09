import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.exceptions import HTTPException
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


@app.route("/search", methods=["GET", "POST"])
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
            "activated": False,
            "completions": 0,
        }
        mongo.db.challenges.insert_one(challenge)
        flash("Task Successully Added")
        return redirect(url_for("get_challenges"))

    return render_template("add_challenge.html", times=[1, 2, 5, 10])


@app.route("/edit_challenge/<challenge_id>", methods=["GET", "POST"])
def edit_challenge(challenge_id):
    challenge = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})
    if not challenge:
        flash("Challenge does not exist")
        return redirect(url_for("get_challenges"))

    if challenge['activated']:
        flash("Challenge cannot be edited while activated")
        return redirect(url_for("get_challenges"))

    checkedTime = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})
    # checkedTime = challenge.time
    if request.method == "POST":
        submit = {
            "challenge_title": request.form.get("challenge_title"),
            "challenge_description": request.form.get("challenge_description"),
            "time": request.form.get("timetocomplete"),
            "activated": False,
            "completions": 0,
        }
        mongo.db.challenges.update(
            {"_id": ObjectId(challenge_id)}, {"$set": submit})
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
        "activated": True,
    }

    mongo.db.challenges.update_one(
        {"_id": ObjectId(challenge_id)}, {"$set": submit})
    flash("Challenge Activated")
    return redirect(url_for("get_challenges"))


@app.route("/deactivated_challenge/<challenge_id>")
def deactivated_challenge(challenge_id):
    challenge = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})
    completions_count = challenge["completions"]
    completions_count += 1

    submit = {
        "challenge_title": challenge["challenge_title"],
        "challenge_description": challenge["challenge_description"],
        "time": challenge["time"],
        "activated": False,
        "completions": completions_count
    }
    mongo.db.challenges.update_one(
        {"_id": ObjectId(challenge_id)}, {"$set": submit})
    flash("Challenge Completed")
    return redirect(url_for("get_challenges"))


@app.route("/delete_challenge/<challenge_id>")
def delete_challenge(challenge_id):
    challenge = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})
    if not challenge:
        flash("Challenge does not exist")
        return redirect(url_for("get_challenges"))

    mongo.db.challenges.remove({"_id": ObjectId(challenge_id)})
    flash("Challenge Successfully Deleted")
    return redirect(url_for("get_challenges"))


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    flash("Challenge does not exist")
    return render_template("challenges.html", e=e), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
