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
# pylint: disable=eval-used


from __future__ import annotations

from typing import Callable
from warnings import warn

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score

from ..shared.utils import normalize, split_by_chars, split_by_columns, verify_function


class KnowledgeKernel:
    def __init__(
        self,
        columns: list[str],
        function: str,
        scorer: Callable = f1_score,
        divide_chars: str | list[str] = "+-/*()",
        to_normalize: bool = True,
    ):
        """
        Initialize the knowledge kernel using a string function on a dataframe.
        :param columns: The columns to check in the function and in the dataframe used latter.
        :param function: The function to be used in string format.
        :param scorer: The scorer function to be used in the function returning a score.
        :param divide_chars: The only characters allows in the string used to split it.
        :param to_normalize: If the function should be normalized.
        """
        self.columns = columns
        self.divide_chars = divide_chars
        self.function = function
        self.scorer = scorer
        self.normalize = to_normalize

        self._threshold: None | float = None

    def fit(self, inputs: pd.DataFrame, targets: pd.Series):
        """
        Fit the model - get a threshold for the classification based on the probability.

        :param inputs: The dataframe to be used (must contain the columns).
        :param targets: The targets to be used (must correspond to the dataframe index).
        """
        probability = self.predict_proba(inputs)[:, 1]
        target = self.check_target(targets, inputs)

        score_best, threshold_best = -1, 0
        for threshold_temp in np.arange(0, 1, 0.01):
            predict_temp = np.where(probability > threshold_temp, 1, 0)
            score_temp = self.scorer(predict_temp, target)
            if score_temp > score_best:
                score_best = score_temp
                threshold_best = threshold_temp

        self.threshold = threshold_best

    def predict_proba(self, inputs: pd.DataFrame) -> np.array:
        """
        Predict the probability of the target.
        :param inputs: The inputs to be used.
        :return: The probability of the target,
        a dataframe containing only 0 values if an error is raised.
        """
        inputs = self.check_input(inputs)

        try:
            probability = eval(self.function).astype(float)
        except Exception as exception:  # pylint: disable=broad-exception-caught
            warn(
                f"The function did not worked, raises the following error: {exception}."
            )
            return np.array(np.zeros((len(inputs), 2)))

        probability = np.stack(
            (np.nanmax(probability.values) - probability.values, probability.values),
            axis=1,
        )

        if self.normalize:
            return normalize(probability)
        return probability

    def score(self, inputs: pd.DataFrame, targets: pd.Series) -> float:
        """
        Score the model.
        :param inputs: The inputs to be used.
        :param targets: The targets to be used.
        :return: The score of the model.
        """
        if self.threshold is None:
            raise AssertionError("The model must be fitted before predicting.")

        return self.scorer(self.predict(inputs), self.check_target(targets, inputs))

    def predict(self, inputs: pd.DataFrame) -> np.array:
        """
        Predict the target.
        :param inputs: The inputs to be used.
        :return: The target as a np.array.
        """
        inputs = self.check_input(inputs)

        if self.threshold is None:
            raise AssertionError("The model must be fitted before predicting.")

        return np.where(self.predict_proba(inputs)[:, 1] > self.threshold, 1, 0)

    def check_input(self, inputs: pd.DataFrame) -> pd.DataFrame:
        """
        Check the input type.
        :param inputs: The inputs to be checked.
        :return: The inputs as a dataframe.
        """
        if not isinstance(inputs, pd.DataFrame):
            raise TypeError("The inputs must be a pandas dataframe.")

        if not set(inputs.columns.tolist()).issubset(self.columns):
            raise KeyError("The columns of the inputs must be used by the function.")

        return inputs

    def check_target(self, targets: pd.Series, inputs: pd.DataFrame) -> pd.DataFrame:
        """
        Check the target type.
        :param targets: The targets to be checked.
        :param inputs: The inputs to be used.
        :return: The targets as a dataframe.
        """
        inputs = self.check_input(inputs)

        if not isinstance(targets, pd.Series):
            raise TypeError("The target must be a pandas series.")

        if not inputs.index.equals(targets.index):
            raise IndexError(
                "The index of the target must be the same as the dataframe."
            )

        return targets

    @property
    def divide_chars(self) -> str | list[str]:
        """
        The characters used to split the function.
        """
        return self._divide_chars

    @divide_chars.setter
    def divide_chars(self, value: str | list[str]):
        # verify value is a list of string
        if not isinstance(value, (list, str)):
            raise TypeError("The divide chars must be a list of string or a string.")

        if isinstance(value, list):
            if any(not isinstance(char, str) for char in value):
                raise TypeError(
                    "The divide chars must be a list of string or a string."
                )

        self._divide_chars = value

    @property
    def columns(self) -> list:
        """
        The columns used in the kernel.
        """
        return self._columns

    @columns.setter
    def columns(self, value: list):
        if not isinstance(value, list):
            raise TypeError("The columns must be a list.")

        self._columns = value

    @property
    def function(self) -> str:
        """
        The function used in the kernel.
        """
        return self._function

    @function.setter
    def function(self, function: str):
        """
        Transform the function and verify its correctness;
        Only the correct character chains are allowed :
        the columns, the digits and the divide chars.
        Example: "a + 1" => inputs['a'] + 1"
        :param function: The function to be used.
        """
        string_to_split = function.replace(" ", "")

        # Separate by the columns
        result_list = split_by_columns(string_to_split, self.columns, "inputs")

        # Separate by the divide chars
        result_list = split_by_chars(result_list, self.divide_chars, "inputs")

        # Verify the outputs
        verify_function(result_list, self.columns, self.divide_chars, "inputs")

        self._function = "".join(result_list)

    @property
    def threshold(self) -> float | None:
        """
        The threshold used in the kernel.
        """
        return self._threshold

    @threshold.setter
    def threshold(self, value: float):
        if not isinstance(value, float):
            raise TypeError("The threshold must be a float.")
        if value < 0 or value > 1:
            raise ValueError("The threshold must be between 0 and 1.")

        self._threshold = value

    @property
    def scorer(self):
        """
        The scorer used in the kernel.
        """
        return self._scorer

    @scorer.setter
    def scorer(self, value):
        # verify if the scorer is a callable function
        if not callable(value):
            raise TypeError("The scorer must be a callable function.")

        self._scorer = value

    @property
    def normalize(self):
        """
        The normalize function used in the kernel.
        """
        return self._normalize

    @normalize.setter
    def normalize(self, value):
        # verify if normalize is a boolean
        if not isinstance(value, bool):
            raise TypeError("The normalize must be a boolean.")

        self._normalize = value
