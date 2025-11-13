import pytest
# TODO: add necessary import
import pandas as pd

#for test 2
from ml.data import process_data, apply_label
from ml.model import train_model, compute_model_metrics, load_model
from train_model import data, train, test, X_train, y_train
from sklearn.ensemble import RandomForestClassifier 

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # add description for the first test
    """
    # Your code here
    #check that the size of the dataset is reasonable
    #pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # test that the ML model uses the expected algorithm
    """
    # Your code here
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)
    #pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
