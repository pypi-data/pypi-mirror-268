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

# pylint: disable=import-error

from __future__ import annotations

from warnings import warn

import numpy as np
import pandas as pd
from geoh5py.objects import BlockModel, Grid2D, ObjectBase, Octree, Points

from ..shared.utils import (
    add_date_to_name,
    extract_dataframe_from_object,
    get_min_mean,
    indexes_intersect,
    rename_if_inlist,
)

IGNORE_FEATURES = [
    "x",
    "y",
    "z",
    "train",
    "test",
    "cross_validation",
    "in_use",
    "target",
    "no_target",
]


# pylint: disable=too-many-instance-attributes, too-many-public-methods
class Database:
    """
    Create a database object from a geoh5py object containing all the data.

    param data: A geoh5py object containing the data and vertices or centroids.
    param nan_threshold: The threshold of nan values in a column to be removed.
    """

    def __init__(
        self,
        data: Points | Grid2D | BlockModel | Octree | pd.DataFrame,
        nan_threshold: float = 0.8,
    ):
        self._target: None | str = None
        self._no_target: None | str = None
        self._metadata: dict = {}

        self._in_use_distance: None | dict = None
        self._nan_threshold: float = nan_threshold

        self.data = data
        self.columns = self._database.columns
        self._min_mean_distance: float | None = None

        self._database: pd.DataFrame

    # ___ prepare the core DataFrame of the class ___

    @property
    def data(self) -> pd.DataFrame:
        """
        Return the whole database.
        """
        return self._database

    @data.setter
    def data(self, data: Points | Grid2D | BlockModel | Octree | pd.DataFrame):
        """
        Set the database.
        :param data: A geoh5py object containing the data and centroids or vertices attributes;
        or a pandas DataFrame containing the data.
        """

        # if the data is a DataFrame
        if isinstance(
            data, pd.DataFrame
        ):  # considering there is no unwanted columns in it
            self._database = data
            self._data = None
        elif isinstance(data, ObjectBase):  # if the data is a geoh5py object
            # open the workspace
            self._database = extract_dataframe_from_object(data, IGNORE_FEATURES)
        else:
            raise TypeError("The data must be a geoh5py Object or a DataFrame.")

        # set in_use as True for all the data and set cross_validation as np nan for all the data
        self._database["in_use"] = True
        self._database["train"] = False
        self._database["test"] = False
        self._database["cross_validation"] = np.nan
        self._database["target"] = False
        self._database["no_target"] = False

    # ___ columns properties ___

    @property
    def columns(self) -> pd.DataFrame:
        """
        Return a DataFrame containing the information of the columns  .
        """
        return self._columns

    @columns.setter
    def columns(self, columns: list):
        """
        Set the defaults columns of the database.
        This setter should only be call when the database is created.
        :param columns: A list of columns.
        """
        self._columns = pd.DataFrame(
            np.zeros(len(columns)).astype(bool), index=columns, columns=["created"]
        )

        self._columns["ignore"] = [
            not (id_ in IGNORE_FEATURES) for id_ in self._columns.index
        ]
        self._columns["in_use"] = self._columns["ignore"]

        self.nan_threshold = self._nan_threshold

    # ___ remove columns where the percentage of nan> nan_threshold ___

    @property
    def nan_threshold(self) -> float:
        """
        Return the nan threshold.
        """
        return self._nan_threshold

    @nan_threshold.setter
    def nan_threshold(self, nan_threshold: float):
        """
        Set the threshold where a columns won't be used if it contains a percentage of nan values.
        :param nan_threshold: The nan threshold, must be between 0 and 1.
        """
        if nan_threshold <= 0 or nan_threshold > 1:
            raise ValueError("The nan threshold must be between 0 and 1.")

        self._nan_threshold = nan_threshold

        # if percentage of nan is higher than the nan threshold, set the columns in_use to false
        self._columns["percentage_nan"] = self._database.isnull().sum() / len(
            self._database
        )
        self._columns["in_use"] = (
            self._columns["percentage_nan"] < self._nan_threshold
        ) * self._columns["ignore"]

    # ___ features getter and setter ___

    def get_features(
        self,
        feature_names: str | list,
        index: pd.Index | list | None = None,
    ) -> pd.DataFrame:
        """
        Return the features of the database
        only the in_use columns are returned,
        the rows containing nan values are removed.
        :param feature_names: The name of the features to return.
        :param index: The list of indexes to use.
        :return: A dataframe containing the features.
        """
        if isinstance(feature_names, str):
            feature_names = [feature_names]

        if not all(feature in self.columns.index for feature in feature_names):
            raise KeyError(
                f"At least one of features {feature_names} not found in the database."
            )

        # prepare the index
        if index is None:
            index = self._database.index
        else:
            index = indexes_intersect(index)

        # return the features
        return self._database.loc[index, feature_names]

    def set_features(
        self,
        features_df: pd.DataFrame = None,
        ignore: bool = False,
        metadata: dict | None = None,
    ):
        """
        Set the features of the database.

        :param features_df: A dataframe containing the new features.
        :param ignore: If True, the new features will be ignored.
        :param metadata: The metadata of the new features.
        """
        if not isinstance(features_df, pd.DataFrame):
            raise TypeError("The features must be a pandas DataFrame.")

        if not isinstance(ignore, bool):
            raise TypeError("The ignore must be a boolean.")

        # rename the features if exists
        previous: list = []
        for feature in features_df.columns:
            # almost impossible scenario to have 2 data with the same name
            new_feature_name = rename_if_inlist(
                add_date_to_name(feature), self._columns.index.tolist() + previous
            )
            if new_feature_name != feature:
                features_df.rename(columns={feature: new_feature_name}, inplace=True)
                feature = new_feature_name
            previous.append(feature)

            if isinstance(metadata, dict):
                self._metadata.update({feature: metadata})

        # add columns to database
        self._database = pd.concat([self._database, features_df], axis=1)

        # add the new columns in the columns dataframe
        for feature in features_df.columns:
            # create as pandas series to insert in column dataframe
            series = pd.Series(
                [True, not ignore, np.nan, False],
                index=["created", "ignore", "percentage_nan", "in_use"],
            )

            series["percentage_nan"] = features_df[feature].isnull().sum() / len(
                features_df
            )

            self._columns.loc[feature] = series

    @property
    def features(self) -> list:
        """
        The features of the database,

        They are the features the user can play with.
        """
        return self._columns.loc[self._columns.ignore].index.tolist()

    @property
    def created(self) -> list:
        """
        List of the created features.
        """
        return self._columns.loc[self._columns.created].index.tolist()

    @property
    def metadata(self) -> dict:
        """
        Metadata of the database.
        """
        return self._metadata

    @property
    def in_use_features(self) -> list:
        """
        The activate features of the database,
        """
        return self._columns.loc[self._columns.in_use].index.tolist()

    @in_use_features.setter
    def in_use_features(self, features: list):
        if not all(
            feature in self._columns.loc[self._columns.ignore].index
            for feature in features
        ):
            raise KeyError("The features are not in the database.")

        self._columns.in_use = False
        self._columns.loc[features, "in_use"] = True

    @property
    def in_use(self) -> pd.Index:
        """
        The activate points of the database.
        """
        return self._database.loc[self._database.in_use].index

    @in_use.setter
    def in_use(self, in_use: list | bool):
        self._database["in_use"] = False

        if isinstance(in_use, bool):
            self._database.loc[:, "in_use"] = in_use
        elif isinstance(in_use, (list, pd.Index)):
            self._database.loc[in_use, "in_use"] = True
        else:
            raise TypeError("The in_use must be a list of indices or a boolean.")

        self.drop_nan_in_use()

    def drop_nan_in_use(self):
        """
        Drop the nan in the in_use rows.
        """
        # find nan values rows in the in use set
        nans = (
            ~self._database.loc[
                :, self._columns.loc[self._columns.in_use].index.tolist()
            ]
            .isna()
            .any(axis=1)
        )

        self._database.in_use = nans * self._database.in_use

    # ___ define the target and no target columns for the training of ML models ___

    def reset_test_validation(self):
        """
        Reset the database to its initial state.
        """
        self._database["in_use"] = True
        self._database["train"] = False
        self._database["test"] = False
        self._database["cross_validation"] = np.nan

    def verify_target(self, target: pd.Series):
        """
        Format a target for ML models.
        :param target: The target to format.
        """
        # verify if the target is a pandas series
        if not isinstance(target, pd.Series):
            raise TypeError("Target must be a pandas series.")

        # verify the name is not in the IGNORE_FEATURES
        if target.name in IGNORE_FEATURES:
            raise KeyError(
                f"Target name is in the IGNORE_FEATURES ({IGNORE_FEATURES})."
            )

        # verify the target contains 0 and 1
        if not target.sort_values().unique().astype(int).tolist() == [0, 1]:
            raise AssertionError("Target must be a binary variable.")

        # verify the index of the target are in the database
        if not all(target.index.isin(self._database.index)):
            raise IndexError("Target index not in the database.")

        # verify the name is in the columns
        if target.name not in self._columns.index:
            raise KeyError("Target not found in the database.")

        # ignore the target column
        self.reset_test_validation()
        self._columns.loc[target.name, "in_use"] = False
        self._columns.loc[target.name, "ignore"] = False

    def clean_no_target(self):
        """
        Remove the no_target which are targets.
        """
        # remove the no_target which are target
        if self._target is not None and self._no_target is not None:
            self._database.no_target = self._database.no_target * np.invert(self.target)

    @property
    def target(
        self,
    ) -> pd.Series | None:
        """
        Return the target of the database.
        """
        if self._target is None:
            warn("Target not set.")
            return None

        return self._database.target.rename(self._target)

    @target.setter
    def target(self, target: pd.Series):
        # todo: verify target is in self.columns and replace if in Feature
        """
        Set the target of the database.
        :param target: The target of the database in form of a binary pandas series.
        """
        # verify the target properties
        self.verify_target(target)

        # verify the target is different from the no target
        if target.equals(self.no_target):
            raise AssertionError("Target and no target are the same.")

        self._database.target = target
        self._target = target.name

        self.clean_no_target()

    @property
    def no_target(
        self,
    ) -> pd.Series | None:
        """
        Return the no target of the database.
        """
        if self._no_target is None:
            if self._target is None:
                warn("No target not set.")
                return None
            # return the opposite of target
            return ~self._database.target.copy()

        return self._database.no_target.rename(self._no_target)

    @no_target.setter
    def no_target(self, no_target: pd.Series):
        """
        Set the no target of the database.
        :param no_target: The target of the database.
        """
        # verify the target properties
        self.verify_target(no_target)

        # verify the target is different from the no target
        if no_target.equals(self.target):
            raise AssertionError("Target and no target are the same.")

        self._database.no_target = no_target
        self._no_target = no_target.name

        self.clean_no_target()

    # ___ training and testing data ___

    @property
    def train(self) -> pd.Index | None:
        """
        Return the training set of the database;
        only the "used" data will be returned.
        :return: A copy of the pandas DataFrame containing the training set.
        """
        # verify if train column is only False
        if self._database.train.sum() == 0:
            warn("The training set is not defined in the database.")
            return None

        return self._database.loc[self._database.train & self._database.in_use].index

    @train.setter
    def train(self, train: list):
        """
        Define the training set of the database.
        :param train: The indices of the training set.
        """
        self._database["train"] = False
        self._database.loc[train, "train"] = True

    @property
    def test(self) -> pd.Index | None:
        """
        Return the test set of the database;
        only the "used" data will be returned.
        :return: A copy of the pandas DataFrame containing the test set.
        """
        if self._database.test.sum() == 0:
            warn("The testing set is not defined in the database.")
            return None

        return self._database.loc[self._database.test & self._database.in_use].index

    @test.setter
    def test(self, test: list):
        """
        Define the test set of the database.
        :param test: The indices of the test set.
        """
        self._database["test"] = False
        self._database.loc[test, "test"] = True

    # ___ cross validation getters and setters ___

    @property
    def cross_validation_cluster(self) -> pd.Series:
        """
        Return the cross validation set of the database.
        """
        return self._database.cross_validation

    @cross_validation_cluster.setter
    def cross_validation_cluster(
        self, cross_validation: pd.Series | None
    ):  # todo: useful latter if the user wants to set is own training/testing set.
        """
        Define the cross validation set of the database.
        :param cross_validation: The indices of the cross validation set.
        """
        # verify if cross_validation is None for default value
        if cross_validation is None:
            self._database["cross_validation"] = np.nan
        elif isinstance(cross_validation, pd.Series):
            # verify all the index are in the database
            if not cross_validation.index.isin(self._database.index).all():
                raise IndexError(
                    "The index of 'cross_validation' are not in the database."
                )

            self._database.loc[
                cross_validation.index, "cross_validation"
            ] = cross_validation.values

        else:
            raise TypeError("'cross_validation' must be a pandas Series.")

    @property
    def cross_validation_train(self) -> list | None:
        """
        Return the cross validation training set of the database.
        """
        if self.train is None:
            return None

        # verify if the cross_validation is separated
        return self._database.loc[self.train, "cross_validation"].unique().tolist()

    @cross_validation_train.setter
    def cross_validation_train(self, cross_validation: list):
        """
        Set the cross validation training set of the database.
        :param cross_validation: The cross validation to set to train.
        """
        self._database.loc[:, "train"] = False

        for value in cross_validation:
            # select the value in cross_validation and in use and set the train to true
            self._database.loc[
                self._database.in_use & (self._database.cross_validation == value),
                "train",
            ] = True

    @property
    def cross_validation_test(self) -> list | None:
        """
        Return the cross validation testing set of the database.
        """
        if self.test is None:
            return None

        return self._database.loc[self.test, "cross_validation"].unique().tolist()

    @cross_validation_test.setter
    def cross_validation_test(self, cross_validation: list):
        """
        Set the cross validation testing set of the database.
        :param cross_validation: The cross validation to set to train.
        """
        self._database.loc[:, "test"] = False

        # verify if the cross_validation is separated
        if self.cross_validation_train is not None:
            if bool(set(self.cross_validation_train) & set(cross_validation)):
                raise AssertionError(
                    "The cross validation train and test are not separated."
                )

        for value in cross_validation:
            self._database.loc[
                self._database.in_use & (self._database.cross_validation == value),
                "test",
            ] = True

    def cross_validation_representation(self) -> pd.DataFrame:
        """
        Return the percentage of positive values each cross validation group contains.

        :return: A DataFrame containing the percentage of positive values.
        """
        if self.target is None or self.cross_validation_cluster is None:
            raise AssertionError("Target or cross validation are not set.")

        # get the target and no target
        target = self.target.loc[self.in_use]

        # get the cross validation in use
        cross_validation = self.cross_validation_cluster.loc[target.index]

        # group by cluster
        cross_correlation = target.groupby(cross_validation).size()

        # compute the percentage
        cross_correlation = cross_correlation / cross_correlation.sum() * 100

        return cross_correlation

    def respect_inuse_cross_validation(self):
        """
        Keep only the cross_validation that are in use, drop the others
        and reorder the cross validation.
        """
        # get the cross validation in use
        cross_validation = self.cross_validation_cluster.loc[self.in_use]

        # change the unique values to be a range list
        cross_validation = cross_validation.replace(
            cross_validation.unique(), range(cross_validation.nunique())
        )

        # set the cross validation
        self.cross_validation_cluster = None
        self.cross_validation_cluster = cross_validation

        # verify for each cross validation group if they are target and no target

    @property
    def min_mean_distance(self) -> float:
        """
        Return the minimum mean distance between the points.
        """
        if self._min_mean_distance is None:
            self._min_mean_distance = get_min_mean(
                self._database.loc[self._database.in_use, ["x", "y", "z"]]
            )

        return self._min_mean_distance
