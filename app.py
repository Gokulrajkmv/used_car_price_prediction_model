import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

# initialise the Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')# html front end

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 6)
    loaded_model = pickle.load(open("used_car.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    #print(result)
    return result[0]


@app.route('/results',methods=['POST'])
def result():
    if request.method== 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        #to_predict_list = list(to_predict_list)
        #print(to_predict_list)
        result = ValuePredictor(to_predict_list)
        #result = np.exp(result)
        #min_price = np.absolute(result-85000)
        #min_price =round(min_price,2)
        result =round(result,2)

        if result<0:
            return render_template('result.html',prediction_text="Sorry we can't get the predict price of your car")
        else:
            return render_template('result.html',prediction_text=f"selling price of the car  Rs.{result} in lakhs")

if __name__ == '__main__':
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
