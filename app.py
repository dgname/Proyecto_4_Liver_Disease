from flask import Flask, render_template, send_from_directory, abort, jsonify
from config import CONNSTRING
from sqlalchemy import create_engine
import pandas as pd
import os

engine = create_engine(CONNSTRING)

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def take_me_to_liver_disease_predictor():
    return render_template('index.html')

@app.route('/api')
def api():
        with engine.connect() as conn:

            finddf=pd.read_sql('Select * From PatientData',con=conn)
            dfgroup=finddf[['Age', 'Gender', 'BMI', 'AlcoholConsumption', 'Smoking', 'GeneticRisk', 'PhysycalActivity', 'Diabetes', 'Hypertension', 'LiverFunctionTest', 'Diagnosis']]
            dfgroup.reset_index(inplace=True)

        return dfgroup.to_json(orient='records')
