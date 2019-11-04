from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import csv
import random
import numpy as np
random.seed(42)

def loadCsv(filename):
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset


def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]

def pandasLoad():
    df = pd.read_csv("pima-indians-diabetes.csv")
    data = df.values
    X = data[:,:-2]
    y = data[:,-1:]
    y = y.ravel()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test))

def natLoad():
    filename = 'pima-indians-diabetes.csv'
    splitRatio = 0.67
    dataset = loadCsv(filename)
    trainingSet, testSet = splitDataset(dataset, splitRatio)
    trainingSet, testSet = np.array(trainingSet), np.array(testSet)
    X_train, y_train, X_test, y_test =  trainingSet[:,:-1], trainingSet[:,-1:].ravel(), \
                                        testSet[:, :-1], testSet[:, -1:].ravel()

    clf = GaussianNB()
    clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test))

def LogLoad():
    filename = 'pima-indians-diabetes.csv'
    splitRatio = 0.67
    dataset = loadCsv(filename)
    trainingSet, testSet = splitDataset(dataset, splitRatio)
    trainingSet, testSet = np.array(trainingSet), np.array(testSet)
    X_train, y_train, X_test, y_test =  trainingSet[:,:-1], trainingSet[:,-1:].ravel(), \
                                        testSet[:, :-1], testSet[:, -1:].ravel()

    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test))

def TreeLoad():
    filename = 'pima-indians-diabetes.csv'
    splitRatio = 0.67
    dataset = loadCsv(filename)
    trainingSet, testSet = splitDataset(dataset, splitRatio)
    trainingSet, testSet = np.array(trainingSet), np.array(testSet)
    X_train, y_train, X_test, y_test =  trainingSet[:,:-1], trainingSet[:,-1:].ravel(), \
                                        testSet[:, :-1], testSet[:, -1:].ravel()

    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test))

def GradLoad():
    filename = 'pima-indians-diabetes.csv'
    splitRatio = 0.67
    dataset = loadCsv(filename)
    trainingSet, testSet = splitDataset(dataset, splitRatio)
    trainingSet, testSet = np.array(trainingSet), np.array(testSet)
    X_train, y_train, X_test, y_test =  trainingSet[:,:-1], trainingSet[:,-1:].ravel(), \
                                        testSet[:, :-1], testSet[:, -1:].ravel()

    clf = GradientBoostingClassifier()
    clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test))

if __name__ == "__main__":
    pandasLoad()
    natLoad()
    LogLoad()
    TreeLoad()
    GradLoad()



