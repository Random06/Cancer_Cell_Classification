

import pickle
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snss

df = pd.read_csv("data.csv")
df.head(7)

df.shape

# Count of number of empty(NaN,NAN) values in each column
df.isna().sum()

# Get a count of the number of Malignant (M)(Cancer) or Benign (B)(Cancer free) cell
df['diagnosis'].value_counts()

# Visualize the count
sns.countplot(df['diagnosis'], label='count')

# Look at the data types to see which columns need to be encoded
df.dtypes

# Encode the categorical data values
labelencoder_Y = LabelEncoder()
df.iloc[:, 1] = labelencoder_Y.fit_transform(df.iloc[:, 1].values)
# 1 ==> M , 0 ==> B

# Create a pair plot
sns.pairplot(df.iloc[:, 1:5], hue="diagnosis")

df.head()

# Get the correlation of the columns
df.iloc[:, 1:12].corr()

# Visualize the correlation
plt.figure(figsize=(10, 10))  # to expand each cell
# annot gives us the value  , fmt convert those values into percentage.
sns.heatmap(df.iloc[:, 1:12].corr(), annot=True, fmt=".0%")

# Split the dataset into independent (X) and dependent (Y)(which we have predict) datasets
# Here training data is independent data and testing data is dependent where X=independent Y= dependent
# X ==> feature data or independent data
# Y ==> predicting data or dependent data

X = df.iloc[:, 2:31].values  # values is used to convert then into an array
Y = df.iloc[:, 1].values  # Predicting array (Diagnosis)

print(type(X))
print(type(Y))
print(X.shape)
print(Y.shape)
X

# Split the dataset into 75% training and 25% testing

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=0)
X_test
X_train

# Create a function for the models


def models(X_train, Y_train):

    # Logistic Regression

    from sklearn.linear_model import LogisticRegression
    log = LogisticRegression(random_state=0)
    log.fit(X_train, Y_train)

    # Decision Tree Classifier

    from sklearn.tree import DecisionTreeClassifier
    tree = DecisionTreeClassifier(criterion="entropy", random_state=0)
    tree.fit(X_train, Y_train)

    # Random Forest Classifier

    from sklearn.ensemble import RandomForestClassifier
    forest = RandomForestClassifier(
        n_estimators=10, criterion="entropy", random_state=0)
    forest.fit(X_train, Y_train)

    # Print the models accuracy on the training data

    print('[0] Logistic Regression Training Accuracy : ',
          log.score(X_train, Y_train))
    print('[1] Decision Tree Classifier Training Accuracy : ',
          tree.score(X_train, Y_train))
    print('[2] Random Forest Classifier Training Accuracy : ',
          forest.score(X_train, Y_train))

    return log, tree, forest


# Getting all the models
model = models(X_train, Y_train)


for i in range(len(model)):
    print("Model ", i)

    cm = confusion_matrix(Y_test, model[i].predict(X_test))
    # [[true_negative , false_postive] [false_negative,true_positive]]
    TP = cm[1][1]
    TN = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]

    print(cm)
    print("Testing Accuracy =  ", (TP + TN)/(TP + TN + FN + FP))
    print()

# Show another way to get metrices of the models


for i in range(len(model)):
    print("Model ", i)
    print(classification_report(Y_test, model[i].predict(X_test)))
    print(accuracy_score(Y_test, model[i].predict(X_test)))
    print()

X_test

# Print the prediction of Random Forest Classifier Model

pred = model[2].predict(X_test)
print(pred)
print()
print(Y_test)


def SaveModel():
    import pickle
    with open("BreastCancer", "wb") as f:
        pickle.dump(model[2], f)


SaveModel()

with open("BreastCancer", "rb") as f:
    randomForest = pickle.load(f)

pred = randomForest.predict(X_test)
print(pred)
print()
print(Y_test)

inputsa = [9.742, 19.12, 61.93, 289.7, 0.1075, 0.08333, 0.008934, 0.01967, 0.2538, 0.07029, 0.6965, 1.747, 4.607, 43.52,
           0.01307, 0.01885, 0.006021, 0.01052, 0.031, 0.004225, 11.21, 23.17, 71.79, 380.9, 0.1398, 0.1352, 0.02085, 0.04589, 0.3196]
inputsa1 = [9.504, 12.44, 60.34, 273.9, 0.1024, 0.06492, 0.02956, 0.02076, 0.1815, 0.06905, 0.2773, 0.9768, 1.909, 15.7,
            0.009606, 0.01432, 0.01985, 0.01421, 0.02027, 0.002968, 10.23, 15.26, 65.13, 314.9, 0.1324, 0.1148, 0.08867, 0.06227, 0.245]
inputsa2 = [20.29, 14.34, 135.1, 1297, 0.1003, 0.1328, 0.198, 0.1043, 0.1809, 0.05883, 0.7572, 0.7813, 5.438, 94.44, 0.01149, 0.02461, 0.05688, 0.01885, 0.01756, 0.005115, 22.54, 16.67, 152.2, 1575, 0.1374, 0.205, 0.4, 0.1625, 0.2364
            ]

model[2].predict([inputsa2])
