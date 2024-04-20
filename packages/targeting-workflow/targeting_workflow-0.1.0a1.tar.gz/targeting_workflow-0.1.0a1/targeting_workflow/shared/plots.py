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

from itertools import product

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import auc

from ..shared.utils import (
    dataframe_to_histogram,
    format_float_string,
    int_to_k,
    random_sampling,
)


def plot_correlation_matrix(
    correlation: pd.DataFrame,
    maximum_plot_size: int = 25,
    save_fig: bool = False,
    **html_kwargs,
) -> go.Figure:
    """
    Plot the correlation matrix.
    :param correlation: The correlation matrix.
    :param maximum_plot_size: the number where the labels are shut off.
    :param save_fig: If True, return the figure, else save it.
    :param html_kwargs: The kwargs to pass to plotly write_html.
    :return: The plotly figure if return_fig = True.
    """
    # mask upper matrix
    mask = np.triu(np.ones_like(correlation, dtype=bool))
    correlation = correlation.mask(mask)

    # create the annotations
    annotations = []
    if len(correlation) < maximum_plot_size:
        for i, j in product(range(len(correlation)), repeat=2):
            if ~np.isnan(correlation.iloc[i, j]):
                color = "black"
                if abs(correlation.iloc[i, j]) > 0.8:
                    color = "white"
                annotations.append(
                    {
                        "x": j,
                        "y": i,
                        "text": round(correlation.iloc[i, j], 2),
                        "showarrow": False,
                        "font": {"color": color},
                    }
                )

    fig = px.imshow(
        correlation,
        color_continuous_scale=px.colors.diverging.RdBu[::-1],
        zmin=-1,
        zmax=1,
    )

    fig.update_layout(
        title="Correlation matrix",
        xaxis={"tickangle": -45, "tickfont": {"size": 10}},
        yaxis={"tickfont": {"size": 10}},
        margin={"l": 50, "r": 50, "b": 50, "t": 50, "pad": 4},
        annotations=annotations,
        template="plotly_white",
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        xaxis_zeroline=False,
        yaxis_zeroline=False,
        font={"size": 10},
    )

    # Save the figure as an HTML file
    if save_fig:
        fig.write_html(**html_kwargs)

    # return for the user
    return fig


def plot_data_groups(
    points: pd.DataFrame, save_fig: bool = False, **html_kwargs
) -> go.Figure:
    """
    Plot the cross validation groups of data.
    :param points: The points containing the cross validation values in a DataFrame.
    :param save_fig: If True, return the figure, else save it.
    :param html_kwargs: The kwargs to pass to plotly write_html.
    :return: The plotly figure if return_fig = True.
    """
    # verify that the desired columns are in the dataframe
    if any(
        column not in points.columns
        for column in ["x", "y", "z", "target", "cross_validation", "test"]
    ):
        raise KeyError(
            "One of the columns ['x', 'y', 'z', 'target', 'cross_validation',"
            " 'test'] is missing in 'points'."
        )

    # resample the points for a fast plot
    points = pd.DataFrame(random_sampling(points.values, 10000), columns=points.columns)

    # change cross validation to string
    points["cross_validation"] = points["cross_validation"].astype(str)

    points.loc[(points.target == 0) & (points.test == 0), "target"] = "negative - train"
    points.loc[(points.target == 1) & (points.test == 0), "target"] = "target - train"
    points.loc[(points.target == 0) & (points.test == 1), "target"] = "negative - test"
    points.loc[(points.target == 1) & (points.test == 1), "target"] = "target - test"

    points.rename(columns={"cross_validation": "spatial group"}, inplace=True)
    points.test = 15

    # Create the 3D scatter plot using Plotly
    fig = px.scatter_3d(
        points,
        x="x",
        y="y",
        z="z",
        color="spatial group",
        symbol="target",
        color_discrete_sequence=px.colors.qualitative.Dark24,
        size="test",
        size_max=15,
    )

    # specify trace names and symbols in a dict
    symbols = {
        "negative - train": "circle-open",
        "target - train": "diamond-open",
        "negative - test": "circle",
        "target - test": "diamond",
    }

    # set all symbols in fig
    for id_, _ in enumerate(fig.data):
        fig.data[id_].marker.symbol = symbols[fig.data[id_].name.split(", ")[1]]

    # Update the layout to respect aspect ratio
    x_range = points.x.max() - points.x.min()
    y_range = points.y.max() - points.y.min()
    z_range = points.z.max() - points.z.min()

    # add annotation
    fig.add_annotation(
        {
            "x": 0,
            "y": 1.0,
            "showarrow": False,
            "text": "○ negative - train<br>◇ target - train "
            "<br>● negative - test<br>◆ target - test",
            "xanchor": "left",
            "align": "left",
        }
    )

    # Update the layout
    fig.update_layout(
        title="Spatial groups",
        scene={
            "aspectmode": "manual",
            "aspectratio": {"x": x_range / y_range, "y": 1, "z": z_range / y_range},
        },
        legend_title="",
    )

    # remove marker from legend
    for trace in fig.data:
        trace["marker"]["line"]["width"] = 0
        trace["legendgroup"] = "groups"
        trace["legendgrouptitle_text"] = "groups"
        if "negative" in trace["name"]:
            trace["name"] = trace["name"].split(".")[0]
        else:
            trace["showlegend"] = False

    # return for the user
    if save_fig:
        fig.write_html(**html_kwargs)

    # Save the figure as an HTML file
    return fig


