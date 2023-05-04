# -*- coding: utf-8 -*-
"""Naive_Bayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NUWaX60WpIg_X0bDG3XsgXFiZ-9-I4Yy

# Naive Bayes Classifier

## 1. Importing the required libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, LeaveOneOut
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import CategoricalNB
# %matplotlib inline

"""## 2. For Iris Dataset"""

# Reading the dataset into a pandas dataframe
iris_data = pd.read_csv("Iris.csv", index_col=0)
iris_data

# Plotting to view the number of tuples of each class
sns.countplot(x="Species", data=iris_data);

"""### As the parameters are numerical, GaussianNB is used

#### For data split as 90 : 10
"""

np.random.seed(42)
X = iris_data.drop("Species", axis=1)
y = iris_data["Species"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=125)
clf = GaussianNB()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)

"""#### For the data split as 70 : 30"""

np.random.seed(42)
X = iris_data.drop("Species", axis=1)
y = iris_data["Species"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=125)
clf = GaussianNB()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)

"""#### For Leave one out"""

scores = []
np.random.seed(42)
loo = LeaveOneOut()
for i, (train_idx, test_idx) in enumerate(loo.split(X, y=y)):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    scores.append(clf.score(X_test, y_test))
scores = pd.DataFrame(scores)
scores.rename(columns={"0": "scores"}, inplace=True)
scores.columns = ["scores"]
score_0 = len(scores[scores["scores"] == 0.0])
score_1 = len(scores[scores["scores"] == 1.0])
print("Probability of not predicting accurately: ", (score_0/(score_1 + score_0))*100)
print("Probability of predicting accurately: ", (score_1/(score_1 + score_0))*100)
sns.countplot(x="scores", data=scores);

"""## 3. For Titanic Dataset"""

# Reading the file into a pandas dataframe
titanic_data = pd.read_csv("Titanic-Dataset.csv", index_col=0)
temp = pd.read_csv("titanic.csv", index_col=0)
titanic_data = pd.concat([titanic_data, temp])
titanic_data

titanic_data.drop("Name", axis=1, inplace=True)
titanic_data

titanic_data.drop("Ticket", axis=1, inplace=True)
titanic_data

titanic_data.isnull().sum()

titanic_data["Age"].fillna(value=titanic_data["Age"].mean(), inplace=True)
titanic_data.isnull().sum()

titanic_data.dtypes

titanic_data["Cabin"].loc[~titanic_data["Cabin"].isnull()] = "Yes"
titanic_data["Cabin"].loc[titanic_data["Cabin"].isnull()] = "No"
titanic_data.isnull().sum()

titanic_data

titanic_data.dropna(axis=0, inplace=True)
titanic_data.isnull().sum()

titanic_data

"""### Use CategoricalNB for categorical values and GaussianNB for Gaussian values"""

new_titanic_data_2 = titanic_data
new_titanic_data_2

new_titanic_data_2 = pd.get_dummies(new_titanic_data_2, columns=["Pclass", "Sex", "Cabin", "Embarked"])
new_titanic_data_2

"""#### For 70 : 30 split"""

cat_X = new_titanic_data_2.drop("Age", axis=1)
cat_X.drop("SibSp", axis=1, inplace=True)
cat_X.drop("Parch", axis=1, inplace=True)
cat_X.drop("Fare", axis=1, inplace=True)
cat_X.drop("Survived", axis=1, inplace=True)
gaus_X = pd.concat([new_titanic_data_2["Age"], new_titanic_data_2["Parch"], new_titanic_data_2["Fare"], new_titanic_data_2["SibSp"]], axis=1, ignore_index=True)
y = new_titanic_data_2["Survived"]
cat_X_train, cat_X_test, gaus_X_train, gaus_X_test, y_train, y_test = train_test_split(cat_X, gaus_X, y, test_size=0.3, random_state=75)
clf1 = CategoricalNB()
clf1.fit(cat_X_train, y_train)
clf2 = GaussianNB()
clf2.fit(gaus_X_train, y_train)
cat_score = clf1.score(cat_X_test, y_test)
gaus_score = clf2.score(gaus_X_test, y_test)
print("Total Score = ", cat_score * gaus_score)

"""#### For 90 : 10 split"""

cat_X = new_titanic_data_2.drop("Age", axis=1)
cat_X.drop("SibSp", axis=1, inplace=True)
cat_X.drop("Parch", axis=1, inplace=True)
cat_X.drop("Fare", axis=1, inplace=True)
cat_X.drop("Survived", axis=1, inplace=True)
gaus_X = pd.concat([new_titanic_data_2["Age"], new_titanic_data_2["Parch"], new_titanic_data_2["Fare"], new_titanic_data_2["SibSp"]], axis=1, ignore_index=True)
y = new_titanic_data_2["Survived"]
cat_X_train, cat_X_test, gaus_X_train, gaus_X_test, y_train, y_test = train_test_split(cat_X, gaus_X, y, test_size=0.1, random_state=75)
clf1 = CategoricalNB()
clf1.fit(cat_X_train, y_train)
clf2 = GaussianNB()
clf2.fit(gaus_X_train, y_train)
cat_score = clf1.score(cat_X_test, y_test)
gaus_score = clf2.score(gaus_X_test, y_test)
print("Total Score = ", cat_score * gaus_score)

"""#### For LeaveOneOut"""

cat_X = new_titanic_data_2.drop("Age", axis=1)
cat_X.drop("SibSp", axis=1, inplace=True)
cat_X.drop("Parch", axis=1, inplace=True)
cat_X.drop("Fare", axis=1, inplace=True)
cat_X.drop("Survived", axis=1, inplace=True)
gaus_X = pd.concat([new_titanic_data_2["Age"], new_titanic_data_2["Parch"], new_titanic_data_2["Fare"], new_titanic_data_2["SibSp"]], axis=1, ignore_index=True)
y = new_titanic_data_2["Survived"]
cat_X_train, cat_X_test, gaus_X_train, gaus_X_test, y_train, y_test = train_test_split(cat_X, gaus_X, y, test_size=0.3, random_state=75)
cat_scores = []
np.random.seed(42)
loo = LeaveOneOut()
for i, (train_idx, test_idx) in enumerate(loo.split(cat_X, y=y)):
    X_train, X_test = cat_X.iloc[train_idx], cat_X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    clf = CategoricalNB()
    clf.fit(X_train, y_train)
    cat_scores.append(clf.score(X_test, y_test))
gaus_scores = []
for i, (train_idx, test_idx) in enumerate(loo.split(gaus_X, y=y)):
    X_train, X_test = gaus_X.iloc[train_idx], gaus_X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    gaus_scores.append(clf.score(X_test, y_test))
scores = []
for i in range(len(cat_scores)):
    scores.append(cat_scores[i] * gaus_scores[i])
scores = pd.DataFrame(scores)
scores.rename(columns={"0": "scores"}, inplace=True)
scores.columns = ["scores"]
score_0 = len(scores[scores["scores"] == 0.0])
score_1 = len(scores[scores["scores"] == 1.0])
print("Probability of not predicting accurately: ", (score_0/(score_1 + score_0))*100)
print("Probability of predicting accurately: ", (score_1/(score_1 + score_0))*100)
sns.countplot(x="scores", data=scores);
