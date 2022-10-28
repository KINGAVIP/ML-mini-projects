from ast import main
import imp
from flask import Flask,render_template,request
import pickle
# import numpy as np
# import pandas as pd
app=Flask(__name__)


@app.route('/')
def main():
    return render_template('home.html')

@app.route('/home',methods=['POST'])
def home(): 
    data1=request.form['a']
    data2=request.form['b']
    return render_template('after.html',data=data1,date=data2)
if __name__ ==" __main__ ":
    app.run(debug=True)