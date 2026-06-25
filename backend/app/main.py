from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data_validation import input_validation
from model.model_prediction import model,predict_output,MODEL_VERSION
import pandas as pd


app = FastAPI()

@app.get('/')
def home():
    return {"Hey":"Welcome Greetings.Yours Students Performance Prediction API"}

@app.get('/health') # --->server side FACILITATION | will EXPLORE! 
def health_checker():
    return{
        'status':'Ok',
        'model_version':MODEL_VERSION,
        'model': model is not None        
    }

@app.post('/predict')
def prediction(uv:input_validation):

    
    inputs = pd.DataFrame([{
    'Hours Studied':uv.Hours_Studied,
    'Previous Scores':uv.Previous_Scores,
    'Extracurricular Activities':uv.Extracurricular_Activities.title(),
    'Sleep Hours':uv.Sleep_Hours,
    'Sample Question Papers Practiced':uv.Sample_Question_Papers_Practiced
    }])
    try:
        pred = predict_output(inputs)
        return JSONResponse(status_code=201,content={'Grade':pred})
    
    except Exception as e:
        return JSONResponse(status_code=500,content={'Error':str(e)})