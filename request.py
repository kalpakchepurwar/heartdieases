import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':30, 'gender':1, 'chestpain':2,'restbps':100, 'chol':90, 'fbs':120})

print(r.json())