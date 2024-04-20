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

import warnings

import pandas as pd
import sklearn.cluster as sk

from ..features.base_feature import BaseFeature

warnings.filterwarnings("ignore")


class KMean(BaseFeature):
    _kernel_type = sk.KMeans

    @property
    def clustered(self) -> pd.DataFrame | None:
        """
        Get the clustering.

        :return: the clustering results of the KMean as DataFrame.
        """
        if not self.fitted:
            self.compute()

        return pd.DataFrame(
            self.kernel.labels_, index=self.output.index, columns=[self.name]  # type: ignore
        )

    @property
    def closest_to_centroids(self) -> list | None:
        """
        Get the closest centroids ids.

        :return: get the closest centroids ids.
        """
        return self.output.idxmin().to_list()  # type: ignore


class FastKMean(KMean):
    _kernel_type = sk.MiniBatchKMeans
