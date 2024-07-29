from flask import Flask, render_template, request, jsonify
from config import CONNSTRING
from sqlalchemy import create_engine
import pandas as pd
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__, static_folder='static', template_folder='templates')

# Load the machine learning model
model_path = 'model_gbm.pkl'
scaler_path = 'scaler_gbm.pkl'

# Load the model
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Load the scaler
with open(scaler_path, 'rb') as file:
    scaler = pickle.load(file)

# Database connection
engine = create_engine(CONNSTRING)

@app.route("/")
def take_me_to_liver_disease_predictor():
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

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON data from the request
        data = request.get_json() # The request object in Flask provides access to the data sent by the client. 
        
        # Extract features from the data
        features = np.array([
            int(data['age']),                      # Convert age to int
            int(data['gender']),                   # Convert gender to int
            float(data['bmi']),                    # Convert bmi to float
            float(data['alcoholconsumption']),     # Convert alcoholconsumption to float
            int(data['smoking']),                  # Convert smoking to int
            int(data['geneticrisk']),              # Convert geneticrisk to int
            float(data['physicalactivity']),       # Convert physicalactivity to float
            int(data['diabetes']),                 # Convert diabetes to int
            int(data['hypertension']),             # Convert hypertension to int
            float(data['liverfunctiontest'])       # Convert liverfunctiontest to float
        ]).reshape(1, -1)  # Reshape for a single sample

        # Scale the features
        scaled_features = scaler.transform(features)
        
        # Predict using the model
        prediction = model.predict(scaled_features)[0] # extract the first element from the prediction result
        
        # Return the prediction as JSON
        return jsonify({'prediction': int(prediction)})
    
    except Exception as e:
        # Return an error message in case of failure
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
