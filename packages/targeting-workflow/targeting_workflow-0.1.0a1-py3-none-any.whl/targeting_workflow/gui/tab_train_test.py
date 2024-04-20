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
# pylint: disable=import-error, duplicate-code
import warnings
from pathlib import Path

import targeting_workflow.database.database_plots as dbp
from targeting_workflow import assets_path
from targeting_workflow.gui.threads import GroupDataThread

PLOTLY_PATH = Path(assets_path() / "plotly" / "plotly-2.18.0.min.js")
warnings.filterwarnings("ignore")


class TabTrainTest:
    def __init__(self, main_window):
        """
        Initialize the train test tab.
        :param main_window: The parent widget of the main window
        """
        self.main_window = main_window
        self.ui_form = main_window.ui_form
        self.database = main_window.database

        self.ui_form.move_right_button.clicked.connect(self.move_item_right)
        self.ui_form.move_left_button.clicked.connect(self.move_item_left)

        # set default distance value 2x the minimum mean distance,
        # as minimum distance creates too many groups
        self.ui_form.distance_spinbox.setValue(
            self.main_window.database.min_mean_distance * 2
        )
        # connect the spinbox to the group_data method
        self.ui_form.distance_spinbox.valueChanged.connect(self.group_data)

        self.group_data_worker_thread = None

        self.group_data()

    def group_data(self):
        """Method to calculate the cross validation groups"""
        # alter widget visibility
        self.ui_form.progressBar.show()
        self.ui_form.label_groups.hide()
        self.main_window.toggle_buttons_enabled(False)

        # get user set distance from the slider
        distance = self.ui_form.distance_spinbox.value()

        # use a thread for long-running process
        self.group_data_worker_thread = GroupDataThread(self.database, distance)
        self.group_data_worker_thread.error_occurred.connect(
            self.main_window.error_occurred
        )
        self.group_data_worker_thread.finished.connect(self.group_data_finished)
        self.group_data_worker_thread.setTerminationEnabled(True)
        self.group_data_worker_thread.start()

    def group_data_finished(self):
        """Event to be fired when the group_data_worker_thread thread finishes running."""
        self.group_data_worker_thread = None
        self.ui_form.progressBar.hide()
        self.ui_form.label_groups.show()
        self.main_window.toggle_buttons_enabled(True)
        try:
            self.populate_train_test_lists()
            self.plot_data_groups()
        except AssertionError as error:
            self.main_window.error_occurred(f"{error}")
            self.ui_form.test_list.clear()
            self.ui_form.train_list.clear()
            self.ui_form.label_train.clear()
            self.ui_form.label_test.clear()
            self.ui_form.label_groups.clear()
            self.ui_form.examples_mapwidget.setHtml("")

    def move_item_left(self):
        """Moves item from the test list to the train list"""
        # get the list of selected indices as integers
        selected = [item.text() for item in self.ui_form.test_list.selectedItems()]
        if not selected:
            print("Nothing Selected")
            return

        residual = [
            i for i in self.database.cross_validation_test if str(i) not in selected
        ]

        # Don't allow user to empty the testing set
        if not residual:
            self.main_window.error_occurred(
                "Cannot remove all groups from the testing set"
            )
            return

        # remove selected from the testing set
        self.database.cross_validation_test = residual

        # add selected to the training set
        cv_train = self.database.cross_validation_train
        cv_train.extend([int(float(i)) for i in selected])
        self.database.cross_validation_train = cv_train
        self.populate_train_test_lists()
        self.plot_data_groups()

    def move_item_right(self):
        """Moves item from the train list to the test list"""
        # get the list of selected indices as integers
        selected = [item.text() for item in self.ui_form.train_list.selectedItems()]
        if not selected:
            return

        residual = [
            i for i in self.database.cross_validation_train if str(i) not in selected
        ]

        # Don't allow user to empty the training set
        if not residual:
            self.main_window.error_occurred(
                "Cannot remove all groups from the training set"
            )
            return

        # remove selected from the training set
        self.database.cross_validation_train = residual

        # add selected to the testing set
        cv_test = self.database.cross_validation_test
        cv_test.extend([int(float(i)) for i in selected])
        self.database.cross_validation_test = cv_test
        self.populate_train_test_lists()
        self.plot_data_groups()

    def plot_data_groups(self):
        """Method to plot the data groups map"""
        fig = dbp.plot_data_groups(self.database, folder=None)
        html_file = Path(self.main_window.temp_dir) / "groups.html"
        config = {
            "modeBarButtonsToRemove": [
                "toImage",
                "zoomIn2d",
                "zoomOut2d",
                "autoscale",
                "orbitRotation",
            ],
            "displaylogo": False,
        }
        fig.write_html(html_file, include_plotlyjs=PLOTLY_PATH.as_uri(), config=config)
        self.ui_form.examples_mapwidget.setUrl(html_file.as_uri())

    def populate_train_test_lists(self):
        """Method to populate the train test split lists"""
        self.ui_form.train_list.clear()
        cv_train = self.database.cross_validation_train
        if cv_train is not None:
            cv_train.sort()
            self.ui_form.train_list.addItems(list(map(str, cv_train)))

        self.ui_form.test_list.clear()
        cv_test = self.database.cross_validation_test
        if cv_test is not None:
            cv_test.sort()
            self.ui_form.test_list.addItems(list(map(str, cv_test)))

        self.update_pct_labels()

    def update_pct_labels(self):
        """Method to update the percentage labels for the train/test split"""

        train_cv = [
            int(float(self.ui_form.train_list.item(idx).text()))
            for idx in range(self.ui_form.train_list.count())
        ]
        test_cv = [
            int(float(self.ui_form.test_list.item(idx).text()))
            for idx in range(self.ui_form.test_list.count())
        ]

        percentage_cv = self.database.cross_validation_representation()

        # Filter the DataFrame for train_cv and test_cv indices and sum their percentages
        train_percentage_sum = percentage_cv.loc[train_cv].sum()
        test_percentage_sum = percentage_cv.loc[test_cv].sum()

        # get the sum of train percentage cv
        self.ui_form.train_pct_label.setText(f"{train_percentage_sum:.2f}%")
        self.ui_form.test_pct_label.setText(f"{test_percentage_sum:.2f}%")
        self.ui_form.label_groups.setText(f"{percentage_cv.shape[0]} groups")
