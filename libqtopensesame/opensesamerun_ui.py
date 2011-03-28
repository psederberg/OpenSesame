# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/opensesamerun.ui'
#
# Created: Fri Mar 25 15:35:52 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 375)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/experiment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtGui.QWidget(self.centralwidget)
        self.widget_5.setStyleSheet("background-color: #555753;\n"
"color: rgb(255, 255, 255);")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setMargin(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtGui.QLabel(self.widget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icons/experiment_large.png"))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.widget_5)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.verticalLayout.addWidget(self.widget_5)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(0, 6, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.widget_3 = QtGui.QWidget(self.groupBox_3)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edit_experiment = QtGui.QLineEdit(self.widget_3)
        self.edit_experiment.setObjectName("edit_experiment")
        self.horizontalLayout_3.addWidget(self.edit_experiment)
        self.button_browse_experiment = QtGui.QPushButton(self.widget_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/browse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_browse_experiment.setIcon(icon1)
        self.button_browse_experiment.setObjectName("button_browse_experiment")
        self.horizontalLayout_3.addWidget(self.button_browse_experiment)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.widget_3)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.widget_2 = QtGui.QWidget(self.groupBox_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edit_logfile = QtGui.QLineEdit(self.widget_2)
        self.edit_logfile.setObjectName("edit_logfile")
        self.horizontalLayout.addWidget(self.edit_logfile)
        self.button_browse_logfile = QtGui.QPushButton(self.widget_2)
        self.button_browse_logfile.setIcon(icon1)
        self.button_browse_logfile.setObjectName("button_browse_logfile")
        self.horizontalLayout.addWidget(self.button_browse_logfile)
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.widget_2)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spinbox_subject_nr = QtGui.QSpinBox(self.groupBox_3)
        self.spinbox_subject_nr.setMaximum(100000)
        self.spinbox_subject_nr.setObjectName("spinbox_subject_nr")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinbox_subject_nr)
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setContentsMargins(0, 6, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.checkbox_fullscreen = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_fullscreen.setObjectName("checkbox_fullscreen")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkbox_fullscreen)
        self.checkbox_custom_resolution = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_custom_resolution.setObjectName("checkbox_custom_resolution")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkbox_custom_resolution)
        self.widget = QtGui.QWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_width = QtGui.QLabel(self.widget)
        self.label_width.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_width.sizePolicy().hasHeightForWidth())
        self.label_width.setSizePolicy(sizePolicy)
        self.label_width.setObjectName("label_width")
        self.horizontalLayout_2.addWidget(self.label_width)
        self.spinbox_width = QtGui.QSpinBox(self.widget)
        self.spinbox_width.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_width.sizePolicy().hasHeightForWidth())
        self.spinbox_width.setSizePolicy(sizePolicy)
        self.spinbox_width.setMinimum(1)
        self.spinbox_width.setMaximum(100000)
        self.spinbox_width.setProperty("value", 1024)
        self.spinbox_width.setObjectName("spinbox_width")
        self.horizontalLayout_2.addWidget(self.spinbox_width)
        self.label_height = QtGui.QLabel(self.widget)
        self.label_height.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_height.sizePolicy().hasHeightForWidth())
        self.label_height.setSizePolicy(sizePolicy)
        self.label_height.setObjectName("label_height")
        self.horizontalLayout_2.addWidget(self.label_height)
        self.spinbox_height = QtGui.QSpinBox(self.widget)
        self.spinbox_height.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_height.sizePolicy().hasHeightForWidth())
        self.spinbox_height.setSizePolicy(sizePolicy)
        self.spinbox_height.setMinimum(1)
        self.spinbox_height.setMaximum(100000)
        self.spinbox_height.setProperty("value", 768)
        self.spinbox_height.setObjectName("spinbox_height")
        self.horizontalLayout_2.addWidget(self.spinbox_height)
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.widget)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_3.setItem(2, QtGui.QFormLayout.FieldRole, spacerItem)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 6, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.checkbox_pylink = QtGui.QCheckBox(self.groupBox)
        self.checkbox_pylink.setObjectName("checkbox_pylink")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkbox_pylink)
        self.verticalLayout.addWidget(self.groupBox)
        self.widget_4 = QtGui.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.button_cancel = QtGui.QPushButton(self.widget_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cancel.setIcon(icon2)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_4.addWidget(self.button_cancel)
        self.button_run = QtGui.QPushButton(self.widget_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/execute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_run.setIcon(icon3)
        self.button_run.setObjectName("button_run")
        self.horizontalLayout_4.addWidget(self.button_run)
        self.verticalLayout.addWidget(self.widget_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.button_cancel, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(self.checkbox_custom_resolution, QtCore.SIGNAL("toggled(bool)"), self.spinbox_width.setEnabled)
        QtCore.QObject.connect(self.checkbox_custom_resolution, QtCore.SIGNAL("toggled(bool)"), self.spinbox_height.setEnabled)
        QtCore.QObject.connect(self.checkbox_custom_resolution, QtCore.SIGNAL("toggled(bool)"), self.label_width.setEnabled)
        QtCore.QObject.connect(self.checkbox_custom_resolution, QtCore.SIGNAL("toggled(bool)"), self.label_height.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "OpenSesame Run", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">OpenSesame Run</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Run your OpenSesame experiment</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Experiment, subject and log file", None, QtGui.QApplication.UnicodeUTF8))
        self.button_browse_experiment.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Experiment", None, QtGui.QApplication.UnicodeUTF8))
        self.button_browse_logfile.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Log file", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Subject number", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_fullscreen.setText(QtGui.QApplication.translate("MainWindow", "Run fullscreen", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_custom_resolution.setText(QtGui.QApplication.translate("MainWindow", "Use custom display resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.label_width.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_width.setSuffix(QtGui.QApplication.translate("MainWindow", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.label_height.setText(QtGui.QApplication.translate("MainWindow", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_height.setSuffix(QtGui.QApplication.translate("MainWindow", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Miscellaneous", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_pylink.setText(QtGui.QApplication.translate("MainWindow", "Enable PyLink module (required for the Eyelink plug-ins)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.button_run.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
