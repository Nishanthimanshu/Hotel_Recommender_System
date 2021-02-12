import pandas as pd
import numpy as np
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def info():
    msg = ""
    if request.method=="POST" and "destination" in request.form and "adults" in request.form and "child" in request.form and "sd" in request.form:
        df = pd.read_csv("result.csv")
        dest = request.form.get("destination")
        adults = request.form.get("adults")
        child = request.form.get("child")
        stay_dur = request.form.get("sd")
        room = request.form.get("room")
        df = df[(df["srch_destination_id"] == int(dest)) & (df["srch_adults_cnt"] == int(adults))]
        df = df[(df["srch_children_cnt"] == int(child)) & (df["srch_rm_cnt"] == int(room))]
        df = df[df["stay_dur"] == float(stay_dur)]
        msg = df["prediction"][0]
        msg = "Recommended Hotel_cluster_id are: {}".format(msg)
    else:
        msg= "Please fill the form"

    return render_template('info.html', msg=msg)


if __name__=="__main__":
    app.run(debug=True)