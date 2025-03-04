from flask import Flask, render_template, request, session
import numpy as np
import requests
import json
import base64
import pandas as pd
import time

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "efiedoedkkkkfoiefnnoefnveodf"

@app.route('/questions', methods=["GENERAL", "SPECIFIC"])
def questions():
    return json.loads("Error":"0")


@app.route('/prognose', methods=["MANUAL", "AUTO"])
def prognose():
    if request.method == "MANUAL":
        paramsname=["latitude","longitude","massbody","Ta","RH","Ws","radG","age","work","year","month","day","hour","minu"]
        cityparms={}
        for i in paramsname:
            try:
                cityparms[i]=request.form[i]:
            except:
                return json.loads({"ERROR":"801"})#'Some params not found.'

        if timenow()[:5]!=cityn["time"]:
            updatepet(cityparams)
        
        # download data from github
        req = requests.get(url)

        return req
    if request.method == "AUTO":
        city = request.form["city"]
        cities=json.loads("cities.json")
        cityn=cities.get(city)
        if cityn!=False:
            data_url = 'https://api.github.com/repos/noahtingb/saker_lopning_API_code6372/data/'+cityn.get('filename')+'.json'
        else:
            return json.loads({"ERROR":"921"})#'Prognose for ' + city + ', not found.'

        if timenow()[:5]!=cityn["time"]:
            params=updatecity(cityn)
            updatepet(params)
        # download data from github
        req = requests.get(url)
        return req 
def timenow():
    t1=time.asctime().split(" ")
    t1[4]=t1[4].split(":")
    t1[1]={"Jan":0,"Feb":1,"Mar":2,"Apr":3,"May":4,"Jun":5,"Jul":6,"Aug":7,'Sep': 8, 'Oct': 9,'Nov': 10,'Dec': 11}[t1[1]]
    return [int(t1[5]),t1[1],int(t1[3]),int(t1[4][0]),int(t1[4][1]),int(t1[4][2])]