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

from ..predictors.base_predictor import BasePredictor
from ..shared.knowledge_driven import KnowledgeKernel


class KnowledgePredictor(BasePredictor):
    _kernel_type = KnowledgeKernel

    def set_kernel(self, **kernel_kwargs):
        """
        Set the kernel.
        """
        self.kernel = self._kernel_type(self.inputs.columns.tolist(), **kernel_kwargs)
        self._best_parameters = kernel_kwargs
