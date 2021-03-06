"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

import libqtopensesame.preferences_widget_ui
from PyQt4 import QtCore, QtGui
import os

class preferences_widget(QtGui.QWidget):

	"""
	Displayed in the preferences tab
	"""

	def __init__(self, parent):
	
		"""
		Constructor
		"""
		
		QtGui.QWidget.__init__(self, parent)
		self.tab_name = "__preferences__"					
		self.main_window = parent
		
		# Setup the GUI
		self.ui = libqtopensesame.preferences_widget_ui.Ui_Form()
		self.ui.setupUi(self)		
		
		self.set_controls()
			
		# Connect the controls
		self.ui.checkbox_immediately_rename.toggled.connect(self.apply)
		self.ui.checkbox_autoresponse.toggled.connect(self.apply)
		self.ui.checkbox_show_random_tips.toggled.connect(self.apply)
		self.ui.checkbox_toolbar_text.toggled.connect(self.apply)
		self.ui.checkbox_enable_autosave.toggled.connect(self.apply)
		self.ui.spinbox_autosave_interval.valueChanged.connect(self.apply)
		self.ui.checkbox_auto_update_check.toggled.connect(self.apply)		
		self.ui.checkbox_opensesamerun.toggled.connect(self.apply)
		self.ui.checkbox_auto_opensesamerun_exec.toggled.connect(self.apply)						
		self.ui.edit_opensesamerun_exec.editingFinished.connect(self.apply)			
		self.ui.button_browse_autosave.clicked.connect(self.main_window.open_autosave_folder)	
		self.ui.button_update_check.clicked.connect(self.main_window.check_update)
				
	def set_controls(self):
	
		"""
		Set the controls based on the current preferences
		"""
		
		if self.main_window.experiment.debug:
			print "preferences_widget.set_controls(): setting controls"
		
		self.ui.checkbox_immediately_rename.setChecked(self.main_window.immediate_rename)
		self.ui.checkbox_autoresponse.setChecked(self.main_window.experiment.auto_response)
		self.ui.checkbox_show_random_tips.setChecked(self.main_window.show_startup_tip)
		self.ui.checkbox_toolbar_text.setChecked(self.main_window.ui.toolbar_main.toolButtonStyle() == QtCore.Qt.ToolButtonTextUnderIcon)		
		self.ui.checkbox_enable_autosave.setChecked(self.main_window.autosave_interval > 0)
		self.ui.spinbox_autosave_interval.setValue(self.main_window.autosave_interval / 60000) # Show in minutes, not milliseconds		
		self.ui.checkbox_auto_update_check.setChecked(self.main_window.auto_check_update)		
		self.ui.checkbox_opensesamerun.setChecked(self.main_window.opensesamerun)				
		self.ui.checkbox_auto_opensesamerun_exec.setChecked(self.main_window.opensesamerun_exec == "")
		self.ui.edit_opensesamerun_exec.setText(self.main_window.opensesamerun_exec)
		
		# Disable some of the controls, if they depend on other controls
		if self.main_window.autosave_interval <= 0:
			self.ui.spinbox_autosave_interval.setDisabled(True)	
				
		if not self.main_window.opensesamerun:
			self.ui.checkbox_auto_opensesamerun_exec.setDisabled(True)
			self.ui.edit_opensesamerun_exec.setDisabled(True)
			self.ui.label_opensesamerun_exec.setDisabled(True)
					
		if self.main_window.opensesamerun_exec == "":
			self.ui.edit_opensesamerun_exec.setDisabled(True)
			self.ui.label_opensesamerun_exec.setDisabled(True)
			
	def apply(self):
	
		"""
		Set the preferences based on the controls and save
		"""
		
		if self.main_window.experiment.debug:
			print "preferences_widget.apply(): applying controls"		
		
		self.main_window.immediate_rename = self.ui.checkbox_immediately_rename.isChecked()
		self.main_window.show_startup_tip = self.ui.checkbox_show_random_tips.isChecked()		
		self.main_window.experiment.auto_response = self.ui.checkbox_autoresponse.isChecked()
		self.main_window.ui.action_enable_auto_response.setChecked(self.ui.checkbox_autoresponse.isChecked())
		
		if self.ui.checkbox_toolbar_text.isChecked():
			self.main_window.ui.toolbar_main.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		else:
			self.main_window.ui.toolbar_main.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
			
		if self.ui.checkbox_enable_autosave.isChecked():
			self.main_window.autosave_interval = 60000 * self.ui.spinbox_autosave_interval.value()
		else:
			self.main_window.autosave_interval = 0
		self.main_window.start_autosave_timer()
			
		self.main_window.auto_check_update = self.ui.checkbox_auto_update_check.isChecked()
		self.main_window.opensesamerun = self.ui.checkbox_opensesamerun.isChecked()
		
		self.ui.edit_opensesamerun_exec.setEnabled(self.ui.checkbox_opensesamerun.isChecked() and not self.ui.checkbox_auto_opensesamerun_exec.isChecked())
		self.ui.label_opensesamerun_exec.setEnabled(self.ui.checkbox_opensesamerun.isChecked() and not self.ui.checkbox_auto_opensesamerun_exec.isChecked())
		
		if self.ui.checkbox_auto_opensesamerun_exec.isChecked():
			self.main_window.opensesamerun_exec = ""
			self.ui.edit_opensesamerun_exec.setText("")
		else:
			if self.ui.edit_opensesamerun_exec.text() == "":
				if os.name == "nt":
					self.ui.edit_opensesamerun_exec.setText("opensesamerun.exe")
				else:
					self.ui.edit_opensesamerun_exec.setText("opensesamerun")
			self.main_window.opensesamerun_exec = str(self.ui.edit_opensesamerun_exec.text())
			
		self.main_window.save_state()
