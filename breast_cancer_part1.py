# -*- coding: utf-8 -*-
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
plt.style.use('ggplot')

data = load_breast_cancer()
print(data.feature_names)
print(data.target_names)

df = pd.read_csv('data.csv')
df.head()

df.info()

df.drop(df.columns[[-1, 0]], axis=1, inplace=True)
df.info()

print("Total number of diagnosis are ", str(df.shape[0]), ", ", df.diagnosis.value_counts()['B'], "Benign and Malignant are",
      df.diagnosis.value_counts()['M'])

df.describe()

featureMeans = list(df.columns[1:11])

correlationData = df[featureMeans].corr()
sns.pairplot(df[featureMeans].corr(), diag_kind='kde', size=2)

plt.figure(figsize=(10, 10))
sns.heatmap(df[featureMeans].corr(), annot=True, square=True, cmap='coolwarm')
plt.show()

bins = 12
plt.figure(figsize=(15, 15))
plt.subplot(3, 2, 1)
sns.distplot(df[df['diagnosis'] == 'M']['radius_mean'],
             bins=bins, color='green', label='M')
sns.distplot(df[df['diagnosis'] == 'B']['radius_mean'],
             bins=bins, color='red', label='B')
plt.legend(loc='upper right')
plt.subplot(3, 2, 2)
sns.distplot(df[df['diagnosis'] == 'M']['texture_mean'],
             bins=bins, color='green', label='M')
sns.distplot(df[df['diagnosis'] == 'B']['texture_mean'],
             bins=bins, color='red', label='B')
plt.legend(loc='upper right')
plt.subplot(3, 2, 3)
sns.distplot(df[df['diagnosis'] == 'M']['perimeter_mean'],
             bins=bins, color='green', label='M')
sns.distplot(df[df['diagnosis'] == 'B']['perimeter_mean'],
             bins=bins, color='red', label='B')
plt.legend(loc='upper right')
plt.subplot(3, 2, 4)
sns.distplot(df[df['diagnosis'] == 'M']['area_mean'],
             bins=bins, color='green', label='M')
sns.distplot(df[df['diagnosis'] == 'B']['area_mean'],
             bins=bins, color='red', label='B')
plt.legend(loc='upper right')
plt.subplot(3, 2, 5)
sns.distplot(df[df['diagnosis'] == 'M']['concavity_mean'],
             bins=bins, color='green', label='M')
sns.distplot(df[df['diagnosis'] == 'B']['concavity_mean'],
             bins=bins, color='red', label='B')
plt.legend(loc='upper right')
plt.subplot(3, 2, 6)
sns.distplot(df[df['diagnosis'] == 'M']['symmetry_mean'],
             bins=bins, color='green', label='M')
sns.distplot(df[df['diagnosis'] == 'B']['symmetry_mean'],
             bins=bins, color='red', label='B')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

X = df.loc[:, featureMeans]
y = df.loc[:, 'diagnosis']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


nbclf = GaussianNB().fit(X_train, y_train)
predicted = nbclf.predict(X_test)
print('naive_bayes Breast cancer dataset accuracy')
print('Accuracy of GaussianNB classifier on training set: {:.2f}'.format(
    nbclf.score(X_train, y_train)))
print('Accuracy of GaussianNB classifier on test set: {:.2f}'.format(
    nbclf.score(X_test, y_test)))


clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
prediction = clf.predict(X_test)

print('KNeighborsClassifier Breast cancer dataset Accuracy')
print('Accuracy of GaussianNB classifier on training set: {:.2f}'.format(
    clf.score(X_train, y_train)))
print('Accuracy of GaussianNB classifier on test set: {:.2f}'.format(
    clf.score(X_test, y_test)))
