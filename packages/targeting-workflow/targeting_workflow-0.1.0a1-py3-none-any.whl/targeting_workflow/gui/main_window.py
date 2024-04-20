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
import os
import sys
import warnings
from pathlib import Path

from geoh5py.data.referenced_data import ReferencedData
from geoh5py.ui_json import InputFile
from geoh5py.workspace import Workspace
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMessageBox, QWidget

from targeting_workflow import assets_path
from targeting_workflow.database.database import Database
from targeting_workflow.database.database_utils import set_no_target, set_target
from targeting_workflow.gui.auto_generated.qt_gui import Ui_Form
from targeting_workflow.gui.tab_modelling import ModellingTab
from targeting_workflow.gui.tab_property_eda import TabPropertyEDA
from targeting_workflow.gui.tab_property_selection import PropertySelection
from targeting_workflow.gui.tab_train_test import TabTrainTest
from targeting_workflow.shared.geoh5py_utils import get_multi_data_from_ui_json
from targeting_workflow.shared.utils import special_round

warnings.filterwarnings("ignore")


class MainWindow(QWidget):
    def __init__(self, parameters: dict):
        """
        Initialize the main window.
        :param parameters: Ui json parameters
        """
        super().__init__()
        self.icon = None
        self.ui_form = Ui_Form()
        self.ui_form.setupUi(self)

        self.setWindowTitle("Data Driven Targeting Workflow")
        self.set_window_icon()

        # store reference to data objects
        self.monitoring_directory = parameters["monitoring_directory"]
        self.geoh5_object = parameters["grid_object"]
        self.database = Database(self.geoh5_object)

        # Set the target and no target property
        self.set_target_no_target(parameters)

        # Hide progress bars
        self.ui_form.run_progress_bar.hide()

        # Temporary directory to store plotly html files
        folder = os.path.dirname(parameters["geoh5"].h5file)
        self.temp_dir = folder

        # Instantiate the tab callbacks
        self.tab_test_train_split = TabTrainTest(self)
        self.tab_property_eda = TabPropertyEDA(self)
        self.tab_modelling = ModellingTab(self)
        self.tab_property_selection = PropertySelection(self)
        self.set_button_icon()

    def set_target_no_target(self, parameters):
        if isinstance(parameters["target"]["property"], ReferencedData):
            text = (
                f"{parameters['target']['property'].name} "
                f"= {special_round(parameters['target']['value'][0])}"
            )
            operand = "="
        else:
            text = (
                f"{special_round(parameters['target']['value'][0])} > "
                f"{parameters['target']['property'].name} "
                f"> {special_round(parameters['target']['value'][1])}"
            )
            operand = "<>"

        # define the data and target variable
        self.ui_form.target_property.setText(text)

        set_target(
            self.database,
            parameters["target"]["property"].name,
            operand,
            parameters["target"]["value"],
        )

        # define the no target variable if it exists
        if parameters["no_target"]["property"] is None:
            self.ui_form.no_target_frame.hide()
        else:
            if isinstance(parameters["no_target"]["property"], ReferencedData):
                text = (
                    f"{parameters['no_target']['property'].name} "
                    f"= {special_round(parameters['no_target']['value'][0])}"
                )
                operand = "="
            else:
                text = (
                    f"{special_round(parameters['no_target']['value'][0])} > "
                    f"{parameters['no_target']['property'].name} "
                    f"> {special_round(parameters['no_target']['value'][1])}"
                )
                operand = "<>"

            # define the no target variable
            self.ui_form.no_target_property.setText(text)

            set_no_target(
                self.database,
                parameters["no_target"]["property"].name,
                operand,
                parameters["no_target"]["value"],
            )

    def error_occurred(self, error_message: str):
        """
        Method to handle errors in the model run.
        :param error_message: Error message to display
        """
        # Popup a pyside 2 warning dialog
        QMessageBox.critical(
            self,
            "Something went wrong!",
            error_message,
        )
        self.ui_form.run_progress_bar.hide()
        self.ui_form.progressBar.hide()
        self.toggle_buttons_enabled(True)

    def set_button_icon(self):
        """Sets icons on buttons"""
        download_icon_path = Path(assets_path() / "icon" / "download.png")
        self.ui_form.export_to_ga_button.setIcon(QIcon(str(download_icon_path)))

    def set_window_icon(self):
        """Sets the mira AI icon to the main window"""
        icon_path = Path(assets_path() / "icon" / "prism-ball-10cm.png")
        self.icon = QIcon(str(icon_path))
        self.setWindowIcon(self.icon)

    def toggle_buttons_enabled(self, enabled: bool):
        """
        Enables or disables the buttons and sliders while another thread is running
        :param enabled: true if the user input is enabled
        """
        self.ui_form.run_button.setEnabled(enabled)
        self.ui_form.export_to_ga_button.setEnabled(enabled)
        self.ui_form.move_left_button.setEnabled(enabled)
        self.ui_form.move_right_button.setEnabled(enabled)
        self.ui_form.distance_spinbox.setEnabled(enabled)
        self.ui_form.eda_property_combobox.setEnabled(enabled)
        # self.ui_form.property_selection_list.setEnabled(true_false)


def main():
    app = QApplication()
    if len(sys.argv) > 1:
        to_change = {
            "target": ["property", "value"],
            "no_target": ["property", "value"],
        }

        params = get_multi_data_from_ui_json(
            InputFile.read_ui_json(sys.argv[1]), to_change
        )
        window = MainWindow(params)
        window.show()
        sys.exit(app.exec_())
    else:
        with Workspace(str(assets_path() / "MPM_input.geoh5")).open("r") as in_ws:
            ui_file = assets_path() / "uijson" / "targeting_workflow.ui.json"

            ifile = InputFile.read_ui_json(
                str(ui_file), validation_options={"disabled": True}
            )

            obj = in_ws.get_entity("MPM_test")[0]
            target = obj.get_entity("MIN_ore")[0]
            ifile.data["geoh5"] = in_ws
            ifile.data["grid_object"] = obj
            ifile.data["target_property"] = target
            ifile.data["target_operator"] = "=="
            ifile.data["target_threshold"] = [2.0]
            ifile.data["no_target_operator"] = "=="
            ifile.data["no_target_threshold"] = [1.0]
            ifile.data["monitoring_directory"] = str(assets_path())

        ifile.write_ui_json("tester.ui.json", path=str(assets_path()))
        filepath = assets_path() / "tester.ui.json"

        completed_input_file = InputFile.read_ui_json(str(filepath))

        main_window = MainWindow(completed_input_file.data)
        main_window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()
