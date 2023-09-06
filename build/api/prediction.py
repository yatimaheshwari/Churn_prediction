import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OrdinalEncoder
# from sklearn.preprocessing import StandardScaler
import pickle


df = pd.read_excel(r'Churn Prediction\build\api\customer_churn_large_dataset.xlsx')

# print(df.head(2))
X =df.drop(['Churn','Name','CustomerID'],axis=1)
Y = df['Churn']


X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.2,random_state=7)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

label_encoder = preprocessing.LabelEncoder()

X_train['Gender']= label_encoder.fit_transform(X_train['Gender'])
X_test['Gender'] = label_encoder.transform(X_test['Gender'])


X_train['Location']= label_encoder.fit_transform(X_train['Location'])
X_test['Location'] = label_encoder.transform(X_test['Location'])
print(X_test)
print(X_test.info())
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
scaled_train_data = scale.fit_transform(X_train)

scaled_test_data = scale.transform(X_test)
print(X_test)
print(X_test.info())

# Bulding the Model
RFClassifier = RandomForestClassifier(random_state=0)
# Training the Model
RFClassifier.fit(X_train, y_train)
RFClassifier.fit(scaled_train_data, y_train)

RFClassifier.predict([[35,1,4,12,50.0,90]])
# RFClassifier.predict({'Age':35,'Gender':1,'Location':4,'Subscription_Length_Months':12,'Monthly_Bill':50.0,'Total_Usage_GB': 90})

# Specify the file path where you want to save the .pkl file
model_filename = 'prediction.pkl'

# Save the trained model to a .pkl file
# with open(model_filename, 'wb') as file:
#     pickle.dump(RFClassifier, file)

# pickle.dump(RFClassifier,open('prediction.pkl','wb'))