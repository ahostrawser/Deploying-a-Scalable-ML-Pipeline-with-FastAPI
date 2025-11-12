# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Anna Hostrawser created the model. It is Random Forest Classifier using the default hyperparameters in scikit-learn 1.7.2.

## Intended Use
This model is intended to be used in the context of this udacity course. This model should be used to predict if the income of individuals exceeds $50K/yr based on census data.

## Training Data
The data was obtained from the UCI Machine Learning Repository (https://archive.ics.uci.edu/dataset/20/census+income). 

The original data set has 48842 rows, and a 80-20 split was used to break this into a train and test set. 

## Evaluation Data
A 80-20 split was used to break this into a train and test set.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The model was evaluated using F1 score. The value is 0.6790.
Precision: 0.7362 | Recall: 0.6300 | F1: 0.6790

## Ethical Considerations


## Caveats and Recommendations
