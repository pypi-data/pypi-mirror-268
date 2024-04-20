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
# pylint: disable=duplicate-code
import warnings
from pathlib import Path

import targeting_workflow.database.database_plots as dbp
from targeting_workflow import assets_path

PLOTLY_PATH = Path(assets_path() / "plotly" / "plotly-2.18.0.min.js")
warnings.filterwarnings("ignore")


class PropertySelection:
    def __init__(self, main_window):
        """
        Initialize the property selection tab.
        :param main_window: The parent widget of the main window
        """
        self.main_window = main_window
        self.database = main_window.database
        self.ui_form = main_window.ui_form

        # Select all features for the default correlation matrix
        self.ui_form.property_selection_list.addItems(self.database.in_use_features)
        self.ui_form.property_selection_list.selectAll()
        self.ui_form.update_plots_button.clicked.connect(self.plot_correlation_matrix)
        self.plot_correlation_matrix()

    def plot_correlation_matrix(self):
        """Method to plot the correlation matrix"""
        print("plotting correlation matrix")
        selected_properties = [
            i.text() for i in self.ui_form.property_selection_list.selectedItems()
        ]
        self.database.in_use_features = selected_properties

        fig = dbp.plot_correlation_matrix(
            self.database, selected_properties, folder=None
        )

        config = {
            "modeBarButtonsToRemove": [
                "toImage",
                "zoomIn2d",
                "zoomOut2d",
                "autoscale",
            ],  # 'zoom2d',
            "displaylogo": False,
        }

        self.main_window.tab_modelling.enable_index_overlay_tab()

        html_file = Path(self.main_window.temp_dir) / "corr.html"
        fig.write_html(html_file, include_plotlyjs=PLOTLY_PATH.as_uri(), config=config)
        self.ui_form.corr_web_engine.setUrl(html_file.as_uri())
