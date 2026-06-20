import joblib
import os
import pandas as pd

MODEL_VERSION= '1.1.0'

model = joblib.load('model/pipeline.joblib')
# model = joblib.load(r'D:\APIs\FastAPI\mini-project\Backend\pipeline.joblib')
# with open('D:\APIs\FastAPI\mini-project\pipeline.joblib', "rb") as f:
#     model = joblib.load(f)

def predict_output(inputs):

    # data = pd.DataFrame([inputs])

    # return model.predict(inputs)

    pred = model.predict(inputs)
    return pred[0]