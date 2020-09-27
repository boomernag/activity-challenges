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


@app.route("/add_challenge", methods=["GET", "POST"])
def add_challenge():
    if request.method == "POST":
        challenge = {
            "challenge_title": request.form.get("challenge_title"),
            "challenge_description": request.form.get("challenge_description"),
            "time": request.form.get("time"),
            "completion": request.form.get("completion") 
        }
        mongo.db.challenges.insert_one(challenge)
        flash("Task Successully Added")
        
    return render_template("add_challenge.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
            debug=True)
