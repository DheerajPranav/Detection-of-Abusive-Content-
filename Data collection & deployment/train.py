from joblib import dump, load
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from dataset import df
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv("dataset.csv")

Xtr = data.drop(columns =["Name " ,"Roll number","placement"])
ytr = data["placement"]

l=['Logistic Regression','LinearDiscriminantAnalysis','KNeighborsClassifier','Decision Tree Classifier','GaussianNB','SVC']
# prepare models
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('Decision Tree', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
print('-------------ACCURACY SCORE-----------------')
for name, model in models:
    model.fit(Xtr,ytr)
    y_pred_class = model.predict(Xtr)
    acc=metrics.accuracy_score(ytr, y_pred_class)
    results.append(acc)
    names.append(name)
    print('='*40)
    print("%s: %f" %(name, acc))
print('\n')
ind=results.index(max(results))
print(l[ind].upper(),'has highest accuracy:',max(results))
plt.title('Accuracy Comparison')
colors=['b','b','b','y','b','b']
plt.bar(names,results,color=colors)
plt.show()
plt.plot(names,results) 

plt.scatter(Xtr)

clf = DecisionTreeClassifier()
clf.fit(df.drop(columns = ["Name ","Roll number","placement"]),df["placement"])
dump(clf, "model.ml")