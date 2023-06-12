from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Ruta pagina inicio

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
         # Obtener los datos del formulario y crear un objeto CustomData
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        # Convertir el objeto CustomData en un DataFrame
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")
        # Crear una instancia de PredictPipeline
        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        # Realizar la predicción usando el pipeline

        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        # Renderizar la plantilla 'home.html' y pasar los resultados de la predicción

        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        
