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
from pathlib import Path

import numpy as np
from geoh5py.ui_json import monitored_directory_copy
from geoh5py.workspace import Workspace
from pandas import DataFrame
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QStyledItemDelegate, QTableWidgetItem

from targeting_workflow import assets_path
from targeting_workflow.database.export import export_data
from targeting_workflow.gui.threads import RunModelThread
from targeting_workflow.predictors.base_predictor import BasePredictor
from targeting_workflow.shared import plots

PLOTLY_PATH = Path(assets_path() / "plotly" / "plotly-2.18.0.min.js")


class ReadOnlyDelegate(QStyledItemDelegate):
    """
    ReadOnlyDelegate class that inherits from QStyledItemDelegate and
    overrides the createEditor() method to return None.

    This effectively disables editing for the column that the delegate is applied to.
    """

    def createEditor(self, *_):  # pylint: disable=invalid-name
        """Override the existing method of `:obj:PySide2.QtWidgets.QStyledItemDelegate`
        to set as readonly"""
        return


class ModellingTab:
    def __init__(self, main_window):
        """
        Initialize the modelling tab.
        :param main_window: The parent widget of the main window.
        """
        self.run_model_worker_thread = None
        self.main_window = main_window
        self.main_window.ui_form.score_label.hide()
        self.main_window.ui_form.export_to_ga_button.clicked.connect(self.export_to_ga)
        self.main_window.ui_form.run_button.clicked.connect(self.run_model)
        self.populate_table_widget()

        # hide the Index Overlay tab
        self.main_window.ui_form.modelling_tabs.setTabVisible(0, False)

        # Connect combobox to enable index overlay tab
        self.main_window.ui_form.predictor_combo_box.currentIndexChanged.connect(
            self.enable_index_overlay_tab
        )

    def enable_index_overlay_tab(self):
        """
        Method to enable the index overlay tab
        """
        self.populate_table_widget()

        if (
            self.main_window.ui_form.predictor_combo_box.currentText()
            == "Knowledge Driven"
        ):
            self.main_window.ui_form.modelling_tabs.setTabVisible(0, True)
            self.main_window.ui_form.modelling_tabs.setCurrentIndex(0)
        else:
            self.main_window.ui_form.modelling_tabs.setTabVisible(0, False)

    def export_to_ga(self):
        """Method to export created features to the geoh5 object"""
        print(
            f"Exporting feature '{self.main_window.database.created}' to "
            f"{self.main_window.geoh5_object.name}"
        )

        out_ws = monitored_directory_copy(
            self.main_window.monitoring_directory, self.main_window.geoh5_object
        )

        with Workspace(out_ws) as w_s:
            out_obj = w_s.get_entity(self.main_window.geoh5_object.name)[0]
            export_data(
                out_obj,
                self.main_window.database,
                self.main_window.database.created,
            )

        print("Export successful.")

    def get_index_overlay_values(self) -> tuple:
        """
        Method to get the index overlay values from the table widget.
        """
        output_string, columns = "", []

        table_widget = self.main_window.ui_form.tableWidget

        # Read every row of the table widget
        for row in range(table_widget.rowCount()):
            # Get the property name
            column = table_widget.item(row, 0).text()

            # Get the min value
            min_value = table_widget.item(row, 1).text()

            # Get the max value
            max_value = table_widget.item(row, 2).text()

            # Get the weight value
            weight = table_widget.item(row, 3).text()

            if float(weight) > 0:
                # add to output string
                output_string += (
                    f"({column}>{min_value})*({column}<{max_value})*{weight}+"
                )
                columns.append(column)

        return output_string[:-1], columns

    def plot_feature_importance(self, feature_importance: DataFrame):
        """
        Method to plot the feature importance and place in window
        :param feature_importance: feature importance dataframe to plot
        """
        # Populate the feature importance
        fig = plots.plot_feature_importance(feature_importance, folder="")
        html_file = Path(self.main_window.temp_dir) / "feature_importance.html"
        config = {
            "modeBarButtonsToRemove": ["toImage", "zoomIn2d", "zoomOut2d", "autoscale"],
            "displaylogo": False,
        }
        fig.write_html(html_file, include_plotlyjs=PLOTLY_PATH.as_uri(), config=config)
        self.main_window.ui_form.feature_importance_web_engine.setUrl(
            html_file.as_uri()
        )

    def plot_confusion_matrix(self, confusion_matrix: np.ndarray):
        """
        Method to plot the feature importance and place in window
        :param confusion_matrix: confusion matrix array to plot
        """
        # Populate the feature importance
        fig = plots.plot_confusion_matrix(confusion_matrix, folder="")
        html_file = Path(self.main_window.temp_dir) / "confusion_matrix.html"
        config = {
            "modeBarButtonsToRemove": ["toImage", "zoomIn2d", "zoomOut2d", "autoscale"],
            "displaylogo": False,
        }
        fig.write_html(html_file, include_plotlyjs=PLOTLY_PATH.as_uri(), config=config)
        self.main_window.ui_form.confusion_matrix_web_engine.setUrl(html_file.as_uri())

    def plot_roc_curve(self, roc_curve: DataFrame):
        """
        Method to plot the feature importance and place in window
        :param roc_curve: roc curve dataframe to plot
        """
        # Populate the feature importance
        fig = plots.plot_roc_curve(roc_curve, folder="")
        html_file = Path(self.main_window.temp_dir) / "roc_curve.html"
        config = {
            "modeBarButtonsToRemove": ["toImage", "zoomIn2d", "zoomOut2d", "autoscale"],
            "displaylogo": False,
        }
        fig.write_html(html_file, include_plotlyjs=PLOTLY_PATH.as_uri(), config=config)
        self.main_window.ui_form.roc_curve_web_engine.setUrl(html_file.as_uri())

    def populate_table_widget(self):
        """Function to populate the knowledge driven table, from in-use features."""
        self.main_window.ui_form.tableWidget.setColumnWidth(0, 300)
        self.main_window.ui_form.tableWidget.setColumnWidth(1, 30)
        self.main_window.ui_form.tableWidget.setColumnWidth(2, 30)
        self.main_window.ui_form.tableWidget.setColumnWidth(3, 80)

        # fill with zeros for now, TODO: set min, max values from data stats
        self.main_window.ui_form.tableWidget.setRowCount(
            len(self.main_window.database.in_use_features)
        )
        for row, prop in enumerate(self.main_window.database.in_use_features):
            self.main_window.ui_form.tableWidget.setItem(row, 0, QTableWidgetItem(prop))
            self.main_window.ui_form.tableWidget.setItem(
                row, 1, QTableWidgetItem(str(0))
            )
            self.main_window.ui_form.tableWidget.setItem(
                row, 2, QTableWidgetItem(str(0))
            )
            self.main_window.ui_form.tableWidget.setItem(
                row, 3, QTableWidgetItem(str(0))
            )

        delegate = ReadOnlyDelegate()
        self.main_window.ui_form.tableWidget.setItemDelegateForColumn(0, delegate)

    def run_model(self):
        """Method to run model"""
        # get the selected predictor method to run
        method = self.main_window.ui_form.predictor_combo_box.currentText()
        function, columns = self.get_index_overlay_values()

        if len(self.main_window.database.in_use) == 0:
            self.main_window.error_occurred("No training data are selected.")
            return
        if (
            method == "Random Forest"
            and len(self.main_window.database.in_use_features) == 0
        ):
            self.main_window.error_occurred(
                "Please select at least one feature to run Random Forest"
            )
            return
        if method == "Knowledge Driven" and len(columns) == 0:
            self.main_window.error_occurred(
                "Please select at least one feature to run Index Overlay"
            )
            return

        self.main_window.ui_form.run_progress_bar.show()
        self.main_window.toggle_buttons_enabled(False)

        # use a thread for long-running process
        self.run_model_worker_thread = RunModelThread(
            self.main_window.database, method, function, columns
        )
        self.run_model_worker_thread.predictor_signal.connect(
            self.run_model_worker_finished, Qt.QueuedConnection
        )
        self.run_model_worker_thread.error_ocurred.connect(
            self.main_window.error_occurred
        )

        self.run_model_worker_thread.start()

    def run_model_worker_finished(self, predictor: BasePredictor):
        """
        Method to run when the run model button is clicked
        :param predictor: the predictor object
        """
        # self.run_model_worker_thread = None
        self.main_window.ui_form.score_label.setText(f"Score: {predictor.score:.2f}")
        self.main_window.ui_form.score_label.setVisible(True)

        self.main_window.ui_form.run_progress_bar.hide()
        self.main_window.toggle_buttons_enabled(True)
        self.plot_feature_importance(predictor.feature_importance)
        self.plot_confusion_matrix(predictor.confusion_matrix)
        self.plot_roc_curve(predictor.roc_curve())
