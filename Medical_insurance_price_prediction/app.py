import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import pandas
import numpy as np

#starting point of application
app = Flask(__name__)
# Load model in read byte way

with open('reg_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')

#@app.route('/predict_api', methods = ['POST'])
#def predict_api():
#    data = request.json['data']
#    print(data)
#    print(np.array(list(data.values)).reshape(1, -1))
#    new_data = scaler.transform(np.array(list(data.values)).reshape(1, -1))
#    output = regmodel.predict(new_data)
#    print(output)
#    return jsonify(output[0])

@app.route('/predict', methods = ['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    final_input = scaler.transform(np.array(data).reshape(1, -1))
    print(final_input)
    reg_model = pickle.load(open('reg_model.pkl', 'rb'))
    output = reg_model.predict(final_input)
    print(output)
    return render_template("home.html", prediction_text = "The Medical insurance cost predicted is ${}" .format(np.round(output[0]),2))

if __name__ == "__main__":
    app.run(debug = True)


