import joblib
import pandas as pd



def make_prediction(data:pd.DataFrame):
    label_encoders = joblib.load(filename="label_encoders.pkl")
    col = 'Internship_Experience'
    data[col] = label_encoders[col].transform(data[col])
    scaler = joblib.load(filename="scaler.pkl")
    column_names = list(data.columns)
    data = scaler.transform(data)
    data = pd.DataFrame(data=data, columns = column_names)
    
    # make prediction.
    model = joblib.load(filename="model.pkl")
    prediction = model.predict(data)
    
    return prediction[0]

if __name__ == "__main__":
    print('pass')
    
    
    