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
from PySide2.QtCore import QThread, Signal

import targeting_workflow.database.database_utils as dbu
from targeting_workflow.gui.config import PARAMETERS
from targeting_workflow.predictors.base_predictor import BasePredictor
from targeting_workflow.predictors.knowledge_predictor import KnowledgePredictor
from targeting_workflow.predictors.random_forest import RandomForest


class RunModelThread(QThread):
    """Thread to run the model in the background."""

    # define signals to be emitted
    predictor_signal = Signal(BasePredictor)
    error_ocurred = Signal(Exception, name="errorOcurred")

    def __init__(self, database, method, function, columns):
        super().__init__()
        self.database = database
        if method == "Random Forest":
            self.predictor = RandomForest(
                database,
                database.in_use_features,
                standardize_input=False,
                random_state=42,
            )
        elif method == "Knowledge Driven":
            # compute as a predictor
            self.predictor = KnowledgePredictor(
                database,
                columns,
                function=function,
                divide_chars="+-/*()<>",
                standardize_input=False,
            )

    def run(self):
        print("running predictor")
        # verify the predictor .name is in PARAMETERS
        if self.predictor.name in PARAMETERS:
            # run a random search
            self.predictor.grid_parameters_search(PARAMETERS[self.predictor.name])
        else:
            self.predictor.fit()

        probability = self.predictor.probability
        self.database.set_features(
            probability,
            ignore=True,
            metadata={
                "parameters": self.predictor.best_parameters,
                "score": self.predictor.score,
                "feature_importance": self.predictor.feature_importance.mean(
                    axis=0
                ).to_dict(),
            },
        )

        # Run feature importance calculation before finishing the thread
        self.predictor.compute_feature_importance()
        print("predictor calculated.")
        self.predictor_signal.emit(self.predictor)


class GroupDataThread(QThread):
    """Thread to group data in the background."""

    error_occurred = Signal(Exception, name="errorOccurred")

    def __init__(self, database, distance):
        super().__init__()
        self.database = database
        self.distance = distance

    def run(self):
        # define geographical groups
        dbu.find_cross_validation(self.database, self.distance)
        dbu.assign_cross_validation(self.database)

        # balance the dataframe and assign training and testing groups
        dbu.balance(self.database, self.database.in_use_features)
        dbu.auto_split_train_test(self.database)

    def stop(self):
        self.terminate()
