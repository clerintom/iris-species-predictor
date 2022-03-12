import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_feature = [float(x) for x in request.form.values()]
    print(input_feature)
    species_feat = [np.array(input_feature)]
    print(species_feat)
    print(len(species_feat))
    prediction = model.predict(species_feat)
    return render_template('index.html', prediction_text ="The species of Iris is : {}".format(prediction[0]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090, debug=True)
