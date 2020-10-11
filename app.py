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
    challenges = list(mongo.db.challenges.find({"activated": True}))
    return render_template("home.html", challenges=challenges)


@app.route("/search/challenges", methods=["GET", "POST"])
def search_challenges():
    query = request.form.get("query")
    challenges = list(mongo.db.challenges.find({"$text": {"$search": query}}))
    return render_template("challenges.html", challenges=challenges)


@app.route("/search/home", methods=["GET", "POST"])
def search_home():
    query = request.form.get("query")
    challenges = list(mongo.db.challenges.find({"$text": {"$search": query}}))
    return render_template("home.html", challenges=challenges)


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
    """ Edits the challenge by Id if it exists and is not activated.
    Flashes a message on screen.
    If request method is post and challenge is valid then saves the challenge.

    Args:
      challenge_id : An id of the challenge.
    Returns:
        If request method is get then renders the edit_challenge.html.
        If challenge does not exist or challenge is activated or request
        method is post then redirects the user to get_challenges.html.
    """
    challenge = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})
    if not challenge:
        flash("Challenge does not exist")
        return redirect(url_for("get_challenges"))

    if challenge['activated']:
        flash("Challenge cannot be edited while activated")
        return redirect(url_for("get_challenges"))

    checked_time = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})
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
    return render_template("edit_challenge.html", value=checked_time, challenge=challenge, times=[1, 2, 5, 10], checked=checked_time)


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
    """ Deletes the challenge by Id. Flashes error message if challenge does not exists.
    Args:
        challenge_id : An id of the challenge.
    Returns:
        Redirects the user to get_challenges.
    """
    challenge = mongo.db.challenges.find_one({"_id": ObjectId(challenge_id)})
    if not challenge:
        flash("Challenge does not exist")
        return redirect(url_for("get_challenges"))

    mongo.db.challenges.remove({"_id": ObjectId(challenge_id)})
    flash("Challenge Successfully Deleted")
    return redirect(url_for("get_challenges"))


@app.errorhandler(Exception)
def handle_exception(exception_thrown):
    """ Handles Http and non http execptions.
        Also flashes error message.
        Args:
            exception_thrown : An exception thrown.
        Returns:
        Renders the challenges html.
    """
    if isinstance(exception_thrown, HTTPException):
        return exception_thrown

    flash("Challenge does not exist")
    return render_template("challenges.html", exception_thrown=exception_thrown), 500


@app.errorhandler(404)
def page_not_found(error):
    flash("Challenge does not exist")
    return render_template('challenges.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
