# packages
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
    loaded_model = pickle.load(open("grading_boost_used_car.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


# route function for results display
@app.route('/result',methods=['POST'])
def result():
    if request.method== 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        #to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)

        return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
