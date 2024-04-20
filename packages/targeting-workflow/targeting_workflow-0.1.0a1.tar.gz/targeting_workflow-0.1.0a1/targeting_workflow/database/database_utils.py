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

import pandas as pd
from scipy.spatial import cKDTree

from ..database.database import Database
from ..features.dbscan import DBSCAN
from ..features.kmean import FastKMean
from ..features.pca import PCA
from ..shared.utils import compute_closest_id, grid_resampling


def find_cross_validation(database: Database, distance: float):
    """
    Define the cross validation groups of the database only on the positive targets.
    It runs a DBSCAN on the positive targets and uses
    the found labels as the cross_validation groups.
    :param database: The database to find the cross_validation groups.
    :param distance: The distance to use for the DBSCAN.
    """
    # verify the targets are set
    if database.target is None:
        raise AssertionError("The targets are not set.")

    database.cross_validation_cluster = None

    in_use_positive = database.get_features(
        ["x", "y", "z"], database.target.loc[database.target].index
    )

    if len(in_use_positive) == 0:
        raise AssertionError(
            "No positive targets were found."
            "Restart the workflow and set the targets."
        )

    # create a temporary database
    in_use_positive = Database(in_use_positive)

    # todo: in the future, have an option to allow KMean
    # compute the dbscan
    dbscan = DBSCAN(
        in_use_positive,
        ["x", "y", "z"],
        standardize_input=False,
        eps=distance,
        min_samples=1,
        n_jobs=-1,
    )

    if dbscan.output.DBSCAN.unique().size <= 1:  # type: ignore
        raise AssertionError("No group were found, please reduce distance.")

    # get the output and change the index to the database index
    database.cross_validation_cluster = dbscan.output.DBSCAN  # type: ignore


def assign_cross_validation(database: Database):
    """
    Assign the cross_validation group to the no target of the database.
    :param database: The database to assign the cross_validation group.
    """
    # verify the positive targets have cross_validation groups
    if (
        database.cross_validation_cluster.unique().size <= 1
        or database.target is None
        or database.no_target is None
    ):
        raise AssertionError("The cross_validation groups are not set. ")

    # get the positive targets
    inputs = ["x", "y", "z", "cross_validation"]
    positive_targets = database.get_features(
        inputs, database.target[database.target].index
    )

    negative_targets = database.get_features(
        inputs, database.no_target[database.no_target].index
    )

    if len(negative_targets) == 0:
        raise AssertionError(
            "No negative targets were found."
            "Restart the workflow and ensure to have negative examples."
        )
    if len(positive_targets) == 0:
        raise AssertionError(
            "No positive targets were found."
            "Restart the workflow and ensure to have positive examples."
        )

    # get the closest index of the positive points closest to every negative points
    closest_index = compute_closest_id(
        positive_targets.loc[:, ["x", "y", "z"]],
        negative_targets.loc[:, ["x", "y", "z"]],
    )

    # assign the cross_validation group of the closest positive target
    negative_targets.cross_validation = positive_targets.cross_validation[
        closest_index
    ].values

    # save the targets in the database
    database.cross_validation_cluster = negative_targets.cross_validation


