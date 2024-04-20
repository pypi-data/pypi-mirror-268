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

from PySide2.QtWidgets import QWidget

import targeting_workflow.database.database_plots as dbp
from targeting_workflow import assets_path

PLOTLY_PATH = Path(assets_path() / "plotly" / "plotly-2.18.0.min.js")


class TabPropertyEDA:
    def __init__(self, main_window: QWidget):
        """
        Initialize the property EDA tab.
        :param main_window: The parent widget of the main window
        """
        self.run_distance_accuracy_worker_thread = None
        self.main_window = main_window
        self.ui_form = main_window.ui_form
        self.ui_form.eda_property_combobox.addItems(
            self.main_window.database.in_use_features
        )
        # Set the current index to -1 to clear the combobox
        self.ui_form.eda_property_combobox.setCurrentIndex(-1)

        self.ui_form.eda_property_combobox.currentIndexChanged.connect(
            self.plot_eda_property
        )

    def plot_eda_property(self):
        """Method to produce the eda plot based on the property selected in the combobox"""
        selected_feature = self.ui_form.eda_property_combobox.currentText()
        fig = dbp.plot_histogram_feature(
            self.main_window.database, selected_feature, folder=None
        )
        html_file = Path(self.main_window.temp_dir) / "histogram.html"
        config = {
            "modeBarButtonsToRemove": [
                "toImage",
                "zoomIn2d",
                "zoomOut2d",
                "autoscale",
            ],  # 'zoom2d',
            "displaylogo": False,
        }
        fig.write_html(html_file, include_plotlyjs=PLOTLY_PATH.as_uri(), config=config)
        self.ui_form.property_web_engine.setUrl(html_file.as_uri())
