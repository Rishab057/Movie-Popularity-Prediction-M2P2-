import numpy
#import sklearn
from sklearn import linear_model
#from sklearn.naive_bayes import GaussianNB
#from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error
from sklearn import metrics


filename = 'X_Train.csv'

raw_data = open(filename, 'rt')

data = numpy.loadtxt(raw_data, delimiter=",")

#print(data)

X = data;

filename = 'Y_Train.csv'

raw_data = open(filename, 'rt')

Y = numpy.loadtxt(raw_data)

#Y = numpy.array([79,82,77,82,74,79,74,81,82,76]);


#               Logistic Regression
# =============================================================================
h = .02
logreg = linear_model.LogisticRegression(C=0.01)
logreg.fit(X, Y)
# =============================================================================

#gnb = GaussianNB()
#model = gnb.fit(X, Y)

#                       Linear Regression
# =============================================================================
# regr = linear_model.LinearRegression()
# regr.fit(X, Y)
# 
# =============================================================================

#                   Neural Networks
# =============================================================================
# clf = MLPClassifier(activation = 'logistic', solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
# clf.fit(X, Y)
# =============================================================================

filename = 'X_Test.csv'

raw_data = open(filename, 'rt')

prd = numpy.loadtxt(raw_data, delimiter=",")

#prd = numpy.array([[43,18.24062796330654,23,-8.995525383707204],[47,21.08194083694084,35,-12.45753968253968]]);

filename = 'Y_Test.csv'

raw_data = open(filename, 'rt')

y_test = numpy.loadtxt(raw_data)

#y_test = numpy.array([84,68]);
y_pred = logreg.predict(prd);
print("Ratings -> ",y_pred)
print("Score -> ", mean_squared_error(y_test, y_pred))

print("Mean absolute Error: ",metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared Error: ",metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error: ",numpy.sqrt(metrics.mean_squared_error(y_test, y_pred)))

#Mad max fury , 84(7.7) adn the witch = 6.8(7.4)