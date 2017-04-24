from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn.grid_search import RandomizedSearchCV
from scipy.stats import randint as sp_randint
import pydot
import StringIO
import numpy as np
from tempfile import NamedTemporaryFile

rain = .1 * np.load('rain.npy')
rain[rain < 0] = .05/2
dates = np.load('doy.npy').astype(int)
x = np.vstack((dates[:-1], np.sign(rain[:-1])))
x = x.T

y = np.sign(rain[1:])

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=37)

clf = tree.DecisionTreeClassifier(random_state=37)
params = {"max_depth": [2, None],
              "min_samples_leaf": sp_randint(1, 5),
              "criterion": ["gini", "entropy"]}
rscv = RandomizedSearchCV(clf, params)
rscv.fit(x_train,y_train)

sio = StringIO.StringIO()
tree.export_graphviz(rscv.best_estimator_, out_file=sio, feature_names=['day-of-year','yest'])
dec_tree = pydot.graph_from_dot_data(sio.getvalue())

with NamedTemporaryFile(prefix='rain', suffix='.png', delete=False) as f:
    dec_tree.write_png(f.name)
    print "Written figure to", f.name

print "Best Train Score", rscv.best_score_
print "Test Score", rscv.score(x_test, y_test)
print "Best params", rscv.best_params_
