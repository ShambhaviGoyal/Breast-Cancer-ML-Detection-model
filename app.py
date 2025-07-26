from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('models/model.pkl')

# Initialize the Flask app
app = Flask(__name__)

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the form
    input_str = request.form['feature']
    feature_list = [float(x.strip()) for x in input_str.split(',')]

    # Convert to NumPy array and reshape for model input
    features = np.array(feature_list).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)[0]

    # Prepare result message
    if prediction == 1:
        message = ['Cancerous']
    else:
        message = ['Not Cancerous']

    return render_template('index.html', message=message)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
