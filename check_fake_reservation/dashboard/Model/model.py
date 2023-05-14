import pickle
import numpy as np

def model_predict(L):
    model = pickle.load(open('C:/Users/Administrator/Desktop/fake-reservation-check/fake-reservation-check-WEB/check_fake_reservation/dashboard/Model/ml_model.pkl','rb'))
    scaled = pickle.load(open('C:/Users/Administrator/Desktop/fake-reservation-check/fake-reservation-check-WEB/check_fake_reservation/dashboard/Model/scaler.pkl','rb'))
    
    L.append(1)
    d = np.array(L)

    # Reshape the input data to have 14 features
    x = d.reshape(1, -1)
    prediction  = model.predict(scaled.transform([
       d
    ]))

    if prediction == 0:
        return 'Fake'
    elif prediction ==1 :
        return 'True'
    else :
        return 'Error'
    