from flask import Flask,request, render_template, jsonify
import json
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config.from_object("config.Config")
mongo = PyMongo(app)
mongo=mongo.db
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as error:
        return error

@app.route('/get_pickers',methods=['GET','POST'])
def get_pickers():
    if request.method=='POST':
        req = request.get_data()
        req=json.loads(req)
        print(req['apparelType'])
        tshirts=list(mongo.picks.find({'Type':req['apparelType']},{'Vector':0}))
        return JSONEncoder().encode(tshirts[:8])

@app.route('/match',methods=['GET','POST'])
def get_match():
    if request.method=='POST':
        req = request.get_data()
        req=json.loads(req)
        print(req)
        user_picks=[None]*len(req)
        for id in range(len(req)):
            user_picks[id]=mongo.picks.find_one({'_id':ObjectId(req[id])},{'Vector':1})
        print(len(user_picks))
        return render_template('match.html')

if __name__ == '__main__':
    app.run(debug=True)
    

