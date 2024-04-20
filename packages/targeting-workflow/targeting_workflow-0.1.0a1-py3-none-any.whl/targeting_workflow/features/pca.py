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

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA as SkPCA

from ..features.base_feature import BaseFeature


class PCA(BaseFeature):
    _kernel_type = SkPCA

    def explained_variance(self, ratio: float) -> pd.DataFrame:
        """
        Get the components that explain a certain ratio of the variance.
        :param ratio: the ratio of the variance to explain.
        :return: the components that explain the ratio of the variance.
        """
        if not self.fitted:
            self.compute()

        explained = np.hstack(
            (0.0, np.cumsum(self.kernel.explained_variance_ratio_)[:-1])
        )

        return self.output.iloc[:, explained < ratio]  # type: ignore
