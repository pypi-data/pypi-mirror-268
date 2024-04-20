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

from abc import ABC
from warnings import warn

import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.preprocessing import StandardScaler

from ..database.database import Database


class BaseCompute(ABC):
    _kernel_type: type | None = None

    def __init__(
        self,
        database: Database,
        inputs: list | str,
        standardize_input: bool = False,
        scaler: TransformerMixin = StandardScaler(),
        **kernel_kwargs,
    ):
        """
        Base class for any sklearn methods aims to transform an output.

        :param database: the Database to use.
        :param inputs: the inputs to use. None
        :param standardize_input: if the data has to be standardized.
        :param scaler: the Scaler function of the data
        :param kernel_kwargs: the arguments to pass to the kernel.
        """
        self._standardize_input = standardize_input
        self.scaler = scaler
        self.database = database
        self.inputs = inputs  # type: ignore

        self._kernel = None  # type: ignore
        self._output: pd.DataFrame | None = None
        self._fitted: bool = False

        self.set_kernel(**kernel_kwargs)

    def reset(self):
        """
        Reset the results.
        """
        self.fitted = False

    @property
    def name(self) -> str:
        """
        Get the name of the class.
        """
        return self.__class__.__name__

    @property
    def database(self) -> Database:
        """
        Get the database used to compute the feature.
        """
        return self._database

    @database.setter
    def database(self, database: Database):
        """
        Set the database used to compute the feature.
        Cannot verify type because of circular import.
        """
        if not isinstance(database, Database):
            raise TypeError("The database must be a Database.")

        self._database = database

    def set_kernel(self, **kernel_kwargs):
        """
        Set the kernel used to compute the feature.

        :param kernel_kwargs: the arguments to pass to the kernel.
        """
        if not callable(self._kernel_type):
            raise NotImplementedError("The current class is a base class.")

        self.kernel = self._kernel_type(**kernel_kwargs)  # pylint: disable=not-callable

    @property
    def kernel(self):
        """
        Get the kernel used to compute the feature.
        """
        if self._kernel is None:
            warn("No kernel is set, return None.")

        return self._kernel

    @kernel.setter
    def kernel(self, kernel):
        """
        Set the kernel used to compute the feature.
        # todo: add checker there (fit, etc)
        """
        self._kernel = kernel

    @property
    def fitted(self) -> bool:
        """
        Return if the kernel has been fitted.
        """
        return self._fitted

    @fitted.setter
    def fitted(self, fitted: bool):
        """
        Set if the kernel has been fitted.
        """
        if not isinstance(fitted, bool):
            raise TypeError("The fitted must be a boolean.")

        self._fitted = fitted

    @property
    def inputs(self) -> pd.DataFrame:
        """
        Get the inputs used to compute the feature.
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs: list | str):
        """
        Set the inputs used to compute the feature.
        """
        if len(inputs) == 0:
            raise ValueError("The inputs must not be empty.")

        inputs_dataframe = self.database.get_features(inputs, self.database.in_use)

        if self._standardize_input:
            inputs_dataframe = self.scale(inputs_dataframe)

        self._inputs = inputs_dataframe

        self.reset()

    @property
    def scaler(self) -> TransformerMixin:
        """
        the Scaler function of the data
        """
        return self._scaler

    @scaler.setter
    def scaler(self, scaler: TransformerMixin):
        """
        Set the Scaler function of the data
        """
        # Check if the scaler provided has the fit_transform method
        if not hasattr(scaler, "fit_transform"):
            raise TypeError("The scaler must have a fit_transform method.")

        self._scaler = scaler

    def scale(self, inputs: np.ndarray | pd.DataFrame) -> np.ndarray | pd.DataFrame:
        """
        Scale the input data using the scaller.

        :param inputs: the input data to scale

        :return: the scaled input data.
        """
        scaled = self.scaler.fit_transform(X=inputs)

        return pd.DataFrame(scaled, columns=inputs.columns, index=inputs.index)
