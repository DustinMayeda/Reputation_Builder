from prepare_data import *

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor

gradient_classifier = GradientBoostingClassifier(subsample=.5, learning_rate=.0005)

X_class, y_class, vectorizer = classification_data()

gradient_classifier.fit(X_class, y_class)

gradient_regressor = GradientBoostingRegressor(subsample=.5, learning_rate=.0005)

X_reg, y_reg, vector = regression_data()

gradient_regressor.fit(X_reg, y_reg)

'''
for new data X will produce

gradient_classifier.predict_proba(X)[:, 1] * gradient_regressor(X)

'''
