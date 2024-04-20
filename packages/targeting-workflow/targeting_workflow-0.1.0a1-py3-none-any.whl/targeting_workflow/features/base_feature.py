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

from copy import copy
from warnings import warn

import pandas as pd

from ..shared.base_compute import BaseCompute


class BaseFeature(BaseCompute):
    @property
    def output(self) -> pd.DataFrame | None:
        """
        Return the output of the feature computed by the kernel.
        :return: the computed outputs.
        """
        if self._output is None:
            self.compute()

        return copy(self._output)

    def compute(self):
        """
        Compute the results.
        """
        if self.kernel is None:
            warn("The kernel is not set yet.")
            return

        output = self.kernel.fit_transform(self.inputs)

        nb_columns = 1
        if len(output.shape) > 1:
            nb_columns = output.shape[1]

        names = [f"{self.name}_{i}" for i in range(nb_columns)]
        self._output = pd.DataFrame(output, index=self.inputs.index, columns=names)
        self.fitted = True
