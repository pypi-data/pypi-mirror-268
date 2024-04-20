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

from plotly.graph_objects import Figure

from ..database.database import Database
from ..shared import plots


def plot_data_groups(database: Database, **plot_kwargs) -> Figure:
    """
    Create points for the plot validation plots and call the plot,
    it is saved in the assets/temp folder.
    :param database: The database to use.
    :param plot_kwargs: The kwargs to pass to the plot function.
    :return: The plotly figure if return_fig = True in **kwargs.
    """
    if not isinstance(database, Database):
        raise TypeError("database must be a Database")

    # prepare the data
    points = database.get_features(["x", "y", "z", "cross_validation"], database.in_use)

    # if dataframe len is 0, raise error
    if len(points) == 0:
        raise AssertionError(
            "The database does not contain any valid data. "
            "Validate for properties that may only contain no-data values."
        )

    points["target"] = 0

    if database.target is None:
        raise AssertionError("the target is not set")

    points.loc[
        database.target.loc[database.target].index.intersection(database.in_use),
        "target",
    ] = 1

    points["test"] = 0
    points.loc[database.test, "test"] = 1

    points.sort_values(by="cross_validation", inplace=True)

    # plot
    return plots.plot_data_groups(points, **plot_kwargs)


def plot_correlation_matrix(
    database: Database, inputs: list[str], **plot_kwargs
) -> Figure:
    """
    Compute the correlation matrix of the inputs.
    :param database: The database to use.
    :param inputs: The inputs to use to compute the correlation matrix.
    :param plot_kwargs: The kwargs to pass to the plot function.
    :return: The plotly figure if return_fig = True in **kwargs.
    """
    if not isinstance(database, Database):
        raise TypeError("database must be a Database")

    return plots.plot_correlation_matrix(
        database.get_features(inputs).corr(), **plot_kwargs
    )


def plot_histogram_feature(database: Database, feature: str, **plot_kwargs) -> Figure:
    """
    Plot the histogram of the feature.
    :param database: The database to use.
    :param feature: The feature to plot.
    :param plot_kwargs: The kwargs to pass to the plot function.
    :return: The plotly figure if return_fig = True in **kwargs.
    """
    if not isinstance(database, Database):
        raise TypeError("database must be a Database")

    # copy the database
    database_ = database.get_features([feature, "train", "test"])

    # add positive and negative values
    database_["positive"] = False
    database_["negative"] = False

    if database.target is not None and database.no_target is not None:
        database_.loc[database.target.loc[database.target].index, "positive"] = True
        database_.loc[
            database.no_target.loc[database.no_target].index, "negative"
        ] = True

    # rename feature to 'data'
    database_.rename(columns={feature: "data"}, inplace=True)

    # plot the histogram
    return plots.plot_histogram_feature(database_, title=feature, **plot_kwargs)
