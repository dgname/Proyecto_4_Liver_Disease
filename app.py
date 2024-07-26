from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import keras_tuner as kt

app = Flask(__name__)

# Cargar los datos del CSV
data = pd.read_csv('RESOURCES/Liver_disease_data.csv')

# Preprocesamiento y entrenamiento del modelo
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

X_scaler = StandardScaler()
X_train_scaled = X_scaler.fit_transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

def create_model(hp):
    nn_model = tf.keras.models.Sequential()
    activation = hp.Choice('activation', ['relu', 'tanh', 'sigmoid'])
    input_dim = X_train_scaled.shape[1]
    nn_model.add(tf.keras.layers.Dense(units=hp.Int('first_units', min_value=1, max_value=10, step=2), activation=activation, input_dim=input_dim))

    for i in range(hp.Int('num_layers', 1, 6)):
        nn_model.add(tf.keras.layers.Dense(units=hp.Int('units_' + str(i), min_value=1, max_value=10, step=2), activation=activation))

    nn_model.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))
    nn_model.compile(loss="binary_crossentropy", optimizer='adam', metrics=["accuracy"])

    return nn_model

tuner = kt.Hyperband(
    create_model,
    objective="val_accuracy",
    max_epochs=20,
    hyperband_iterations=2,
    overwrite=True
)

tuner.search(X_train_scaled, y_train, epochs=20, validation_data=(X_test_scaled, y_test))
best_model = tuner.get_best_models(1)[0]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = np.array([[
        data['age'], data['gender'], data['bmi'], data['alcohol'],
        data['smoking'], data['genetic'], data['activity'],
        data['diabetes'], data['hypertension']
    ]])
    input_data_scaled = X_scaler.transform(input_data)
    prediction = best_model.predict(input_data_scaled)
    prediction_result = 'Positive' if prediction[0] > 0.5 else 'Negative'

    return jsonify({'prediction': prediction_result})

if __name__ == '__main__':
    app.run(debug=True)