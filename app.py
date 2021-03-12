# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:22:26 2021

@author: administrator
"""


from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import requests
from flask import jsonify

app = Flask(__name__)
model = pickle.load(open("C:/Users/Administrator/Desktop/Devvrat/ModelDeployment/Azure/Randomforestmodel3/model.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")



@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        channel=request.form['channel']
        if(channel=='Banca'):
            Banca = 1
            NonBanca = 0
            Digital = 0
            
        elif(channel=='NonBanca'):
            Banca = 0
            NonBanca = 1
            Digital = 0 
            
        elif(channel=='Digital'):
            Banca = 0
            NonBanca = 0
            Digital = 1
            
        else:
            Banca = 0
            NonBanca = 0
            Digital = 0
            
        segment = request.form["segment"]
        if (segment=='Compact'):
            Compact = 1
            midsize = 0
        elif(segment=='midsize'):
            Compact = 0
            midsize = 1
        else:
            Compact = 0
            midsize = 0
            
        prediction = model.predict([[
            Banca,
            NonBanca,
            Digital,
            Compact,
            midsize
        ]])
        
        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your rate is. {}".format(output))


    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
            
                                   
                                  
            