from flask import Flask, render_template, request, jsonify, make_response
import pickle
import numpy as np

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
    prob=loaded_model.predict(final)
    

    return render_template('after.html', data=prob)

@app.route('/predict_api', methods=['POST', 'GET'])
def predict_api():
    # for direct API calls through request

    data = request.get_json(force=True)
    prediction = loaded_model.predict([np.array(list(data.values()))])

if __name__ == '__main__':
    app.run(debug=True)
