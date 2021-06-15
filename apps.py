from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for
import pickle
import numpy as np
import json
from collections import OrderedDict
import pandas as pd

app = Flask(__name__)

filename = 'model/new_model'
loaded_model = pickle.load(open(filename, 'rb'))

col=['LIMIT','SEX','EDUCATION','MARRIAGE','AGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6','BILL_AMT1','BILL_AMT2','BILL_AMT3', 'BILL_AMT4','BILL_AMT5','BILL_AMT6','PAY_AMT1','PAY_AMT2','PAY_AMT3', 'PAY_AMT4','PAY_AMT5','PAY_AMT6' ]



@app.route('/predicts', methods=['POST'])
def predicts():
    data = request.get_json()
   
    new_customer = OrderedDict([('LIMIT_BAL', data['LIMIT']),('SEX', data['SEX'] ),('EDUCATION', data['EDUCATION']),
                                ('MARRIAGE', data['MARRIAGE'] ),('AGE', data['AGE'] ),('PAY_0', data['PAY_0'] ),
                                ('PAY_2', data['PAY_2'] ),('PAY_3', data['PAY_3'] ), ('PAY_4', data['PAY_4'] ),('PAY_5', data['PAY_5']),
                                ('PAY_6', data['PAY_6'] ),('BILL_AMT1', data['BILL_AMT1']),('BILL_AMT2', data['BILL_AMT2'] ), ('BILL_AMT3', data['BILL_AMT3'] ),
                                ('BILL_AMT4', data['BILL_AMT4'] ),('BILL_AMT5', data['BILL_AMT5'] ),('BILL_AMT6', data['BILL_AMT6'] ), ('PAY_AMT1', data['PAY_AMT1']),
                                ('PAY_AMT2', data['PAY_AMT2']),('PAY_AMT3', data['PAY_AMT3']),('PAY_AMT4', data['PAY_AMT4'] ),('PAY_AMT5', data['PAY_AMT5']),
                                ('PAY_AMT6', data['PAY_AMT6'])])

    # convert to integer
    new_customer1 = {}
    for key, value in new_customer.items():
        new_customer1[key] = int(value )

    # int_features = [int(x) for x in data]
    # final=[np.array(int_features, dtype=float)]
    # prob=loaded_model.predicts(final)[0]
    
    # convert to df
    # df = pd.DataFrame.from_records(new_customer1, index=[0])
    df = pd.DataFrame.from_records(new_customer1, index=[0])
    # convert to array
    df_array = df.to_numpy()
    # make predictions
    prob = loaded_model.predict(df_array)[0]
   
    result = 'will default' if prob >= 0.3 else 'will pay'
    return jsonify(result)

  
    # if prob >= 0.3:
    #        return jsonify('will default')
    # else:
    #        return jsonify('will pay')
    


if __name__ == '__main__':
    app.run(port=5000, debug=True)
