from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from matplotlib import pyplot as plt
from sklearn.svm import SVC
import numpy as np
from load_data import loadCSVfile

features = loadCSVfile('traindata.csv', 'float')
target = np.ravel(loadCSVfile('trainlabel.csv', 'float'))

# # Normalization
# # Subtract the mean for each feature
features -= np.mean(features, axis=0)
# # # Divide each feature by its standard deviation
features /= np.std(features, axis=0)

# Cross Validation
folds = 10
kf = KFold(n=len(target), n_folds=folds, shuffle=False)
cv = 0
mean_error = 0
for tr, tst in kf:
    # Train Test Split
    tr_features = features[tr, :]
    tr_target = target[tr]

    tst_features = features[tst, :]
    tst_target = target[tst]

    # Training SVM Model
    model = SVC(kernel='rbf')
    model.fit(tr_features, tr_target)
    # Measuring training and test accuracy
    tr_accuracy = np.mean(model.predict(tr_features) == tr_target)
    tst_accuracy = np.mean(model.predict(tst_features) == tst_target)
    mean_error = mean_error + tst_accuracy
    print("%d Fold Train Accuracy:%f, Test Accuracy:%f" % (cv, tr_accuracy, tst_accuracy))
    cv += 1

mean_error = mean_error / folds
print("SVM %s folds CV with accuracy: %s\n" % (folds, mean_error))








