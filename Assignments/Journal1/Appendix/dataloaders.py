import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import make_moons
from sklearn.datasets import load_iris
from sklearn.datasets import fetch_openml
from libitmal import utils as itmalutils
from sklearn.base import BaseEstimator
import pandas as pd
from sklearn.base import ClassifierMixin
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix

######################################################################################################
# 
# FUNCTIONS
#
######################################################################################################

# 
# MOON
#
def MOON_GetDataSet(n_samples):
    return make_moons(n_samples, noise = 0.1)

def MOON_Plot(X, y,title="my_title", xlabel="x_label", ylabel="y_label"):
    plt.figure(figsize=(8,6))
    plt.scatter(X[:, 0], X[:, 1], marker='o', c=y, s=25, edgecolor='k')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)  
    
# 
# MNIST
#
def MNIST_PlotDigit(data):
    # TODO: add plot functionality for a single digit...
    image = data.reshape(28, 28)
    plt.imshow(255-image, cmap='gray')
    plt.title('Plot of Single Digit')  


def MNIST_GetDataSet():
    # TODO: use mnist = fetch_mldata('MNIST original') or mnist.load_data(),
    #       but return as a single X-y tuple 
    X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
    return (X, y)

# 
# IRIS
#
def IRIS_GetDataSet():
    return load_iris()


def IRIS_Plot2D(iris_data, features=2, feat1=None, feat2=None, ax=None):
    # Check for Subplots
    if ax is None:
        ax = plt.gca()
        
    # Retrieve IRIS data with amount of features
    X = iris_data.data[:, :features]
    y = iris_data.target
    
    # Set and return IRIS data with setosa, versicolor and virginica
    # feat1 & feat2: 0 = Sepal.Length, 1 = Sepal.Width, 2 = Petal.Length, 3 = Petal.Width
    setosa = ax.scatter(X[:50,feat1], X[:50,feat2], c='red', label='setosa', marker='o')
    versicolor = ax.scatter(X[50:100,feat1], X[50:100,feat2], c="green", label = 'versicolor', marker='o')
    virginica = ax.scatter(X[100:,feat1], X[100:,feat2], c="blue", label ='virginica', marker='o')
    
    return setosa, versicolor, virginica

#
#  PATH OF EXILE HARBINGER DATASET
#
def GetOrderedClassInLadder(ladder):
    # Pre-loading
    df = pd.read_csv('poe_stats.csv', delimiter = ',')
    df_ladder = df.groupby('ladder')
    df_ladder.size()
    
    # Get Ladder Class grouped by class
    mLadder = df_ladder.get_group(ladder).groupby('class')
    
    # Arrange Ordered data by Class and Number of classes
    mOrderedData = pd.DataFrame(0, index=np.arange(len(mLadder.size())), columns=['class','number'])
    mOrderedData['class'] = mLadder.size().index
    
    # Loop through all data and sort class with number of classes
    for i in range(len(mOrderedData)):
        mOrderedData.iat[i,1] =  int(mLadder.size()[i])
    mOrderedData = mOrderedData.sort_values(by = 'number', ascending=False)
    return mOrderedData


#
#  DUMMY_CLASSIFIER
#
class DummyClassifier(BaseEstimator):
    def fit(self, X, y=None):
        pass
    def predict(self, X):
        return np.zeros((len(X),1), dtype=bool)

# 
# Function that plots text in the center of the graph
#
def PlotTextCenter(str, ax=None):
    # Check for subplots
    if ax is None:
        ax = plt.gca()
        
    # Disable x- and y-axis number ticks
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    
    return ax.text(0.5, 0.5, str, horizontalalignment='center',verticalalignment='center')