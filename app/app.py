from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='static/none.png', href3='')
    else:
        myage = request.form['age']
        mygender = request.form['gender']
        mybag = ''
        if str(myage) =='' or str(mygender) =='':
            return render_template('index.html', href2='static/none.png', href3='Please insert your age and gender.')
        else:
            model = load('app/bag-recommander.joblib')
            np_arr = np.array([myage, mygender])
            predictions = model.predict([np_arr])  
            predictions_to_str = str(predictions)
            
            if 'backpack' in predictions_to_str:
                mybag = 'static/backpack.jpg'
            elif 'briefcase' in predictions_to_str:
                mybag = 'static/briefcase.jpg'
            elif 'bucket bag' in predictions_to_str:
                mybag = 'static/bucket-bag.jpg'
            elif 'duffel bag' in predictions_to_str:
                mybag = 'static/duffel-bag.jpg'
            elif 'flap bag' in predictions_to_str:
                mybag = 'static/flap-bag.jpg'
            elif 'tote bag' in predictions_to_str:
                mybag = 'static/tote-bag.jpg'
            else:
                mybag = 'static/none.png' 
                
            return render_template('index.html', href2=str(mybag), href3='The suitable bread for you (age:'+str(myage)+' ,gender:'+str(mygender)+') is:'+predictions_to_str)
        

