#CS 412 Homework 4 Submission Stub
#First_Name: Zongxian Last_Name: Feng


import numpy as np
import random
import math
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
def get_splits(n, k):
    # n个item， 分成k组
    array = np.arange(n)
    np.random.shuffle(array)
    splited = np.array_split(array, k)
    to_return = []
    for arr in splited:
        to_return.append(arr.tolist())
    return to_return


def my_cross_val(method, X, y, k):
    to_return = []
    index_list = get_splits(len(y), k)
    for i in range(len(index_list)):
        val_set_indices = np.array(index_list[i])
        train_set = index_list[0:i] + index_list[i+1:len(index_list)]
        train_set_indices = np.array(sum(train_set, []))
        X_train = X[train_set_indices]
        y_train = y[train_set_indices]
        X_val = X[val_set_indices]
        y_val = y[val_set_indices]
        y_pred = None
        if method == 'LinearSVC':
            myLinearSVC = LinearSVC(max_iter=2000)
            myLinearSVC.fit(X_train, y_train)
            y_pred = myLinearSVC.predict(X_val)
        if method == 'SVC':
            mySVC = SVC(gamma='scale', C=10)
            mySVC.fit(X_train, y_train)
            y_pred = mySVC.predict(X_val)
        if method == 'LogisticRegression':
            myLR = LogisticRegression(penalty='l2', solver='lbfgs', multi_class='multinomial', max_iter=5000)
            myLR.fit(X_train, y_train)
            y_pred = myLR.predict(X_val)
        if method == 'RandomForestClassifier':
            myRF = RandomForestClassifier(max_depth=20, random_state=0, n_estimators=500)
            myRF.fit(X_train, y_train)
            y_pred = myRF.predict(X_val)
        if method == 'XGBClassifier':
            myXGB = XGBClassifier()
            myXGB.fit(X_train, y_train)
            y_pred = myXGB.predict(X_val)
        
        diff_arr = y_pred - y_val
        wrong_cnt = 0
        for e in diff_arr:
            if e != 0:
                wrong_cnt+=1
        err_rate = wrong_cnt / len(y_pred)
        to_return.append(err_rate)
    
    return np.array(to_return)
        
    

def my_train_test(method, X, y, pi, k):
    to_return = []
    for i in range(k):
        X_train, y_train, X_val, y_val = train_test_split(X, y, pi)
        y_pred = None
        if method == 'LinearSVC':
            myLinearSVC = LinearSVC(max_iter=2000)
            myLinearSVC.fit(X_train, y_train)
            y_pred = myLinearSVC.predict(X_val)
        if method == 'SVC':
            mySVC = SVC(gamma='scale', C=10)
            mySVC.fit(X_train, y_train)
            y_pred = mySVC.predict(X_val)
        if method == 'LogisticRegression':
            myLR = LogisticRegression(penalty='l2', solver='lbfgs', multi_class='multinomial', max_iter=5000)
            myLR.fit(X_train, y_train)
            y_pred = myLR.predict(X_val)
        if method == 'RandomForestClassifier':
            myRF = RandomForestClassifier(max_depth=20, random_state=0, n_estimators=500)
            myRF.fit(X_train, y_train)
            y_pred = myRF.predict(X_val)
        if method == 'XGBClassifier':
            myXGB = XGBClassifier()
            myXGB.fit(X_train, y_train)
            y_pred = myXGB.predict(X_val)
        diff_arr = y_pred - y_val
        wrong_cnt = 0
        for e in diff_arr:
            if e != 0:
                wrong_cnt+=1
        err_rate = wrong_cnt / len(y_pred)
        to_return.append(err_rate)
    
    return np.array(to_return)



def train_test_split(X, y, pi):
    total_len = len(y)
    train_len = round(total_len * pi)
    test_len = round(1 - total_len)
    indices = np.arange(total_len)
    np.random.shuffle(indices)
    X_shuffle = X[indices]
    y_shuffle = y[indices]
    X_train = X_shuffle[0:train_len]
    y_train = y_shuffle[0:train_len]
    X_test = X_shuffle[train_len:]
    y_test = y_shuffle[train_len:]
    return X_train, y_train, X_test, y_test

from sklearn.datasets import load_digits
digits = load_digits()
X, y = digits.data, digits.target
print(my_train_test('SVC', X, y, 0.8, 10))