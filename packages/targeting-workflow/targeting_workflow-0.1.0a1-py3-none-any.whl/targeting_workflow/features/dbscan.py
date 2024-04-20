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

import pandas as pd
from sklearn.cluster import DBSCAN as SkDBSCAN

from ..features.base_feature import BaseFeature


class DBSCAN(BaseFeature):
    _kernel_type = SkDBSCAN

    def compute(self):
        """
        Redefine compute as DBSCAN use fit_predict instead of fit_transform.
        """
        output = self.kernel.fit_predict(self.inputs)
        self._output = pd.DataFrame(
            output, index=self.inputs.index, columns=[self.name]
        )
        self.fitted = True
