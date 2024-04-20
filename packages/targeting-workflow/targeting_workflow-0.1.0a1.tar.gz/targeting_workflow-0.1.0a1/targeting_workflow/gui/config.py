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


PARAMETERS = {
    "RandomForest": {
        "n_estimators": [50, 100, 300],
        "max_depth": [5, 10, 25],
        "min_samples_split": [0.05, 0.1, 0.2],
        "min_samples_leaf": [0.01, 0.05, 0.1],
        "criterion": ["entropy"],
        "bootstrap": [True],
        "max_features": ["sqrt"],
        "n_jobs": [-1],
    }
}
