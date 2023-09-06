
# Churn Prediction using Machine Learning

Introduction

Customer churn (also known as customer attrition) occurs when a customer stops using a company's products or services.

Customer churn affects profitability, especially in industries where revenues are heavily dependent on subscriptions (e.g. banks, telephone and internet service providers, pay-TV companies, insurance firms, etc.). It is estimated that acquiring a new customer can cost up to five times more than retaining an existing one.

Therefore, customer churn analysis is essential as it can help a business:
- Identify problems in its services (e.g. poor quality product/service, poor customer support, wrong target audience, etc.), and
- Make correct strategic decisions that would lead to higher customer satisfaction and consequently higher customer retention.







## Installation

1) Install python and pip on your system

2) Download the trained model pickel object from mega link -

[Mega Download - prediction.pkl](https://mega.nz/file/ZOlj1J5S#myJ6PXqv2yGZQLyfXmlB5pTTpTFth2bDGuokPE0wf9A)
 

## Run Locally

Clone the project

```bash
  git clone https://github.com/yatimaheshwari/Churn_prediction.git
```

Copy the downloaded pickel file from installation step into the project at directory

```
\Churn_prediction\build\api\
```

Go to the project directory

```bash
  cd \Churn_prediction\build\api\server.py
```

Install dependencies

```bash
  pip install pickle
  pip install flask
  pip install numpy
  pip install pandas
```

Start the server

```python
  python server.py
```


## Usage/Examples

1) Open \build\api\server.py
2) Run this file with python
3) On the html page enter the values and then click Get Churn Prediction button
4) An api call will be made and prediction according to the entered data will be displayed on screen


## Tech Stack

**Client:** HTML

**Server:** Python/Flask

**Libraries:** Pickle, numpy, pandas, sklearn, matplotlib

**ML Algorithms:** RandomForest, LogisticRegression, xgboost, RandomizedSearchCV


## Roadmap

- Enrich UI with CSS for a better reporting

- Improve model accuracy and performance


## Authors

- [@yati.maheshwari](https://github.com/yatimaheshwari)

