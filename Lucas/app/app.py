from flask import Flask, json, render_template, redirect, request
from flask import jsonify
import pandas as pd
import json

#--------------------- DATA PROCESSING ------------------

f = open('..\..\DataFiles\weekly_data.json',)

data = json.load(f)



#----------------- BASIC ENDPOINTS -------------------- 

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html", data=data)

@app.route('/heatmap')
def heatmap():
    return render_template("Heatmap.html", data=data)

# API works by passing quereys e.g. {url}/query?key=value&key=value&key=value
# each key value pair is seperated by & and the full query is preceeded by a ? 
# Structure: we index the data by ticker symbol and then make an API call for that ticker symbol. Should return json object with all data for that symbol. 
# need another endpoint to do searches by date
@app.route("/query", methods=['GET', 'POST'])
def query():
    input = request.args.get('ticker')
    #here use this key to find the corrisponding value and return it. Should pass a stock ticker and return a json object with all the correponding data. 
    
    return (data)


#---------------- API BELOW -----------------

@app.route('/person/')
def hello():
    return jsonify({'name':'Jimit',
                    'address':'India'})


#------------ RUN FLASK --------------------
if __name__ == '__main__':
    app.run(debug=True)