def plot_histogram_feature(
    dataframe: pd.DataFrame,
    title: str = "histogram",
    nb_bins: int = 50,
    save_fig: bool = False,
    **html_kwargs,
) -> go.Figure:
    """
    Plot the histogram of a feature passed as a pd.DataFrame.
    :param dataframe: The histogram passed as a DataFrame.
    :param title: The feature name for the title.
    :param nb_bins: The number of bins to use.
    :param save_fig: If True, return the figure, else save it.
    :param html_kwargs: The kwargs to pass to plotly write_html.
    :return: The plotly figure if return_fig = True.
    """
    histogram, positive_sum, negative_sum = dataframe_to_histogram(dataframe, nb_bins)

    # plot the figure
    fig = go.Figure(
        data=[
            go.Bar(  # all_positive
                x=histogram.bin,
                y=histogram.positive,
                marker={"color": "#f0fff0"},
                name="all - positive",
                showlegend=True,
            ),
            go.Bar(  # all_negative
                x=histogram.bin,
                y=-histogram.negative,
                marker={"color": "#ffb6c1"},
                name="all - negative",
                showlegend=True,
            ),
            go.Bar(  # train positive
                x=histogram.bin,
                y=histogram.train_positive,
                marker={"color": "#90ee90"},
                name="train set - positive",
                showlegend=True,
                width=0.45,
            ),
            go.Bar(  # train negative
                x=histogram.bin,
                y=-histogram.train_negative,
                marker={"color": "#FF0000"},
                name="train set - negative",
                showlegend=True,
                width=0.45,
            ),
            go.Bar(  # test positive
                x=histogram.bin,
                y=histogram.test_positive,
                marker={"color": "#228b22"},
                name="test set - positive",
                showlegend=True,
                width=0.15,
            ),
            go.Bar(  # test negative
                x=histogram.bin,
                y=-histogram.test_negative,
                marker={"color": "#b22222"},
                name="test set - negative",
                showlegend=True,
                width=0.15,
            ),
        ]
    )

    delta = np.mean(
        [interval.left - interval.right for interval in histogram.index.tolist()]
    )

    fig.update_layout(
        barmode="overlay",
        bargap=0,
        xaxis_title=f"interval {title}",
        yaxis_title=f"% negative ({int_to_k(negative_sum)}) "
        + f"vs % positive ({int_to_k(positive_sum)})",
        xaxis={
            "ticktext": [
                f"{format_float_string(interval.left, delta)} to "
                + f"{format_float_string(interval.right, delta)}"
                for interval in histogram.index.tolist()
            ],
            "tickvals": list(range(len(histogram.bin))),
        },
    )

    # Save the figure as an HTML file
    if save_fig:
        fig.write_html(**html_kwargs)

    # return for the user
    return fig


def plot_confusion_matrix(
    confusion_matrix: np.ndarray, save_fig: bool = False, **html_kwargs
) -> go.Figure:
    """
    Plot the confusion matrix and save it in the assets/temp.
    :param confusion_matrix: The confusion matrix passed as a numpy array.
    :param save_fig: If True, return the figure, else save it.
    :param html_kwargs: The kwargs to pass to plotly write_html.
    return: The plotly figure if return_fig = True.
    """

    fig = px.imshow(
        confusion_matrix,
        text_auto=".0%",
        color_continuous_scale=px.colors.sequential.Reds,
    )

    fig.update_layout(
        title="Confusion matrix",
        xaxis={"ticktext": ["negative", "positive"], "tickvals": [0, 1]},
        yaxis={"ticktext": ["negative", "positive"], "tickvals": [0, 1]},
        yaxis_title="Target",
        xaxis_title="Predicted",
    )

    fig.update_coloraxes(showscale=False)

    # Save the figure as an HTML file
    if save_fig:
        fig.write_html(**html_kwargs)

    # return for the user
    return fig


