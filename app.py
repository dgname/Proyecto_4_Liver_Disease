from flask import Flask, render_template, request, jsonify, url_for, redirect
from config import CONNSTRING
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import joblib

# Initialize Flask app
app = Flask(__name__, static_folder='static', template_folder='templates')

model = joblib.load('model_gbm.joblib')
scaler = joblib.load('scaler_gbm.joblib')

# Database connection
engine = create_engine(CONNSTRING)

@app.route("/")
def take_me_to_about():
    return render_template('about.html')

@app.route("/index")
def take_me_to_index():
    return render_template('index.html')

@app.route('/api')
def api():
    with engine.connect() as conn:
        # Fetch data from the database
        finddf = pd.read_sql('SELECT * FROM patientdata', con=conn)
        
        # Ensure column names are correct
        dfgroup = finddf[['age', 'gender', 'bmi', 'alcoholconsumption', 'smoking', 'geneticrisk', 'physicalactivity', 'diabetes', 'hypertension', 'liverfunctiontest', 'diagnosis']]
        
        # Reset index if needed
        dfgroup.reset_index(drop=True, inplace=True)
    
    # Convert DataFrame to JSON and return
    return dfgroup.to_json(orient='records')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST' :

        try:
            # Parse JSON data from the request
            data = request.form # The request object in Flask provides access to the data sent by the client. 
            
            # Accessing form data using the key names
            age = int(data.get('age', 0))  # Convert to int with default value
            gender = int(data.get('gender', 0))  # Convert to int with default value
            bmi = float(data.get('bmi', 0.0))  # Convert to float with default value
            alcohol_consumption = float(data.get('alcoholconsumption', 0.0))  # Convert to float with default value
            smoking = int(data.get('smoking', 0))  # Convert to int with default value
            geneticrisk = int(data.get('geneticrisk', 0))  # Convert to int with default value
            physical_activity = float(data.get('physicalactivity', 0.0))  # Convert to float with default value
            diabetes = int(data.get('diabetes', 0))  # Convert to int with default value
            hypertension = int(data.get('hypertension', 0))  # Convert to int with default value
            liver_function_test = float(data.get('liverfunctiontest', 0.0))  # Convert to float with default value
            
            print(data)

            # Extract features from the data
            features = np.array([
                age,
                gender,
                bmi,
                alcohol_consumption,
                smoking,
                geneticrisk,
                physical_activity,
                diabetes,
                hypertension,
                liver_function_test
            ]).reshape(1, -1)  # Reshape for a single sample

            # Scale the features
            scaled_features = scaler.transform(features)
            
            # Predict using the model
            prediction = model.predict(scaled_features)[0] # extract the first element from the prediction result
            rounded_prediction = round(prediction)
            print(prediction)

            # Return the prediction
            return jsonify({'prediction': rounded_prediction})
        
        except Exception as e:
            # Return an error message in case of failure
            return jsonify({'error': str(e)}), 400
            print(e)
    

if __name__ == "__main__":
    app.run(debug=True)
