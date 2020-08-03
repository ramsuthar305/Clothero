from flask import Flask,request, render_template, jsonify
import json
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config.from_object("config.Config")
mongo = PyMongo(app)
mongo=mongo.db
from bson import ObjectId
import numpy as np
import os
import math 
from math import sqrt
#import pandas as pd

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class TensorVector():

  def __init__(self):
      pass

  def cosineSim(self,a1,a2):
    sum = 0
    suma1 = 0
    sumb1 = 0
    for i,j in zip(a1, a2):
        suma1 += i * i
        sumb1 += j*j
        sum += i*j
    cosine_sim = sum / ((sqrt(suma1))*(sqrt(sumb1)))
    return cosine_sim

  def jaccard_similarity(self,list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

  def average(self,x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

  def pearson_def(self,x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = self.average(x)
    avg_y = self.average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

  def mean(self,vector1,vector2):
    cs=self.cosineSim(vector1,vector2)
    #js=self.jaccard_similarity(vector1,vector2)
    ps=self.pearson_def(vector1,vector2)
    #print(cs,ps)
    average=(cs+ps)/2
    #print(average)
    return average

  def compare(self,vector1,vector2):
    return self.mean(np.array(vector1),np.array(vector2))


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
        #print(req)
        user_picks=[None]*len(req['elemIds'])
        for id in range(len(req['elemIds'])):
            user_picks[id]=mongo.picks.find_one({'_id':ObjectId(req['elemIds'][id])},{'Vector':1})
        #print(user_picks)
        all_clothes=list(mongo.data.find({'Type':req['type'].lower()},{'Vector':1,'Type':1}).limit(100))
        #print(all_clothes[0]['Type'])
        class_obj=TensorVector()
        all_comparison_rows=[[None]*100]*len(req['elemIds'])
        ##print(all_comparison_rows)
        for i in range(len(user_picks)):
            for j in range(len(all_clothes)):
              
                vector1=json.loads(user_picks[i]['Vector'])
                #print("type of vector id",all_clothes[j]['_id'])
                #print("type of vector id",all_clothes[j]['Vector'])
                vector2=json.loads(all_clothes[j]['Vector'])
                #print("type of vector 2",np.array(vector2))

                all_comparison_rows[i][j]={'id':all_clothes[j]['_id'],'similarity':class_obj.compare(vector1,vector2)}
            all_comparison_rows[i]=sorted(all_comparison_rows[i], key=lambda k: k['similarity'], reverse=True)
            all_comparison_rows[i]=all_comparison_rows[i][:50]
            all_comparison_rows[i]=set([sub['id'] for sub in all_comparison_rows[i]])
            #print(len(all_comparison_rows[i]))
        final_list=list(set.intersection(*all_comparison_rows))
        #print(final_list)
        #print(len(final_list))
        response=[None]*len(final_list)
        for id in range(len(final_list)):
            response[id]=mongo.data.find_one({'_id':final_list[id]},{'Vector':0,'_id':0})
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
    