def balance(database: Database, inputs: list, ratio: float = 0.9):
    """
    Balance the dataset by under sampling with a 1:1 ratio.
    :param database: The database to balance.
    :param inputs: The inputs to use to compute the PCA.
    :param ratio: The ratio of the pca to keep.
    """
    if database.target is None or database.no_target is None:
        warn("The targets are not set, passing.")
        return

    # set in use to True
    database.in_use = True

    # verify in use is not empty
    if len(database.in_use.intersection(database.target.index)) == 0:  # type: ignore
        raise AssertionError(
            "All your positive targets contains no-data. "
            "Drop the properties containing no-data values."
        )
    if len(database.in_use.intersection(database.no_target.index)) == 0:  # type: ignore
        raise AssertionError(
            "All your negative targets contains no-data. "
            "Drop the properties containing no-data values."
        )

    # compute PCA
    pca = PCA(database, inputs, standardize_input=True)
    pcas = pca.explained_variance(ratio=ratio)

    # get positive and negative targets
    positive_targets = database.get_features(
        "cross_validation", [database.target[database.target].index, database.in_use]
    )

    negative_targets = database.get_features(
        "cross_validation",
        [database.no_target[database.no_target].index, database.in_use],
    )

    index_to_keep = []

    for cross_validation in database.cross_validation_cluster.unique():
        positive_targets_cross_validation = positive_targets.loc[
            positive_targets.cross_validation == cross_validation
        ]
        negative_targets_cross_validation = negative_targets.loc[
            negative_targets.cross_validation == cross_validation
        ]

        # compute the number of points to keep
        if len(positive_targets_cross_validation) < len(
            negative_targets_cross_validation
        ):
            to_balance = negative_targets_cross_validation
            to_keep = positive_targets_cross_validation
        elif len(positive_targets_cross_validation) > len(
            negative_targets_cross_validation
        ):
            to_balance = positive_targets_cross_validation
            to_keep = negative_targets_cross_validation
        else:
            continue
        if len(to_keep) > 0:
            # compute fast KMean with the pcas
            kmean = FastKMean(
                Database(pcas.loc[to_balance.index]),
                inputs=pcas.columns.tolist(),
                standardize_input=True,
                n_clusters=len(to_keep),
            )
            kept_index_temp = kmean.closest_to_centroids

            # raise warning if the balance is not exactly 1:1
            if len(kept_index_temp) != len(list(set(kept_index_temp))):  # type: ignore
                warn("The balance is not exactly 1:1.")

            index_to_keep.extend(kept_index_temp + to_keep.index.tolist())

    # set in_use to the balanced data
    database.in_use = index_to_keep

    # clean the cross_validation_cluster
    database.respect_inuse_cross_validation()


def auto_split_train_test(database: Database, test_ratio: float = 0.2):
    """
    Randomly balance the dataset.
    :param database: The database to split the train and the test values.
    :param test_ratio: The ratio of the test set.
    """
    # compute the percentage of every cross_validation group
    cross_validation_count = (
        database.cross_validation_cluster.loc[database.in_use]
        .value_counts(normalize=True)
        .sample(frac=1)
    )

    # split the data into training and testing set
    ratio = 0
    test, train = [], []

    for index_, values_ in cross_validation_count.items():
        cross_validation_index = database.cross_validation_cluster.loc[
            database.cross_validation_cluster == index_
        ].index
        if ratio < test_ratio:
            test += cross_validation_index.intersection(database.in_use).tolist()
        else:
            train += cross_validation_index.intersection(database.in_use).tolist()
        ratio += values_

    # set the training and testing set
    database.train = train
    database.test = test


def spatial_resample_database(
    database: Database, index: pd.Index, distance: float, tree: cKDTree | None = None
) -> pd.Index:
    """
    Spatially resample the database based on the minimum distances between the points.
    :param database: The database to resample.
    :param index: The index of the points to use.
    :param distance: The distance to use for the DBSCAN.
    :param tree: The tree to use for the spatial resampling.
    :return: The new sampled index.
    """
    # get the data to resample
    points = database.get_features(["x", "y", "z"], index)

    # get the new index
    new_points = grid_resampling(points, distance, tree=tree)

    # set the new index
    return new_points


def compute_target(
    database: Database, target: str, operand: str, value: list[int | float]
) -> pd.Series:
    """
    Set the target of the database.

    :param database: The database to set the target.
    :param target: The target to set.
    :param operand: The sign to use for the target.
    :param value: The value of the target.
    """
    # verify if target is in the database
    if target not in database.columns.index:
        raise KeyError("The target must be in the database columns.")

    # compute the output
    inputs = database.get_features([target])

    if operand == "=":
        outputs = inputs[target].isin(value)
    elif operand == "<>":
        outputs = (inputs[target] >= min(value)) & (inputs[target] <= max(value))
    else:
        raise AssertionError("The operand must be '=' or '<>'.")

    return outputs


def set_target(database: Database, target: str, sign: str, value: list[int | float]):
    """
    Set the target of the database.

    :param database: The database to set the target.
    :param target: The target to set.
    :param sign: The sign to use for the target.
    :param value: The value of the target.
    """
    # compute the target
    target_series = compute_target(database, target, sign, value)

    # set the target
    database.target = target_series


def set_no_target(
    database: Database,
    no_target: str,
    sign: str,
    value: list[int | float],
):
    """
    Set the target of the database.
    :param database: The database to set the target.
    :param no_target: The target to set.
    :param sign: The sign to use for the target.
    :param value: The value of the target.
    """
    # compute the target
    target_series = compute_target(database, no_target, sign, value)

    # set the no target
    database.no_target = target_series
