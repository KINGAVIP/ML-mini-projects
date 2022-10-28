from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle

app=Flask(__name__)
model=pickle.load(open('model_pkl','rb'))
# print(model.predict([[0,6,8]]))
@app.route("/")
def intro():
    # return "j"      
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    to_predict_list=request.form.to_dict()
    exp=to_predict_list['exp']
    test=to_predict_list['test']
    inter=to_predict_list['inter']
    # print()
    return render_template("index.html",predicted_score=round(model.predict([[exp,test,inter]])[0],2))

@app.route('/hel')
def hel():
    return "king"

if __name__ == "__main__":
    app.run(debug=True) 