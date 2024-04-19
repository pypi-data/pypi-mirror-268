import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from pandas.api.types import CategoricalDtype



class AdaBoostClassifier_C2V2(AdaBoostClassifier):
    """algorithm: default=SAMME
    """
    def __init__(self,
                 estimator=None,
                 n_estimators=50,
                 learning_rate=1.,
                 algorithm='SAMME',
                 random_state=None,
                 cost=[]):

        super().__init__(
            estimator=estimator,
            n_estimators=n_estimators,
            learning_rate=learning_rate,
            random_state=random_state,
            algorithm=algorithm)

        self.cost = cost

    def _boost_discrete(self, iboost, X, y, sample_weight, random_state):
        """Implement a single boost using the SAMME discrete algorithm."""

        # indexes = np.unique(y, return_index = True)[1]
        # temp2 = y[np.sort(indexes)]
        temp = np.unique(y, return_counts=True)[1]
        order = np.argsort(temp)[::-1]
        # order=y.value_counts().index
        change_cost = np.array(y).astype(float)
        for i in range(len(y)):
            for j in range(len(order)):
                if change_cost[i] == order[j]:
                    change_cost[i] = self.cost[j]
        # for i in range(len(y)):
        #    if change_cost[i]==0.0:
        #        change_cost[i]=self.cost[0]
        #    elif change_cost[i]==1.0:
        #        change_cost[i]=self.cost[1]
        #    else:
        #        change_cost[i]=self.cost[2]

        estimator = self._make_estimator(random_state=random_state)

        estimator.fit(X, y, sample_weight=sample_weight)

        y_predict = estimator.predict(X)

        if iboost == 0:
            self.classes_ = getattr(estimator, 'classes_', None)
            self.n_classes_ = len(self.classes_)

        # Instances incorrectly classified
        incorrect = y_predict != y

        # Error fraction
        estimator_error = np.mean(
            np.average(incorrect, weights=sample_weight, axis=0))

        # Stop if classification is perfect
        if estimator_error <= 0:
            return sample_weight, 1., 0.

        n_classes = self.n_classes_

        # Stop if the error is at least as bad as random guessing
        if estimator_error >= 1. - (1. / n_classes):
            self.estimators_.pop(-1)
            if len(self.estimators_) == 0:
                raise ValueError('BaseClassifier in AdaBoostClassifier '
                                 'ensemble is worse than random, ensemble '
                                 'can not be fit.')
            return None, None, None

        # Boost weight using multi-class AdaBoost SAMME alg
        estimator_weight = self.learning_rate * (
                np.log((1. - estimator_error) / estimator_error) +
                np.log(n_classes - 1.))

        # Only boost the weights if I will fit again
        if not iboost == self.n_estimators - 1:
            # Only boost positive weights
            sample_weight *= np.multiply(change_cost, np.exp(estimator_weight * incorrect *
                                                             ((sample_weight > 0) |
                                                              (estimator_weight < 0))))
            # for i in range(len(y)):
            #    if sample_weight[i]<0.00000005:
            #        sample_weight[i]=0.00000005
            #    else:
            #        sample_weight[i]=sample_weight[i]

        return sample_weight, estimator_weight, estimator_error

