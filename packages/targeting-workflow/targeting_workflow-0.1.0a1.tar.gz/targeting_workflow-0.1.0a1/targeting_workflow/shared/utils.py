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

import math
from copy import copy

import numpy as np
import pandas as pd
from geoh5py.data import NumericData
from geoh5py.objects import ObjectBase
from geoh5py.shared.utils import fetch_active_workspace
from scipy.sparse import csr_matrix
from scipy.spatial import cKDTree


def standardize(inputs: np.ndarray) -> np.ndarray:
    """
    Standardize the inputs.
    :param inputs: the inputs to standardize.
    :return: the standardized inputs.
    """
    return (inputs - np.nanmean(inputs)) / np.nanstd(inputs)


def normalize(inputs: np.ndarray) -> np.ndarray:
    """
    Normalize the inputs between 0 and 1.
    :param inputs: the inputs to standardize.
    :return: the normalized inputs.
    """
    return (inputs - np.nanmin(inputs)) / (np.nanmax(inputs) - np.nanmin(inputs))


def is_digit(value: str) -> bool:
    """
    Check if a value is a digit.
    :param value: the value to check.
    :return: True if the value is a digit, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def rename_if_inlist(name: str, name_list: list) -> str:
    """
    Rename a feature if it is already in the list.
    :param name: the name of the feature.
    :param name_list: the list of names.
    :return: the new name.
    """
    if name in name_list:
        _id = 1
        while f"{name}({_id})" in name_list:
            _id += 1
        name = f"{name}({_id})"
    return name


def indexes_intersect(indexes: list[pd.Index]) -> pd.Index:
    """
    Compute the intersection of a list of indexes.
    :param indexes: the list of indexes.
    :return: the intersection of the indexes.
    """
    if not isinstance(indexes, list):
        indexes = [indexes]

    if not all(isinstance(index, pd.Index) for index in indexes):
        raise TypeError("indexes must be a list of pd.Index")

    output = indexes[0]
    for index in indexes[1:]:
        output = output.intersection(index)

    return output


def compute_closest_id(dataframe1: pd.DataFrame, dataframe2: pd.DataFrame) -> pd.Index:
    """
    Compute the closest id of points of dataframe2 to dataframe1.
    :param dataframe1: the first dataframe with points coordinates.
    :param dataframe2: the second dataframe with points coordinates.
    :return: the index of the closest points from dataframe 1 from points dataframe2 .
    """
    # if the dataframe doesn't have the same columns, raise an error
    if not dataframe1.columns.equals(dataframe2.columns):
        raise IndexError("The dataframes must have the same columns")

    # if the columns type of the dataframes are not numerical, raise an error
    if not dataframe1.select_dtypes(include=np.number).columns.equals(
        dataframe1.columns
    ):
        raise TypeError("The columns must be numerical")

    tree = cKDTree(dataframe1.values)
    _, indices = tree.query(dataframe2.values)

    return dataframe1.index[indices]


def mean_min_distance(values: np.ndarray) -> float:
    """
    Compute the mean of the minimum distance of each point to the other points.

    :param values: the coordinates of the point to compute the KDTree.

    :return: the mean of the minimum distance of each point to the other points.
    """
    # verify the dataframe has numerical columns
    distances, _ = cKDTree(values).query(values, k=2)

    # get the mean of the distances
    return np.mean(distances[:, 1])


def random_sampling(values: np.ndarray, size: int, n_bins: int = 100, axis: int = 3):
    """
    Perform a random sampling of the rows of the input array based on
    the distribution of the columns values.
    :param values: Input array of values N x M, where N >> M
    :param size: Number of indices (rows) to be extracted from the original array.
    :param n_bins: Number of bins to use for the histogram.
    :param axis: Axis along which to compute the histogram.
    :returns: Indices of samples randomly selected from the PDF
    """
    if size >= values.shape[0]:
        return values

    probabilities = np.zeros(values.shape[0])

    if axis > values.shape[1]:
        raise ValueError("axis must be less than the number of columns")

    for id_ in range(axis):
        vals = values[:, id_].astype(float)
        pop, bins = np.histogram(vals, n_bins)
        ind = np.digitize(vals, bins)
        ind[ind > n_bins] = n_bins
        probabilities += 1.0 / (pop[ind - 1] + 1)

    probabilities = probabilities.max() - probabilities + 1
    probabilities /= probabilities.sum()

    np.random.seed(0)

    return values[
        np.random.choice(
            np.arange(values.shape[0]), replace=False, p=probabilities, size=size
        )
    ]


def int_to_k(number: float | int) -> str:
    """
    Convert a number to a string with a K or a M suffix.
    :param number: the number to convert.
    :return: the string with the suffix.
    """
    if not isinstance(number, (int, float)):
        raise TypeError("input must be numeric")

    if number > 1e6:
        return f"{number / 1e6:.1f}M"
    if number > 1e3:
        return f"{number / 1e3:.1f}k"

    return f"{round(number)}"


def format_float_string(number: float, delta: float) -> str:
    """
    Format a float number to a string,
    using the delta to determine the number of decimals.
    :param number: the number to format.
    :param delta: the delta to use for the formatting.
    :return: the formatted string.
    """
    delta = int(f"{delta:e}".split("e")[-1])
    number_e = f"{number:.3e}"
    decimal_place = int(number_e.split("e")[-1])

    if delta < 0:
        decimals = abs(delta)
    else:
        decimals = 0

    if abs(decimal_place) > 5:
        return number_e
    if decimals == 0:
        return f"{round(number)}"

    return f"{round(number, decimals)}"


def compute_histogram(dataframe: pd.DataFrame, bins: int = 50) -> pd.DataFrame:
    """
    Compute the histogram of a dataframe.
    :param dataframe: the dataframe to compute the histogram.
    :param bins: the number of bins to use.
    :return: the histogram dataframe.
    """
    # verify that the dataframe is a dataframe
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("'dataframe' must be a pandas DataFrame.")

    # change to dataframe to  histogram dataframe
    histogram = dataframe.groupby(pd.cut(dataframe.data, bins)).sum()
    histogram.rename(columns={"data": "bin_center"}, inplace=True)
    histogram["bin_center"] = [
        (_interval.left + _interval.right) * 0.5 for _interval in histogram.index
    ]

    return histogram


def dataframe_to_histogram(dataframe: pd.DataFrame, nb_bins: int = 50) -> tuple:
    """
    Convert a dataframe to a histogram dataframe.
    :param dataframe: the dataframe to convert.
    :param nb_bins: the number of bins to use.
    :return: a tuple containing the histogram dataframe and positive
    and negative count.
    """
    # verify that the dataframe is a dataframe
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("'dataframe' must be a pandas DataFrame.")

    # verify that the desired columns are in the dataframe
    if any(
        column not in dataframe.columns
        for column in ["data", "positive", "negative", "train", "test"]
    ):
        raise KeyError(
            "One of the columns ['data', 'positive', 'negative',\
'train', 'test'] is missing in 'dataframe'."
        )

    # get the number of unique data of the dataframe
    unique_data = dataframe.data.unique()
    nb_bins = min(nb_bins, len(unique_data))

    # change the columns of the dataframe
    dataframe = dataframe.copy()
    dataframe["train_positive"] = dataframe.train * dataframe.positive
    dataframe["test_positive"] = dataframe.test * dataframe.positive
    dataframe["train_negative"] = dataframe.train * dataframe.negative
    dataframe["test_negative"] = dataframe.test * dataframe.negative
    dataframe.drop(columns=["train", "test"], inplace=True)

    # change to dataframe to  histogram dataframe
    histogram = compute_histogram(dataframe, bins=nb_bins)
    positive_sum = int(histogram.positive.sum())
    negative_sum = int(histogram.negative.sum())

    # get the percentage between positive and negative of whole histogram
    histogram.positive /= histogram.positive.sum() / 100
    histogram.negative /= histogram.negative.sum() / 100
    histogram.train_positive /= histogram.train_positive.sum() / 100
    histogram.test_positive /= histogram.test_positive.sum() / 100
    histogram.train_negative /= histogram.train_negative.sum() / 100
    histogram.test_negative /= histogram.test_negative.sum() / 100

    # get the ratio between positive and negative
    histogram.sort_values("bin_center", inplace=True)
    histogram["bin"] = np.arange(0, nb_bins).astype(int)

    return histogram, positive_sum, negative_sum


def grid_resampling(
    points: pd.DataFrame, voxel_size: float, tree: cKDTree | None = None
) -> pd.Index:
    """
    Re-sample a point clouds based on a distance between points.
    :param points: the points to sample.
    :param voxel_size: the distance between points.
    :param tree: the kdtree to use for the sampling.
    :return: the sampled points.
    """

    non_empty_voxel_keys, inverse, nb_pts_per_voxel = np.unique(
        ((points.values - np.min(points.values, axis=0)) // voxel_size).astype(int),
        axis=0,
        return_inverse=True,
        return_counts=True,
    )

    avg = csr_matrix(
        (np.ones(len(points)), (inverse, np.arange(len(points)))),
        shape=(len(non_empty_voxel_keys), len(points)),
    )

    barycenters = avg @ points.values / nb_pts_per_voxel[:, None]

    if tree is None:
        tree = cKDTree(points.values)

    _, ind = tree.query(barycenters, k=1)

    return points.iloc[ind].index


def get_min_mean(points: pd.DataFrame) -> float:
    """
    Get the minimum mean distance of closest point for points.
    :param points: the points to compute the distance.
    :return: the minimum mean distance.
    """
    tree = cKDTree(points.values)
    dist, _ = tree.query(points.values, k=2)

    return dist[:, 1].mean()


def get_geoh5py_coordinates(geoh5py_object: ObjectBase) -> tuple:
    """
    Get the vertices of a geoh5py object.
    :param geoh5py_object: the geoh5py object to get the vertices from.
    :return: a tuple containing the vertices and the association.
    """
    vertices = None
    association = None
    # prepare the association of the data
    if hasattr(geoh5py_object, "centroids"):
        association = "CELL"
        vertices = getattr(geoh5py_object, "centroids")
    elif hasattr(geoh5py_object, "vertices"):
        association = "VERTEX"
        vertices = getattr(geoh5py_object, "vertices")
    if vertices is None:
        raise ValueError("Geoh5py Objects 'vertices' is None")

    # verify the database and the geoh5py object have the same vertices
    vertices = pd.DataFrame(dict(zip(["x", "y", "z"], vertices.T)))

    return vertices, association


def balanced_sampling(target: pd.Series, mode: str = "under") -> pd.Index:
    """
    Random sample of the least represented class.
    :param target: the target to sample.
    :param mode: the mode of the sampling ('under' or 'over').
    :return: the indexes of the sampled features and target.
    """
    if not isinstance(target, pd.Series):
        raise TypeError("'target' must be a pandas Series.")

    # count the number of sample of unique in target
    unique, counts = np.unique(target.values, return_counts=True)

    if len(unique) <= 1:
        return target.index

    # get the minimum number of sample and the corresponding class
    if mode == "under":
        count = np.min(counts)
        class_ = unique[np.argmin(counts)]
        replace = False
    elif mode == "over":
        count = np.max(counts)
        class_ = unique[np.argmax(counts)]
        replace = True
    else:
        raise ValueError(f"Unknown mode '{mode}', must me 'over' or 'under.")

    kept_indexes = [target[target == class_].index]
    for class_ in unique[unique != class_]:
        np.random.seed(42)
        kept_indexes.append(
            target[target == class_].index[
                np.random.choice(
                    target[target == class_].index.shape[0], count, replace=replace
                )
            ]
        )

    # merge the indexes
    return pd.Index(np.concatenate(kept_indexes))


def split_by_columns(
    function: str | list, columns: list, name_dataframe: str = "inputs"
) -> list:
    """
    Split a string function by columns name.
    :param function: the function to split.
    :param columns: the columns to split the function by.
    :param name_dataframe: the name of the dataframe to add to the columns.
    :return: the split function.
    """
    function = copy(function)
    if isinstance(function, str):
        function = [function]
    if not isinstance(function, list):
        raise TypeError("'function' must be a string or a list of string.")

    for column in sorted(columns, key=len, reverse=True):
        new_sub_function = []
        for sub_function in function:
            if name_dataframe not in sub_function:
                splits = sub_function.split(column)
                if len(splits) > 1:
                    for word in splits[:-1]:
                        new_sub_function += [word] + [f"{name_dataframe}['{column}']"]
                    new_sub_function += [splits[-1]]
                else:
                    new_sub_function += splits
            else:
                new_sub_function += [sub_function]
        function = new_sub_function

    return function


def split_by_chars(
    function: str | list, chars: str | list, name_dataframe: str = "inputs"
) -> list:
    """
    Split a string function by chars.
    :param function: the function to split.
    :param chars: the chars to split the function by.
    :param name_dataframe: the name of the dataframe to add to the columns.
    :return: the split function.
    """
    function = copy(function)
    if isinstance(function, str):
        function = [function]
    if not isinstance(function, list):
        raise TypeError("'function' must be a string or a list of string.")

    for char in chars:
        new_sub_function = []
        for sub_function in function:
            if name_dataframe not in sub_function:
                splits = sub_function.split(char)
                if len(splits) > 1:
                    for word in splits[:-1]:
                        new_sub_function += [word] + [char]
                    new_sub_function += [splits[-1]]
                else:
                    new_sub_function += splits
            else:
                new_sub_function += [sub_function]
        function = new_sub_function

    return function


def verify_function(
    function: list, columns: list, chars: list | str, name_dataframe="inputs"
):
    """
    Verify if the function is valid.
    :param function: the function to verify.
    :param columns: the columns the function can contain.
    :param chars: the chars the function can contain.
    :param name_dataframe: the name of the dataframe to add to the columns.
    """

    if not isinstance(function, list):
        raise TypeError("'function' must be a list of string.")

    columns_test = [f"{name_dataframe}['{column}']" for column in columns]
    for word in function:
        if word not in chars and not is_digit(word) and word not in columns_test:
            raise KeyError(
                f"The character chain : {word} is not a recognize operator"
                + f"({chars}), a digit nor a column."
            )


def extract_dataframe_from_object(
    my_object: ObjectBase, ignore_features: list[str]
) -> pd.DataFrame:
    """
    Extract a dataframe from a geoh5py object.

    :param my_object: The geoh5py object to extract the dataframe from.
    :param ignore_features: The list of features to rename.

    :return: The dataframe extracted from the geoh5py object.
    """
    with fetch_active_workspace(my_object.workspace, mode="r"):
        # verify the data type and convert if needed
        vertices, _ = get_geoh5py_coordinates(my_object)

        # get all the data of the object
        all_data: dict[str, np.ndarray] = {}
        for name in my_object.get_data_list():
            temp_data = my_object.get_data(name)[0]

            if not isinstance(temp_data, NumericData) or temp_data.values is None:
                continue

            subdata = temp_data.values.copy()

            # remove the value for memory efficiency
            setattr(temp_data, "_values", None)

            name = rename_if_inlist(name, ignore_features + list(all_data.keys()))
            all_data[name] = subdata

        # create the dataframe
        return pd.DataFrame({**vertices, **all_data})


def special_round(number: float) -> float:
    """
    Rounds a number to the nearest significant figure after the first non-zero digit.

    :params number: The number to be rounded.

    returns: The rounded number.
    """
    if number == 0:
        return 0

    # Determine the first significant digit's position
    first_significant_digit = math.floor(math.log10(abs(number)))

    # Calculate the number of decimal places to round to
    decimal_places = -first_significant_digit if first_significant_digit < 0 else 0

    # Increase decimal places to round to the next significant figure
    decimal_places += 1

    # Round the number
    rounded_number = round(number, decimal_places)

    return rounded_number


def add_date_to_name(name: str) -> str:
    """
    Prepare the name of the text to add to the database.

    :param name: The name of the text.
    :param application_name: The name of the application.

    :return: The new name
    """
    name = str(name) + "_" + pd.Timestamp.now().strftime("%c")

    name = name.replace(" ", "_").replace(":", "_")

    return name
