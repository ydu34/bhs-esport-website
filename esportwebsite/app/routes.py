from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    esport = {"name": "League of Legends"}  # temporary, replace with database
    return render_template("index.html",
                           title='Esports',
                           esport=esport)

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/standings")
def standings():
    return render_template("standings.html")

@app.route("/rules")
def rules():
    return render_template("rules.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/leagueoflegends")
def leagueoflegends():
    return render_template("leagueoflegends/index.html")

@app.route("/hearthstone")
def hearthstone():
    return render_template("hearthstone/index.html")

@app.route("/overwatch")
def overwatch():
    return render_template("overwatch/index.html")

@app.route("/leagueoflegends/schedule")
def lolschedule():
    return render_template("leagueoflegends/schedule.html")

@app.route("/leagueoflegends/standings")
def lolstandings():
    return render_template("leagueoflegends/standings.html")

@app.route("/leagueoflegends/rules")
def lolrules():
    return render_template("leagueoflegends/rules.html")

@app.route("/leagueoflegends/about")
def lolabout():
    return render_template("leagueoflegends/about.html")

@app.route("/leagueoflegends/signup")
def lolsignup():
    return render_template("leagueoflegends/signup.html")

@app.route("/hearthstone/schedule")
def hsschedule():
    return render_template("hearthstone/schedule.html")

@app.route("/hearthstone/standings")
def hsstandings():
    return render_template("hearthstone/standings.html")

@app.route("/hearthstone/rules")
def hsrules():
    return render_template("hearthstone/rules.html")

@app.route("/hearthstone/about")
def hsabout():
    return render_template("hearthstone/about.html")

@app.route("/hearthstone/signup")
def hssignup():
    return render_template("hearthstone/signup.html")

@app.route("/overwatch/schedule")
def owschedule():
    return render_template("overwatch/schedule.html")

@app.route("/overwatch/standings")
def owstandings():
    return render_template("overwatch/standings.html")

@app.route("/overwatch/rules")
def owrules():
    return render_template("overwatch/rules.html")

@app.route("/overwatch/about")
def owabout():
    return render_template("overwatch/about.html")

@app.route("/overwatch/signup")
def owsignup():
    return render_template("overwatch/signup.html")




