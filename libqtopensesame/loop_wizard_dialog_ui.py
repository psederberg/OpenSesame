# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/loop_wizard_dialog.ui'
#
# Created: Fri Mar 25 10:52:07 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 426)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/wizard_large.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtGui.QCheckBox(self.widget_2)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget_2)
        self.table_example = good_looking_table(Dialog)
        self.table_example.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_example.setGridStyle(QtCore.Qt.DotLine)
        self.table_example.setObjectName("table_example")
        self.table_example.setColumnCount(10)
        self.table_example.setRowCount(12)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_example.setItem(4, 0, item)
        self.table_example.horizontalHeader().setVisible(False)
        self.table_example.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_example)
        self.table_wizard = good_looking_table(Dialog)
        self.table_wizard.setGridStyle(QtCore.Qt.DotLine)
        self.table_wizard.setObjectName("table_wizard")
        self.table_wizard.setColumnCount(0)
        self.table_wizard.setRowCount(0)
        self.table_wizard.horizontalHeader().setVisible(False)
        self.table_wizard.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_wizard)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("toggled(bool)"), self.table_example.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Loop Variable Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Loop variable wizard</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the names of the variables (factors) in the first row in the table below. Under the variable names, enter the levels of the variables.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Note: This will overwrite the current loop table</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Dialog", "Show example", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(3).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(4).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(5).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(6).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(7).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(8).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(9).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(10).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.verticalHeaderItem(11).setText(QtGui.QApplication.translate("Dialog", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Dialog", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Dialog", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("Dialog", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("Dialog", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("Dialog", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("Dialog", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.horizontalHeaderItem(9).setText(QtGui.QApplication.translate("Dialog", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.table_example.isSortingEnabled()
        self.table_example.setSortingEnabled(False)
        self.table_example.item(0, 0).setText(QtGui.QApplication.translate("Dialog", "soa", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.item(0, 1).setText(QtGui.QApplication.translate("Dialog", "target", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.item(0, 2).setText(QtGui.QApplication.translate("Dialog", "cue", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.item(1, 0).setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.item(1, 1).setText(QtGui.QApplication.translate("Dialog", "left", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.item(1, 2).setText(QtGui.QApplication.translate("Dialog", "left", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.item(2, 0).setText(QtGui.QApplication.translate("Dialog", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.item(2, 1).setText(QtGui.QApplication.translate("Dialog", "right", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.item(2, 2).setText(QtGui.QApplication.translate("Dialog", "right", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.item(3, 0).setText(QtGui.QApplication.translate("Dialog", "500", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.item(4, 0).setText(QtGui.QApplication.translate("Dialog", "1000", None, QtGui.QApplication.UnicodeUTF8))
        self.table_example.setSortingEnabled(__sortingEnabled)

from good_looking_table import good_looking_table
import icons_rc
