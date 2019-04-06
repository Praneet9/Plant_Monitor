import numpy as np 
import pickle as pb

supervised_dict = {
    1 : 'Healthy',
    0 : 'Not-Healthy'
}
unsupervised_dict = {
    1 : 'Not-Healthy',
    0 : 'Healthy'
}

global svc, rfc, standard_scaler, pca, kmeans

with open('./model/svc_sensor.pb', 'rb') as f:
    svc = pb.load(f)

with open('./model/rfc_sensor.pb', 'rb') as f:
    rfc = pb.load(f)

with open('./model/standard_scaler.pb', 'rb') as f:
    standard_scaler = pb.load(f)

with open('./model/pca_transform.pb', 'rb') as g:
    pca = pb.load(g)

with open('./model/kmeans_clustering.pb', 'rb') as h:
    kmeans = pb.load(h)


# Methods for prediction
def predict_svm(soil_moisture, humidity, temperature):
    prediction = svc.predict(X=[[soil_moisture, humidity, temperature]])
    return supervised_dict[prediction[0]]

def predict_rfc(soil_moisture, humidity, temperature):
    prediction = rfc.predict(X=[[soil_moisture, humidity, temperature]])
    return supervised_dict[prediction[0]]

def predict_kmeans(soil_moisture, humidity, temperature):
    scale = standard_scaler.transform(X=np.array([[soil_moisture, humidity, temperature]]))
    pca_op = pca.transform(scale)
    y = kmeans.predict(pca_op)
    return unsupervised_dict[y[0]]