from flask import Flask, json, render_template, redirect, request
from flask import jsonify

# ----- dummy data
data={

    "A" : {
        "ticker": "A",
        "closing" : "3.44",
        "open" : "3",
        "sentiment" : "0.323"
    },

    "B" : {
        "ticker": "B",
        "closing" : "10",
        "open" : "1444",
        "sentiment" : "-0.9"
    }
}

#----------------- BASIC ENDPOINTS -------------------- 

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

# API works by passing quereys e.g. {url}/query?key=value&key=value&key=value
# each key value pair is seperated by & and the full query is preceeded by a ? 
# Structure: we index the data by ticker symbol and then make an API call for that ticker symbol. Should return json object with all data for that symbol. 
# need another endpoint to do searches by date
@app.route("/query", methods=['GET', 'POST'])
def query():
    input = request.args.get('ticker')
    print(input)
    #here use this key to find the corrisponding value and return it. Should pass a stock ticker and return a json object with all the correponding data. 
    
    return jsonify(data[input])


#---------------- API BELOW -----------------

@app.route('/person/')
def hello():
    return jsonify({'name':'Jimit',
                    'address':'India'})


#------------ RUN FLASK --------------------
if __name__ == '__main__':
    app.run(debug=True)

