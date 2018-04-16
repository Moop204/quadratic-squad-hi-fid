from flask import Flask, render_template
application = Flask(__name__)

@application.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@application.route("/create_account", methods=["GET", "POST"])
def create_account():
    return render_template("create_account.html")

@application.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")

@application.route("/user/<username>", methods=["GET", "POST"])
def user_profile(username):
    return render_template("user_profile.html", username = username)

@application.route("/match", methods=["GET", "POST"])
def match():
    return render_template("match.html")

@application.route("/message", methods=["GET", "POST"])
def message():
    return render_template("message.html")

@application.route("/meetup", methods=["GET", "POST"])
def meetup():
    return render_template("meetup.html")

@application.route("/textbooks", methods=["GET", "POST"])
def textbooks():
    return render_template("textbooks.html")

@application.route("/textbooks/<textbook>", methods=["GET", "POST"])
def textbook_individual(textbook):
    return render_template("textbook_individual.html", textbook_name = textbook)
 
if __name__ == "__main__":
    application.run(port=8080)
