# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(940, 716)
        Form.setStyleSheet(u"/* Widget */\n"
"QWidget {\n"
"    background-color: #fafafa;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    color: #343a40;\n"
"}\n"
"\n"
"QListWidget {\n"
"        border-radius: 5px;\n"
"border: 1px solid black;\n"
"    }\n"
"\n"
"\n"
"/* Push Buttons */\n"
"QPushButton {\n"
"    background-color: #343a40;\n"
"    color: #fff;\n"
"    border-radius: 4px;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #535c68;\n"
"}\n"
"\n"
"/* Combo Boxes */\n"
"QComboBox {\n"
"    background-color: #fff;\n"
"    color: #495057;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #bdc3c7;\n"
"}\n"
"\n"
"\n"
"/* Check Boxes */\n"
"QCheckBox {\n"
"    color: #495057;\n"
"}\n"
"\n"
"/* Tab Widget */\n"
"QTabWidget {\n"
"    background-color: #343a40;\n"
"    color: #fff;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    fo"
                        "nt-size: 10pt;\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #343a40;\n"
"    color: #fff;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    padding: 8px 16px;\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #4d5563;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #535c68;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"/* Scroll Bars */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #fafafa;\n"
"    width: 12px;\n"
"    margin: 0px 0 0px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #dee2e6;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
                        "\n"
"    background: none;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.target_layout = QHBoxLayout()
        self.target_layout.setObjectName(u"target_layout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Segoe UI,sans-serif")
        font.setPointSize(10)
        self.label.setFont(font)

        self.target_layout.addWidget(self.label)

        self.target_property = QLabel(Form)
        self.target_property.setObjectName(u"target_property")
        font1 = QFont()
        font1.setFamily(u"Segoe UI,sans-serif")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.target_property.setFont(font1)

        self.target_layout.addWidget(self.target_property)


        self.horizontalLayout.addLayout(self.target_layout)

        self.no_target_frame = QFrame(Form)
        self.no_target_frame.setObjectName(u"no_target_frame")
        self.no_target_layout = QHBoxLayout(self.no_target_frame)
        self.no_target_layout.setObjectName(u"no_target_layout")
        self.label_2 = QLabel(self.no_target_frame)
        self.label_2.setObjectName(u"label_2")

        self.no_target_layout.addWidget(self.label_2)

        self.no_target_property = QLabel(self.no_target_frame)
        self.no_target_property.setObjectName(u"no_target_property")
        self.no_target_property.setFont(font1)

        self.no_target_layout.addWidget(self.no_target_property)


        self.horizontalLayout.addWidget(self.no_target_frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.workflow_tabs = QTabWidget(Form)
        self.workflow_tabs.setObjectName(u"workflow_tabs")
        self.workflow_tabs.setFont(font)
        self.workflow_tabs.setStyleSheet(u"")
        self.workflow_tabs.setTabShape(QTabWidget.Rounded)
        self.tab_property_selection = QWidget()
        self.tab_property_selection.setObjectName(u"tab_property_selection")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_property_selection)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.properties_vertical_layout = QVBoxLayout()
        self.properties_vertical_layout.setObjectName(u"properties_vertical_layout")
        self.properties_vertical_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_properties = QLabel(self.tab_property_selection)
        self.label_properties.setObjectName(u"label_properties")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_properties.sizePolicy().hasHeightForWidth())
        self.label_properties.setSizePolicy(sizePolicy)
        self.label_properties.setFont(font)

        self.properties_vertical_layout.addWidget(self.label_properties)

        self.property_selection_list = QListWidget(self.tab_property_selection)
        self.property_selection_list.setObjectName(u"property_selection_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.property_selection_list.sizePolicy().hasHeightForWidth())
        self.property_selection_list.setSizePolicy(sizePolicy1)
        self.property_selection_list.setMinimumSize(QSize(300, 0))
        self.property_selection_list.setMaximumSize(QSize(16777215, 16777215))
        self.property_selection_list.setSelectionMode(QAbstractItemView.MultiSelection)

        self.properties_vertical_layout.addWidget(self.property_selection_list)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.update_plots_button = QPushButton(self.tab_property_selection)
        self.update_plots_button.setObjectName(u"update_plots_button")

        self.horizontalLayout_13.addWidget(self.update_plots_button)

        self.horizontalSpacer_6 = QSpacerItem(90, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.properties_vertical_layout.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_10.addLayout(self.properties_vertical_layout)

        self.corr_web_engine = QWebEngineView(self.tab_property_selection)
        self.corr_web_engine.setObjectName(u"corr_web_engine")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.corr_web_engine.sizePolicy().hasHeightForWidth())
        self.corr_web_engine.setSizePolicy(sizePolicy2)
        self.corr_web_engine.setMinimumSize(QSize(0, 0))
        self.corr_web_engine.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.corr_web_engine)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_10)

        self.workflow_tabs.addTab(self.tab_property_selection, "")
        self.tab_train_test = QWidget()
        self.tab_train_test.setObjectName(u"tab_train_test")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_train_test)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_distance = QLabel(self.tab_train_test)
        self.label_distance.setObjectName(u"label_distance")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_distance.sizePolicy().hasHeightForWidth())
        self.label_distance.setSizePolicy(sizePolicy3)
        self.label_distance.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_distance)

        self.distance_spinbox = QSpinBox(self.tab_train_test)
        self.distance_spinbox.setObjectName(u"distance_spinbox")
        self.distance_spinbox.setMinimumSize(QSize(0, 31))
        self.distance_spinbox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.distance_spinbox.setKeyboardTracking(False)
        self.distance_spinbox.setMaximum(1000000)
        self.distance_spinbox.setSingleStep(10)
        self.distance_spinbox.setValue(5000)

        self.horizontalLayout_3.addWidget(self.distance_spinbox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(self.tab_train_test)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QSize(180, 30))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)

        self.horizontalLayout_3.addWidget(self.progressBar)

        self.label_groups = QLabel(self.tab_train_test)
        self.label_groups.setObjectName(u"label_groups")
        sizePolicy3.setHeightForWidth(self.label_groups.sizePolicy().hasHeightForWidth())
        self.label_groups.setSizePolicy(sizePolicy3)
        self.label_groups.setFont(font1)
        self.label_groups.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_groups)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.train_pct_label = QLabel(self.tab_train_test)
        self.train_pct_label.setObjectName(u"train_pct_label")
        sizePolicy3.setHeightForWidth(self.train_pct_label.sizePolicy().hasHeightForWidth())
        self.train_pct_label.setSizePolicy(sizePolicy3)
        self.train_pct_label.setFont(font)
        self.train_pct_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.train_pct_label)

        self.label_train = QLabel(self.tab_train_test)
        self.label_train.setObjectName(u"label_train")
        sizePolicy3.setHeightForWidth(self.label_train.sizePolicy().hasHeightForWidth())
        self.label_train.setSizePolicy(sizePolicy3)
        self.label_train.setFont(font)
        self.label_train.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_train)

        self.train_list = QListWidget(self.tab_train_test)
        self.train_list.setObjectName(u"train_list")
        sizePolicy1.setHeightForWidth(self.train_list.sizePolicy().hasHeightForWidth())
        self.train_list.setSizePolicy(sizePolicy1)
        self.train_list.setMinimumSize(QSize(50, 300))
        self.train_list.setMaximumSize(QSize(75, 16777215))
        self.train_list.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_2.addWidget(self.train_list)


        self.horizontalLayout_12.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.move_left_button = QToolButton(self.tab_train_test)
        self.move_left_button.setObjectName(u"move_left_button")
        self.move_left_button.setMinimumSize(QSize(20, 0))
        self.move_left_button.setStyleSheet(u"")
        self.move_left_button.setArrowType(Qt.LeftArrow)

        self.horizontalLayout_2.addWidget(self.move_left_button)

        self.move_right_button = QToolButton(self.tab_train_test)
        self.move_right_button.setObjectName(u"move_right_button")
        self.move_right_button.setMinimumSize(QSize(20, 0))
        self.move_right_button.setStyleSheet(u"")
        self.move_right_button.setArrowType(Qt.RightArrow)

        self.horizontalLayout_2.addWidget(self.move_right_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_12.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.test_pct_label = QLabel(self.tab_train_test)
        self.test_pct_label.setObjectName(u"test_pct_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.test_pct_label.sizePolicy().hasHeightForWidth())
        self.test_pct_label.setSizePolicy(sizePolicy4)
        self.test_pct_label.setFont(font)
        self.test_pct_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.test_pct_label)

        self.label_test = QLabel(self.tab_train_test)
        self.label_test.setObjectName(u"label_test")
        sizePolicy4.setHeightForWidth(self.label_test.sizePolicy().hasHeightForWidth())
        self.label_test.setSizePolicy(sizePolicy4)
        self.label_test.setFont(font)
        self.label_test.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_test)

        self.test_list = QListWidget(self.tab_train_test)
        self.test_list.setObjectName(u"test_list")
        sizePolicy1.setHeightForWidth(self.test_list.sizePolicy().hasHeightForWidth())
        self.test_list.setSizePolicy(sizePolicy1)
        self.test_list.setMinimumSize(QSize(50, 0))
        self.test_list.setMaximumSize(QSize(75, 16777215))
        self.test_list.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_3.addWidget(self.test_list)


        self.horizontalLayout_12.addLayout(self.verticalLayout_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.examples_mapwidget = QWebEngineView(self.tab_train_test)
        self.examples_mapwidget.setObjectName(u"examples_mapwidget")
        self.examples_mapwidget.setMinimumSize(QSize(700, 500))
        self.examples_mapwidget.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.examples_mapwidget)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.workflow_tabs.addTab(self.tab_train_test, "")
        self.tab_property_eda = QWidget()
        self.tab_property_eda.setObjectName(u"tab_property_eda")
        self.verticalLayout_6 = QVBoxLayout(self.tab_property_eda)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_2 = QWidget(self.tab_property_eda)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.eda_property_combobox = QComboBox(self.widget_2)
        self.eda_property_combobox.setObjectName(u"eda_property_combobox")
        sizePolicy.setHeightForWidth(self.eda_property_combobox.sizePolicy().hasHeightForWidth())
        self.eda_property_combobox.setSizePolicy(sizePolicy)
        self.eda_property_combobox.setMinimumSize(QSize(300, 0))
        self.eda_property_combobox.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.eda_property_combobox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.verticalLayout_6.addWidget(self.widget_2)

        self.property_web_engine = QWebEngineView(self.tab_property_eda)
        self.property_web_engine.setObjectName(u"property_web_engine")
        self.property_web_engine.setMinimumSize(QSize(500, 500))
        self.property_web_engine.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.property_web_engine)

        self.workflow_tabs.addTab(self.tab_property_eda, "")
        self.tab_modelling = QWidget()
        self.tab_modelling.setObjectName(u"tab_modelling")
        self.verticalLayout_7 = QVBoxLayout(self.tab_modelling)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_7 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.modelling_tabs = QTabWidget(self.tab_modelling)
        self.modelling_tabs.setObjectName(u"modelling_tabs")
        self.modelling_tabs.setLayoutDirection(Qt.LeftToRight)
        self.modelling_tabs.setAutoFillBackground(False)
        self.modelling_tabs.setStyleSheet(u"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"/* set background color of tabs 1, 2, and 3 to blue */\n"
"QTabBar::tab:first:selected, \n"
"QTabBar::tab:first:hover, \n"
"QTabBar::tab:selected:first, \n"
"QTabBar::tab:hover:first,\n"
"QTabBar::tab:nth:selected(2),\n"
"QTabBar::tab:nth:hover(2),\n"
"QTabBar::tab:selected:nth(2),\n"
"QTabBar::tab:hover:nth(2),\n"
"QTabBar::tab:nth:selected(3),\n"
"QTabBar::tab:nth:hover(3),\n"
"QTabBar::tab:selected:nth(3),\n"
"QTabBar::tab:hover:nth(3) {\n"
"    background-color: blue;\n"
"}\n"
"QTabWidget {\n"
"   background-color: blue;    color: blue;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab {\n"
"    background-color: blue;\n"
"    color: blue;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    padding: 8px 16px;\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"      background-color: blue;\n"
"    color: blue;\n"
"}")
        self.modelling_tabs.setTabShape(QTabWidget.Rounded)
        self.modelling_tabs.setUsesScrollButtons(True)
        self.tab_KnowledgeDtiven = QWidget()
        self.tab_KnowledgeDtiven.setObjectName(u"tab_KnowledgeDtiven")
        self.verticalLayout_9 = QVBoxLayout(self.tab_KnowledgeDtiven)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tableWidget = QTableWidget(self.tab_KnowledgeDtiven)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(610, 0))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.CustomDashLine)

        self.verticalLayout_9.addWidget(self.tableWidget)

        self.modelling_tabs.addTab(self.tab_KnowledgeDtiven, "")
        self.tab_feature_importance = QWidget()
        self.tab_feature_importance.setObjectName(u"tab_feature_importance")
        self.verticalLayout_11 = QVBoxLayout(self.tab_feature_importance)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.feature_importance_web_engine = QWebEngineView(self.tab_feature_importance)
        self.feature_importance_web_engine.setObjectName(u"feature_importance_web_engine")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.feature_importance_web_engine.sizePolicy().hasHeightForWidth())
        self.feature_importance_web_engine.setSizePolicy(sizePolicy6)

        self.verticalLayout_11.addWidget(self.feature_importance_web_engine)

        self.modelling_tabs.addTab(self.tab_feature_importance, "")
        self.tab_confusion_matrix = QWidget()
        self.tab_confusion_matrix.setObjectName(u"tab_confusion_matrix")
        self.verticalLayout_12 = QVBoxLayout(self.tab_confusion_matrix)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.confusion_matrix_web_engine = QWebEngineView(self.tab_confusion_matrix)
        self.confusion_matrix_web_engine.setObjectName(u"confusion_matrix_web_engine")
        sizePolicy6.setHeightForWidth(self.confusion_matrix_web_engine.sizePolicy().hasHeightForWidth())
        self.confusion_matrix_web_engine.setSizePolicy(sizePolicy6)

        self.verticalLayout_12.addWidget(self.confusion_matrix_web_engine)

        self.modelling_tabs.addTab(self.tab_confusion_matrix, "")
        self.tab_roc_curve = QWidget()
        self.tab_roc_curve.setObjectName(u"tab_roc_curve")
        self.verticalLayout_13 = QVBoxLayout(self.tab_roc_curve)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.roc_curve_web_engine = QWebEngineView(self.tab_roc_curve)
        self.roc_curve_web_engine.setObjectName(u"roc_curve_web_engine")
        sizePolicy6.setHeightForWidth(self.roc_curve_web_engine.sizePolicy().hasHeightForWidth())
        self.roc_curve_web_engine.setSizePolicy(sizePolicy6)

        self.verticalLayout_13.addWidget(self.roc_curve_web_engine)

        self.modelling_tabs.addTab(self.tab_roc_curve, "")

        self.verticalLayout_10.addWidget(self.modelling_tabs)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.predictor_combo_box = QComboBox(self.tab_modelling)
        self.predictor_combo_box.addItem("")
        self.predictor_combo_box.addItem("")
        self.predictor_combo_box.setObjectName(u"predictor_combo_box")
        self.predictor_combo_box.setMinimumSize(QSize(200, 20))
        self.predictor_combo_box.setMaximumSize(QSize(16777215, 40))
        self.predictor_combo_box.setTabletTracking(False)

        self.horizontalLayout_7.addWidget(self.predictor_combo_box)

        self.score_label = QLabel(self.tab_modelling)
        self.score_label.setObjectName(u"score_label")
        sizePolicy3.setHeightForWidth(self.score_label.sizePolicy().hasHeightForWidth())
        self.score_label.setSizePolicy(sizePolicy3)
        self.score_label.setStyleSheet(u"")
        self.score_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.score_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.run_progress_bar = QProgressBar(self.tab_modelling)
        self.run_progress_bar.setObjectName(u"run_progress_bar")
        self.run_progress_bar.setEnabled(True)
        self.run_progress_bar.setMaximumSize(QSize(180, 16777215))
        self.run_progress_bar.setMaximum(0)
        self.run_progress_bar.setValue(-1)
        self.run_progress_bar.setTextVisible(False)

        self.horizontalLayout_7.addWidget(self.run_progress_bar)

        self.run_button = QPushButton(self.tab_modelling)
        self.run_button.setObjectName(u"run_button")
        self.run_button.setMinimumSize(QSize(100, 0))
        self.run_button.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.run_button)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.export_to_ga_button = QPushButton(self.tab_modelling)
        self.export_to_ga_button.setObjectName(u"export_to_ga_button")
        self.export_to_ga_button.setEnabled(False)
        self.export_to_ga_button.setLayoutDirection(Qt.LeftToRight)
        self.export_to_ga_button.setStyleSheet(u"QPushButton{ background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"QPushButton:hover {\n"
"    background-color: #3e6c82;\n"
"}")

        self.horizontalLayout_11.addWidget(self.export_to_ga_button)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)


        self.verticalLayout_7.addLayout(self.verticalLayout_10)

        self.workflow_tabs.addTab(self.tab_modelling, "")

        self.verticalLayout.addWidget(self.workflow_tabs)


        self.retranslateUi(Form)

        self.workflow_tabs.setCurrentIndex(0)
        self.modelling_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Mineralization Potential Index", None))
        self.label.setStyleSheet("")
        self.label.setText(QCoreApplication.translate("Form", u"Target:", None))
        self.target_property.setText(QCoreApplication.translate("Form", u"target_property", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"No Target:", None))
        self.no_target_property.setText(QCoreApplication.translate("Form", u"no_target_property", None))
        self.label_properties.setStyleSheet("")
        self.label_properties.setText(QCoreApplication.translate("Form", u"Properties:", None))
        self.property_selection_list.setStyleSheet("")
        self.update_plots_button.setText(QCoreApplication.translate("Form", u"Update Plot", None))
        self.workflow_tabs.setTabText(self.workflow_tabs.indexOf(self.tab_property_selection), QCoreApplication.translate("Form", u"Property Selection", None))
        self.label_distance.setStyleSheet("")
        self.label_distance.setText(QCoreApplication.translate("Form", u"Distance:", None))
        self.label_groups.setText(QCoreApplication.translate("Form", u"300 groups", None))
        self.train_pct_label.setStyleSheet("")
        self.train_pct_label.setText(QCoreApplication.translate("Form", u"100%", None))
        self.label_train.setStyleSheet("")
        self.label_train.setText(QCoreApplication.translate("Form", u"Train", None))
