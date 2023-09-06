import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<username>')
def hello(username):
    return f'Hello!!!!  {username}'

@app.route('/prediction', methods = ['POST'])
def prediction():
    print("Hello")
    print(request.form.get('gender'))
    try:
        Age = request.form.get('age')
        Gender = request.form.get('gender')
        Location = request.form.get('location')
        Subscription_Length_Months = request.form.get('subscription_Length_Months')
        Monthly_Bill = request.form.get('monthly_bill')
        Total_Usage_GB = request.form.get('total_usage_gb')
        if Gender == "Female":
            Gender = 0
        elif Gender == "Male":
            Gender = 1
        if Location == "Chicago":
            Location = 0
        elif Location == "Houston":
            Location = 1
        elif Location == "Los Angeles":
            Location = 2
        elif Location == "Miami":
            Location = 3
        elif Location == "New York":
            Location = 4

        model = pickle.load(open('prediction.pkl','rb'))
        print("foobar")
        test = model.predict([[Age,Gender,Location,Subscription_Length_Months,Monthly_Bill,Total_Usage_GB]])
        print(test[0])
        if test == 1:
            return 'Churn is 1'
        elif test == 0:
            return 'Churn is 0'
        else :
            return 'Internal Error'
    except Exception as err:
        return " Give error ",err

    
if __name__ == "__main__":
    app.run(debug=True)

    