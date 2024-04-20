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

import numpy as np
import pandas as pd

from ..features.base_feature import BaseFeature
from ..shared.knowledge_driven import KnowledgeKernel


class KnowledgeFeature(BaseFeature):
    _kernel_type = KnowledgeKernel

    def set_kernel(self, **kernel_kwargs):
        """
        Set the kernel.
        """
        self.kernel = self._kernel_type(self.inputs.columns.tolist(), **kernel_kwargs)

    def compute(self):
        """
        Compute the results.
        """
        output = self.kernel.predict_proba(self.inputs)[:, 1][:, np.newaxis]

        self._output = pd.DataFrame(
            data=output, index=self.inputs.index, columns=[self.name]
        )

        self.fitted = True
