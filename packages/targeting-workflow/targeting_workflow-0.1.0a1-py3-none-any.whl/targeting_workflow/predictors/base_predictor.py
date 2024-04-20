#  Copyright (c) 2024 Mira Geoscience Ltd.
#
#  This file is part of targeting_workflow package.
#
#  All rights reserved.
#
#  The software and information contained herein are proprietary to, and
#  comprise valuable trade secrets of, Mira Geoscience, which
#  intend to preserve as trade secrets such software and information.
#  This software is furnished pursuant to a written license agreement and
#  may be used, copied, transmitted, and stored only in accordance with
#  the terms of such license and with the inclusion of the above copyright
#  notice.  This software and information or any other copies thereof may
#  not be provided or otherwise made available to any other person.
#
# pylint: disable=import-error


from __future__ import annotations

from warnings import warn

import numpy as np
import pandas as pd
from sklearn.inspection import permutation_importance
from sklearn.metrics import confusion_matrix, roc_curve
from sklearn.model_selection import GridSearchCV, GroupKFold, RandomizedSearchCV

from ..database.database import Database
from ..shared.base_compute import BaseCompute


class BasePredictor(BaseCompute):
    def __init__(self, database: Database, inputs: list | str, **kwargs):
        """
        Base class for feature computation.

        :param database: The database containing the data to use.
        :param inputs: The inputs to use.
        :param kwargs: The BaseCompute kwargs. .
        """
        self._target: pd.Series | None = None
        self._predict: pd.DataFrame | None = None
        self._probability: pd.DataFrame | None = None
        self._k_fold: pd.Series | None = None
        self._cv_strategy: GroupKFold | None = None

        self._score: float | None = None

        # todo: should we keep the figures values in memory?
        self._feature_importance: pd.DataFrame | None = None
        self._confusion_matrix: np.ndarray | None = None
        self._best_parameters: dict | None = None

        super().__init__(database, inputs, **kwargs)

    def reset(self):
        """
        Reset the feature.
        """
        self._score = None
        self._predict = None
        self._probability = None
        self.fitted = False
        self._feature_importance = None
        self._confusion_matrix = None
        self._best_parameters = None

    @property
    def train_index(self) -> pd.Index:
        """
        Return the training index.
        """
        return self.inputs.index.intersection(self.database.train)

    @property
    def train_data(self) -> pd.DataFrame:
        """
        Return the training data.
        """
        return self.inputs.loc[self.train_index]

    @property
    def test_index(self) -> pd.Index:
        """
        Return the testing index.
        """
        return self.inputs.index.intersection(self.database.test)

    @property
    def test_data(self) -> pd.DataFrame:
        """
        Return the testing data.
        """
        return self.inputs.loc[self.test_index]

    @property
    def target(self) -> pd.Series:
        """
        Return the target.
        """
        if self._target is None:
            self._target = self.database.target  # type: ignore

        return self._target

    @property
    def best_parameters(self) -> dict | None:
        """
        Return the best parameters.
        """
        return self._best_parameters

    @property
    def k_fold(self) -> pd.Series:
        """
        Return the k-fold and compute if none existent.
        """
        if self._k_fold is None:
            self._k_fold = self.database.cross_validation_cluster.loc[self.train_index]

        return self._k_fold

    @property
    def cv_strategy(self) -> GroupKFold:
        """
        Return the cross validation strategy.
        """
        if self.database.cross_validation_train is None:
            raise ValueError("The database cross validation is not set.")

        if self._cv_strategy is None:
            self._cv_strategy = GroupKFold(len(self.database.cross_validation_train))

        return self._cv_strategy

    # ___ Prediction ___

    @property
    def predict(self) -> pd.DataFrame | None:
        """
        Predict the whole dataset with the rained kernel.
        """
        if not self.fitted or self.database.target is None:
            warn("The predictor has to be fitted first.")
            return None

        if self._predict is None:
            # get all the data
            values = self.database.get_features(self.inputs.columns).dropna()
            if self._standardize_input:
                values = self.scale(values)

            # compute the prediction for whole dataset
            self._predict = pd.DataFrame(
                self.kernel.predict(values).astype(float),
                index=values.index,
                columns=[f"predicted_{self.database.target.name}_{self.name}"],
            )

        return self._predict

    @property
    def probability(self) -> pd.DataFrame | None:
        """
        Return the probability of the prediction for the whole dataset.
        """
        if not self.fitted or self.database.target is None:
            warn("The predictor has to be fitted first.")
            return None

        if self._probability is None:
            # get all the data
            values = self.database.get_features(self.inputs.columns).dropna()
            if self._standardize_input:
                values = self.scale(values)

            # compute the probabilities for whole dataset
            self._probability = pd.DataFrame(
                self.kernel.predict_proba(values)[:, 1],
                index=values.index,
                columns=[f"predicted_proba_{self.database.target.name}_{self.name}"],
            )

        return self._probability

    @property
    def score(self):
        """
        Get the score of the predictor
        """
        if not self.fitted:
            warn("The predictor has to be fitted first.")
            return None
        if self.database.test is None:
            warn("No test set is set.")
            return None

        if self._score is None:
            self._score = self.kernel.score(
                self.test_data,
                self.target.loc[self.test_index],
            )

        return self._score

    # ___ Training ___

    def fit(self):
        """
        Train the predictor.
        """
        if self.database.train is None:
            warn("No train set is set.")
            return
        if self._kernel is None:
            warn("No kernel is set.")
            return

        self.reset()  # reset the results
        self.kernel.fit(
            self.train_data,
            self.target.loc[self.train_index],
        )

        self.fitted = True

    def random_parameters_search(self, parameters: dict, n_iter: int = 500, **kwargs):
        """
        Perform a random search to find the best parameters.

        This function fits the kernel.

        :param parameters: The parameters to search.
        :param n_iter: The number of iterations.
        :param kwargs: The arguments to pass to the RandomizedSearchCV.
        """
        if self.database.train is None:
            warn("No train set is set.")
            return

        random_search = RandomizedSearchCV(
            self.kernel,
            parameters,
            n_iter=n_iter,
            cv=self.cv_strategy,
            scoring="f1",
            **kwargs,
        )

        random_search.fit(
            self.train_data,
            self.target.loc[self.train_index],  # type:ignore
            groups=self.k_fold,
        )

        self._best_parameters = random_search.best_params_

        # set the best kernel
        self.kernel = random_search.best_estimator_
        self.fitted = True

    def grid_parameters_search(self, parameters: dict, **kwargs):
        """
        Perform a grid search to find the best parameters.

        This function fits the kernel.

        :param parameters: The parameters to search.
        :param kwargs: The arguments to pass to the RandomizedSearchCV.
        """
        if self.database.train is None:
            warn("No train set is set.")
            return

        grid_search = GridSearchCV(
            self.kernel,
            parameters,
            cv=self.cv_strategy,
            scoring="f1",
            **kwargs,
        )

        grid_search.fit(
            self.train_data,
            self.target.loc[self.train_index],  # type:ignore
            groups=self.k_fold,
        )

        self._best_parameters = grid_search.best_params_

        # set the best kernel
        self.kernel = grid_search.best_estimator_
        self.fitted = True

    # ___ Figures ___

    @property
    def feature_importance(self) -> pd.DataFrame | None:
        """
        Return the feature importance and try to compute if None.
        """
        if self._feature_importance is None:
            self.compute_feature_importance()

        return self._feature_importance

    def compute_feature_importance(self, n_repeats=30):
        """
        Compute the feature importance once the model is fitted only.

        The feature importance is computed on the test set.

        :param n_repeats: The number of times to repeat the permutation.
        """
        if not self.fitted:
            warn("The predictor has to be fitted first.")
            return

        # compute the feature importance
        feature_importance = permutation_importance(
            self.kernel,  # type: ignore
            self.test_data,
            self.target.loc[self.test_index],
            n_repeats=n_repeats,
        )

        feature_importance = pd.DataFrame(
            feature_importance.importances.T, columns=self.inputs.columns
        )

        self._feature_importance = feature_importance.reindex(
            feature_importance.mean().sort_values(ascending=False).index, axis=1
        )

    @property
    def confusion_matrix(self) -> pd.DataFrame | None:
        """
        Return the confusion matrix and try to compute if None.
        """
        if self._confusion_matrix is None:
            self.compute_confusion_matrix()

        return self._confusion_matrix

    def compute_confusion_matrix(self):
        """
        Compute the confusion matrix.
        """
        if not self.fitted:
            warn("The predictor has to be fitted first.")
            return

        # compute the confusion matrix
        confusion_matrix_ = confusion_matrix(
            self.target.loc[self.test_index].values,
            self.kernel.predict(self.test_data),
        )

        self._confusion_matrix = np.round(
            confusion_matrix_ / confusion_matrix_.sum(axis=1)[:, np.newaxis], 2
        )

    def roc_curve(self) -> pd.DataFrame | None:
        """
        Compute the ROC curve.
        :return: the ROC curve in a pandas DataFrame.
        """
        if not self.fitted:
            warn("The predictor has to be fitted first.")
            return None

        falsepositive, trueprositive, thresholds = roc_curve(
            self.target.loc[self.test_index].values,
            self.kernel.predict_proba(self.test_data)[:, 1],
        )

        return pd.DataFrame(
            {
                "false_positive_rate": falsepositive,
                "true_positive_rate": trueprositive,
                "thresholds": thresholds,
            }
        )
