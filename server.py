# Zac Capell
# HeavyWater Solutions Front End Engineer Test
# 4/27/2020

from flask import render_template
import connexion


app = connexion.App(__name__, specification_dir='./')

app.add_api("swagger.yml")


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/classifications")
def classifications():
    return render_template('classifications.html')


@app.route("/classupdate")
def class_update():
    return render_template('classupdate.html')


@app.route("/extractions")
def extractions():
    return render_template('extractions.html')


# @app.route("/extract_update")
# def extract_update():
#   return render_template('extractupdate.html')


if __name__ == "__main__":
    app.run(debug=True)
