from flask import request
import pandas as pd
from collections import OrderedDict


def func():
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
        new_customer1[key] = int(value)

    return new_customer1
  

if __name__ == '__main__':
    # app.run(port=5000, debug=True)
    print(func())