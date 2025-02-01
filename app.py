from flask import Flask,render_template,redirect,request
from pymongo import MongoClient

app = Flask(__name__)
my_client = MongoClient("localhost", 27017)
my_db= my_client["Portfolio"]
user = my_db["User"]


@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")

@app.route("/about", methods = ["GET"])
def about():
    return render_template("about.html")

@app.route("/projects", methods = ["GET"])
def projects():
    return render_template("projects.html")

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phno = request.form["phno"]
        org = request.form["org"]
        loc = request.form["loc"]

        user.insert_one({"name ": name, "email ": email, "phno ": phno, "organization ": org, "location ":loc})
        return redirect("/contact")

    return render_template("contact.html")

app.run(debug=True)