#if QT_CONFIG(tooltip)
        self.train_list.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.train_list.setStyleSheet("")
        self.move_left_button.setText(QCoreApplication.translate("Form", u"...", None))
        self.move_right_button.setText(QCoreApplication.translate("Form", u"...", None))
        self.test_pct_label.setStyleSheet("")
        self.test_pct_label.setText(QCoreApplication.translate("Form", u"0%", None))
        self.label_test.setStyleSheet("")
        self.label_test.setText(QCoreApplication.translate("Form", u"Test", None))
#if QT_CONFIG(tooltip)
        self.test_list.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.test_list.setStyleSheet("")
        self.workflow_tabs.setTabText(self.workflow_tabs.indexOf(self.tab_train_test), QCoreApplication.translate("Form", u"Train Test Split", None))
        self.widget_2.setStyleSheet("")
        self.label_5.setStyleSheet("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Property:", None))
        self.eda_property_combobox.setStyleSheet("")
        self.workflow_tabs.setTabText(self.workflow_tabs.indexOf(self.tab_property_eda), QCoreApplication.translate("Form", u"Property EDA", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Property", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Min", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Max", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Weight", None));
        self.modelling_tabs.setTabText(self.modelling_tabs.indexOf(self.tab_KnowledgeDtiven), QCoreApplication.translate("Form", u"Index Overlay", None))
        self.modelling_tabs.setTabText(self.modelling_tabs.indexOf(self.tab_feature_importance), QCoreApplication.translate("Form", u"Feature Importance", None))
        self.modelling_tabs.setTabText(self.modelling_tabs.indexOf(self.tab_confusion_matrix), QCoreApplication.translate("Form", u"Confusion Matrix", None))
        self.modelling_tabs.setTabText(self.modelling_tabs.indexOf(self.tab_roc_curve), QCoreApplication.translate("Form", u"ROC Curve", None))
        self.predictor_combo_box.setItemText(0, QCoreApplication.translate("Form", u"Random Forest", None))
        self.predictor_combo_box.setItemText(1, QCoreApplication.translate("Form", u"Knowledge Driven", None))

        self.score_label.setText(QCoreApplication.translate("Form", u"Score:", None))
        self.run_button.setText(QCoreApplication.translate("Form", u"Run", None))
        self.export_to_ga_button.setText(QCoreApplication.translate("Form", u"  Export to GA", None))
        self.workflow_tabs.setTabText(self.workflow_tabs.indexOf(self.tab_modelling), QCoreApplication.translate("Form", u"Modeling", None))
    # retranslateUi

