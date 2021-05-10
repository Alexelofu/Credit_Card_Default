from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for
import pickle
import numpy as np
import json

app = Flask(__name__)

filename = 'model/new_model'
loaded_model = pickle.load(open(filename, 'rb'))

col=['LIMIT','SEX','EDUCATION','MARRIAGE','AGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6','BILL_AMT1','BILL_AMT2','BILL_AMT3', 'BILL_AMT4','BILL_AMT5','BILL_AMT6','PAY_AMT1','PAY_AMT2','PAY_AMT3', 'PAY_AMT4','PAY_AMT5','PAY_AMT6' ]

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final=[np.array(int_features, dtype=float)]
    prob=loaded_model.predict(final)[0]
    
   
    result = 'will default' if prob >= 0.3 else 'will pay'
    return jsonify(result)
  
   #  if prob >= 0.3:
   #         return jsonify('will default')
   #  else:
   #         return jsonify('will pay')
    
  

if __name__ == '__main__':
    app.run(port=5000, debug=True)