def plot_feature_importance(
    feature_importance: pd.DataFrame, save_fig: bool = False, **html_kwargs
) -> go.Figure:
    """
    Plot the feature importance and save it in the assets/temp.
    :param feature_importance: The feature importance passed as a DataFrame.
    :param save_fig: If True, return the figure, else save it.
    :param html_kwargs: The kwargs to pass to plotly write_html.
    :return: The plotly figure if return_fig = True.
    """

    feature_importance = feature_importance.loc[
        :, feature_importance.quantile([0.25, 0.5, 0.75]).mean() != 0
    ].copy()

    # prepare colorbar
    mean_importance = feature_importance.mean().values

    if mean_importance.size == 0:
        return go.Figure()

    mean_importance = (
        np.where(
            mean_importance > 0,
            mean_importance / np.abs(mean_importance.max()),
            mean_importance / np.abs(mean_importance.min()),
        )
        * 10
    ).astype(int) + 10

    colors_intensities = [0, 0.5, 1]

    colors = np.array([[230, 30, 30], [250, 230, 80], [30, 130, 30]])

    intensities = [np.interp(x, [0, 20], [0, 1]) for x in mean_importance]

    palette = np.array(
        [
            np.interp(intensities, colors_intensities, colors[:, 0]),
            np.interp(intensities, colors_intensities, colors[:, 1]),
            np.interp(intensities, colors_intensities, colors[:, 2]),
        ]
    ).T

    # plot the figure
    fig = go.Figure(
        data=[
            go.Box(
                y=feature_importance.iloc[:, id_],
                marker_color=f"rgb({palette[id_, 0]}, {palette[id_, 1]}, {palette[id_, 2]})",
            )
            for id_ in range(int(feature_importance.shape[1]))
        ]
    )

    fig.add_shape(
        type="line",
        x0=-0.5,
        y0=0,
        x1=feature_importance.shape[1],
        y1=0,
        line_dash="dash",
        line_width=3,
        line={"color": "black"},
        xref="x",
        yref="y",
    )

    # format the layout
    fig.update_layout(
        title="Feature importance",
        xaxis_title="Features",
        yaxis_title="overfitting < unused > predictive",
        xaxis={
            "showgrid": False,
            "zeroline": False,
            "ticktext": feature_importance.columns,
            "tickvals": list(range(len(feature_importance.columns))),
        },
        yaxis={"zeroline": False, "gridcolor": "black"},
        yaxis_range=[
            -np.max(feature_importance.abs().values) - 0.05,
            np.max(feature_importance.abs().values) + 0.05,
        ],
        showlegend=False,
    )

    # save the figure as an HTML file
    if save_fig:
        fig.write_html(**html_kwargs)

    # return for the user
    return fig


def plot_roc_curve(
    roc_curve: pd.DataFrame, save_fig: bool = False, **html_kwargs
) -> go.Figure:
    """
    Plot the ROC curve and save it in the assets/temp.
    :param roc_curve: The ROC curve passed as a pandas DataFrame.
    :param save_fig: If True, return the figure, else save it.
    :param html_kwargs: The kwargs to pass to plotly write_html.
    :return: The plotly figure if return_fig = True.
    """
    default_columns = ["false_positive_rate", "true_positive_rate", "thresholds"]

    # verify if the roc_curve is a pandas DataFrame
    if not isinstance(roc_curve, pd.DataFrame):
        raise TypeError("roc_curve must be a pandas DataFrame.")
    # and contains the right columns
    if set(roc_curve.columns.tolist()) != set(default_columns):
        raise KeyError(f"roc_curve columns must be: {default_columns}.")

    accuracy = auc(roc_curve.false_positive_rate, roc_curve.true_positive_rate)

    # plot the figure
    fig = px.area(
        x=roc_curve.false_positive_rate,
        y=roc_curve.true_positive_rate,
        title=f"ROC Curve (AUC={accuracy:.4f})",
        labels={"x": "False Positive Rate", "y": "True Positive Rate"},
    )

    fig.add_shape(type="line", line={"dash": "dash"}, x0=0, x1=1, y0=0, y1=1)

    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    fig.update_xaxes(constrain="domain")

    # save the figure as an HTML file
    if save_fig:
        fig.write_html(**html_kwargs)

    # return for the user
    return fig
