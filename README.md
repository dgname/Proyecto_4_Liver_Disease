# Liver Disease Predictor

## Overview
The Liver Disease Predictor is a machine learning project designed to estimate the likelihood of liver disease based on various health parameters. The project uses a dataset of liver disease indicators to train a predictive model, providing users with insights into their liver health.

## Features
- **Predictive Model**: Utilizes advanced machine learning techniques to predict liver disease probability.
- **User-Friendly Interface**: An intuitive web application for inputting health data and receiving predictions.
- **High Accuracy**: Achieves 91% accuracy in predicting liver disease.
- **Educational Content**: Provides information on liver disease, its risks, and preventive measures.
  
## Getting Started

### Prerequisites
- Python 3.x
- Flask
- scikit-learn
- Pandas
- Bootstrap (for styling)
- Numpy
- Matplotlib
- Seaborn
- SQLAlchemy
- LightGBM
- Joblib
- Jupyter Notebook
  
1. **Clone the Repository**

   ```bash
   git clone https://github.com/dgname/Proyecto_4_Liver_Disease.git
   
2. **Install Dependencies
pip install -r requirements.txt

3. **Run the Application
python app.py

4. **Access the Application
Open your web browser and go to http://127.0.0.1:5000 to access the application.


## Dataset

  **Dataset Source**: [Liver Disease Dataset](https://www.kaggle.com/datasets/rabieelkharoua/predict-liver-disease-1700-records-dataset)

The dataset includes the following features:

- `Age`: The age of the individual.
- `Gender`: The gender of the individual.
- `BMI`: Body Mass Index of the individual.
- `AlcoholConsumption`: Whether the individual consumes alcohol.
- `Smoking`: Whether the individual smokes.
- `GeneticRisk`: Genetic risk factor for liver disease.
- `PhysicalActivity`: Level of physical activity of the individual.
- `Diabetes`: Whether the individual has diabetes.
- `Hypertension`: Whether the individual has hypertension.
- `LiverFunctionTest`: Results of liver function tests.
- `Diagnosis`: The diagnosis of liver disease.

  
## Model Training

1. **Data Preprocessing**: Clean and preprocess the dataset to handle missing values and standardize features.
2. **Feature Selection**: Identify and select the most relevant features for effective model training.
3. **Model Training**: 
   - Train the predictive model using **LightGBM** (Light Gradient Boosting Machine), a powerful and efficient gradient boosting framework. LightGBM excels in performance with large datasets and high-dimensional features.
   - Save and load the trained model using **joblib**, a library for serializing Python objects. Joblib is used to persist the trained LightGBM model for later use and to deploy the model in a production environment.
4. **Evaluation**: 
   - Assess the model's performance using metrics such as accuracy, confusion matrix, and classification report.
   - Fine-tune the model parameters based on evaluation results to improve accuracy and robustness.


## Application Structure

- **`app.py`**: Main Flask application file.
- **`templates/`**: HTML templates.
- **`static/`**: Static files (CSS, JavaScript).


## Future Possible Improvements

- **Enhanced Model Accuracy**: Explore additional machine learning algorithms and hyperparameter tuning to improve prediction accuracy.
- **Additional Features**: Integrate more health indicators and features to provide a more comprehensive assessment.
- **User Authentication**: Add user authentication and authorization for personalized experience and data privacy.
- **Visualization Enhancements**: Improve data visualizations and reporting for better user insights.
- **API Development**: Develop a RESTful API to allow integration with other applications and services.

## Contributors

- **Daniel Name** 
- **Julio Carramiñana**
- **Katia Cuevas**
- **Oscar Tlacuilo** 





### MODEL IS ONLY FOR EDUCATIONAL PURPOSES. DO NOT USE AS RPOFESSIONAL REFERENCE 
