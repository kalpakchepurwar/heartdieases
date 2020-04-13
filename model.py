# Importing the libraries
import numpy as np
import pandas as pd
import pickle

dataset = pd.read_csv('heart_final.csv')



X = dataset.drop(['target'],axis=1)
y = dataset['target']


from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression(max_iter=1000)


regressor.fit(X, y)



pickle.dump(regressor, open('model.pkl','wb'))



model = pickle.load(open('model.pkl','rb'))
print(model.predict([[30,1,2,100,90,1]]))