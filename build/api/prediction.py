import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import pickle


df = pd.read_excel(r'build\api\customer_churn_large_dataset.xlsx')

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

# Bulding the Model
RFClassifier = RandomForestClassifier(random_state=0)
# Training the Model
RFClassifier.fit(X_train, y_train)

# Specify the file path where you want to save the .pkl file
model_filename = 'prediction.pkl'

# Save the trained model to a .pkl file
with open(model_filename, 'wb') as file:
    pickle.dump(RFClassifier, file)
