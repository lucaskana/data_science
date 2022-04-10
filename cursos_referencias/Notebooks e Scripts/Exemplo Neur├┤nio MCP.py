import sklearn.datasets
import numpy as np
import pandas as pd
from sklearn import metrics 


class MPNeuron:
  
  def __init__(self):
    self.b = None
    
  def model(self, x):
    return(sum(x) >= self.b)
  
  def predict(self, X):
    Y = []
    for x in X:
      result = self.model(x)
      Y.append(result)
    return np.array(Y)
  
  def fit(self, X, Y):
    accuracy = {}
    
    for b in range(X.shape[1] + 1):
      self.b = b
      Y_pred = self.predict(X)
      accuracy[b] = metrics.accuracy_score(Y_pred, Y)
      
    best_b = max(accuracy, key = accuracy.get)
    self.b = best_b
    
    print('Optimal value of b is', best_b)
    print('Highest accuracy is', accuracy[best_b])

breast_cancer = sklearn.datasets.load_breast_cancer()
X = breast_cancer.data
Y = breast_cancer.target

#Converting the data to Pandas dataframe
data = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
data['class'] = breast_cancer.target
data.head()

from sklearn.model_selection import train_test_split
X = data.drop('class', axis=1)
Y = data['class']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify = Y)
#converting the input features to a binary format
X_binarised_train = X_train.apply(pd.cut, bins=2, labels=[1,0])
X_binarised_test = X_test.apply(pd.cut, bins=2, labels=[1,0])


mp_neuron = MPNeuron()
#Calling the fit method inside the class on the training data
mp_neuron.fit(X_binarised_train.values, Y_train)

#testing the model on the test data.
Y_test_pred = mp_neuron.predict(X_binarised_test)
accuracy_test = metrics.accuracy_score(Y_test_pred, Y_test)

#print the accuracy of the test data
print(accuracy_test)