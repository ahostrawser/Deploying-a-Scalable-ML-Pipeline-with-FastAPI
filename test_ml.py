import pytest
# TODO: add necessary import
import pandas as pd

#test 1
from ml.model import train_model
from train_model import X_train, y_train
from sklearn.ensemble import RandomForestClassifier 

#test 2
from fastapi.testclient import TestClient
from main import app
# Instantiate the testing client
client = TestClient(app)

#test 3
import numpy as np
from ml.model import compute_model_metrics


# TODO: implement the first test. Change the function name and input as needed
def test_ML_algorithm():
    """
    # test that the ML model uses the expected algorithm
    """
    # Your code here
    #check that the size of the dataset is reasonable
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)
    #pass


# TODO: implement the second test. Change the function name and input as needed
def test_get_status_code():
    """
    # add description
    """
    # Your code here
    r = client.get("/")
    assert r.status_code == 200
    #pass

# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # add description for the third test
    """
    # Your code here
    y_true = np.array([1, 0, 1, 1])
    y_pred = np.array([1, 0, 0, 1])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    assert 0 < precision <= 1
    assert 0 < recall <=1
    assert 0 < fbeta <=1

    #pass
