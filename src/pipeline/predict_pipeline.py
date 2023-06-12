import os
import sys
import pandas as pd
'''se importan clases y funciones, como src.exception.CustomException y src.utils.load_object.'''
from src.exception import CustomException
from src.utils import load_object

'''La clase PredictPipeline implementa una tubería de predicción. El método predict carga un modelo previamente guardado y un preprocesador desde archivos. Luego,
transforma las características de entrada utilizando el preprocesador y realiza predicciones utilizando el modelo cargado. Devuelve las predicciones resultantes.'''
class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


'''La clase CustomData representa los datos personalizados de entrada para la predicción. Toma varios atributos que describen las características del estudiante. 
El método get_data_as_data_frame crea un diccionario con los valores de los atributos y luego
 crea un DataFrame de pandas utilizando el diccionario. El DataFrame resultante contiene los datos de entrada en un formato adecuado para realizar predicciones.'''
class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
