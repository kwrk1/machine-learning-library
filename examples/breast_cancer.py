# Example for classification

# allows import from different folder
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import pandas as pd
import numpy as np
from pylearn import GaussianNaiveBayes

# Due to the short training duration, this example doesn't store and load the trained model and retraines every execution

data = pd.read_csv("examples/data/breast_cancer_data.csv")

x_train, x_test = pd.DataFrame(data.iloc[:, :5]), pd.DataFrame(data.iloc[:25, :5])
y_train, y_test = pd.DataFrame(data.iloc[:, -1]), pd.DataFrame(data.iloc[:25, -1])

nb = GaussianNaiveBayes()
nb.fit(x_train, y_train)  
prediction = nb.predict(x_test)
def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

print("Gaussian Naive Bayes accuracy:", accuracy(np.array(y_test), np.array(prediction)))      # relatively low accuracy
print()

prediction = pd.DataFrame(prediction)
prediction.columns = ["prediction"]
result = [x_test, y_test, prediction]
result = pd.concat([df for df in result], axis=1)
print(result)



