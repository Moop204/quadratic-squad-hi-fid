from flask import Flask, render_template
application = Flask(__name__)

# done
@application.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

# done
@application.route("/create_account", methods=["GET", "POST"])
def create_account():
    return render_template("create_account.html")

# need buttons to other main pages, i ll do this
@application.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")

# needs to show the profile of the <username>
# for now just show a page with the <username> at the top, and button to send match request
@application.route("/user/<username>", methods=["GET", "POST"])
def user_profile(username):
    return render_template("user_profile.html", username = username)

# needs to show a list of matches, a list of match requests, as well as a find matches button
# have 1 example for a match request, with accept/reject button
# have 1 example for an already matched person, with a profile link (see above function)
# find matches button doesnt actually needa do anything, see the edit profile button in the dashboard
@application.route("/match", methods=["GET", "POST"])
def match():
    return render_template("match.html")

# 1 example of a chat, doesnt have to actually work, just write down some example messages
# messages grouped by user
@application.route("/message", methods=["GET", "POST"])
def message():
    return render_template("message.html")

# done
@application.route("/textbooks", methods=["GET", "POST"])
def textbooks():
    return render_template("textbooks.html")

# done
@application.route("/textbooks/<textbook>", methods=["GET", "POST"])
def textbook_individual(textbook):
    return render_template("textbook_individual.html", textbook = textbook)

# done
@application.route("/calendar", methods=["GET", "POST"])
def calendar():
    return render_template("calendar.html")
 
if __name__ == "__main__":
    application.run(port=8080)
