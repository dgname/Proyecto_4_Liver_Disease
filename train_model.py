import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Cargar los datos del CSV
data = pd.read_csv('RESOURCES/Liver_disease_data.csv')

# Separar las características y la variable objetivo
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Definir y entrenar el modelo XGBoost
model = XGBClassifier(n_estimators=200, random_state=42)
model.fit(X_train_scaled, y_train)

# Guardar el modelo y el escalador
joblib.dump(model, 'xgboost_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
