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

import copy
import libopensesame.loop
import libqtopensesame.qtitem
import libqtopensesame.loop_wizard_dialog_ui
import libqtopensesame.good_looking_table
from PyQt4 import QtCore, QtGui

class loop_table(libqtopensesame.good_looking_table.good_looking_table):

	"""
	The looptable extends the QtTableWidget
	to allow copying and pasting
	"""

	def __init__(self, loop, rows, columns, parent=None):
	
		self.pos = None
		self.loop = loop
		self.lock = False
		
		icons = {}
		icons["cut"] = self.loop.experiment.icon("cut")
		icons["copy"] = self.loop.experiment.icon("copy")
		icons["paste"] = self.loop.experiment.icon("paste")
		icons["clear"] = self.loop.experiment.icon("clear")
		
		libqtopensesame.good_looking_table.good_looking_table.__init__(self, rows, columns, icons, parent)
		
		QtCore.QObject.connect(self, QtCore.SIGNAL("cellChanged(int, int)"), self.apply_changes)							
				
	def paste(self):
	
		"""
		Paste data from the clipboard into the table
		"""
			
		self.lock = True
		libqtopensesame.good_looking_table.good_looking_table.paste(self)	
		self.lock = False
		self.apply_changes()
		
	def _clear(self):
		
		"""
		Clear the table
		"""
	
		self.lock = True
		libqtopensesame.good_looking_table.good_looking_table._clear(self)	
		self.lock = False
		self.apply_changes()
		
	def apply_changes(self):
	
		"""
		Apply changes to the table and make sure that
		the cursor is restored to its previous position
		"""
	
		if self.lock:
			return		
		
		self.loop.apply_edit_changes()
				
class loop(libopensesame.loop.loop, libqtopensesame.qtitem.qtitem):

	def __init__(self, name, experiment, string = None):
	
		"""
		Initialize the experiment		
		"""
		
		libopensesame.loop.loop.__init__(self, name, experiment, string)
		libqtopensesame.qtitem.qtitem.__init__(self)		
		
	def rename(self, from_name, to_name):
	
		"""
		Renames an item
		"""
		
		libqtopensesame.qtitem.qtitem.rename(self, from_name, to_name)
		if self.item == from_name:
			self.item = to_name	
			
	def add_cycle(self):
	
		"""
		Add a cycle
		"""
	
		self.set("cycles", self.get("cycles") + 1)
		self.refresh_loop_table()
		self.apply_edit_changes()		
		
	def add_cycles(self):
	
		"""
		Add multiple cycles
		"""
		
		nr, ok = QtGui.QInputDialog.getInt(self._edit_widget, "Add multiple cycles", "How many cycles do you want to add?", min=1)
		if ok:
			self.set("cycles", self.get("cycles") + nr)
			self.refresh_loop_table()
			self.apply_edit_changes()			
		
	def remove_cycle(self):
	
		"""
		Remove a cycle
		"""
		
		cycle_count = self.get("cycles") - 1
		if cycle_count < 0:
			return
		self.set("cycles", cycle_count)
		
		l = []
		for i in self.matrix:
			if i >= cycle_count:
				l.append(i)	
		
		for i in l:
			del self.matrix[i]
				
		self.refresh_loop_table()
		self.apply_edit_changes()
		
		
	def add_cyclevar(self):
	
		"""
		Add a variable
		"""
		
		var_name, ok = QtGui.QInputDialog.getText(self.loop_table, 'New variable', 'Enter a variable name, optionally followed by a default value (i.e., \"varname defaultvalue\")')
	
		if ok:								
			l = self.cyclevar_list()
			
			var_name = str(var_name)			
			
			# Split by space, because a name may be followed by a default value
			if len(var_name.split()) > 1:
				default = self.experiment.sanitize(var_name.split()[1])
				var_name = var_name.split()[0]
			else:
				default = ""
				
			# Check for valid variable names
			var_name = self.experiment.sanitize(var_name, True)
			if var_name == "":
				self.experiment.notify("Variable names must consist of alphanumeric characters and underscores, and must not be empty")
				return	
				
			# Check if the variable already exists
			if l != None and var_name in l:
				self.experiment.notify("A variable with the name '%s' already exists" % var_name)
				return								
		
			for i in range(self.cycles):
				if i not in self.matrix:
					self.matrix[i] = {}
				self.matrix[i][var_name] = default

			self.refresh_loop_table()			
			self.apply_edit_changes()			
			
	def cyclevar_list(self):
	
		"""
		Return a list of variables
		"""		
		
		var_list = []
		for i in self.matrix:
			for var in self.matrix[i]:
				if var not in var_list:
					var_list.append(var)
					
		if len(var_list) == 0:
			return None
			
		return var_list						
			
	def rename_cyclevar(self):
	
		"""
		Rename a variable
		"""
		
		var_list = self.cyclevar_list()
		if var_list == None:
			return
			
		old_var, ok = QtGui.QInputDialog.getItem(self.experiment.ui.centralwidget, "Remove variable", "Which variable do you want to rename?", var_list)				
		if ok:		
			new_var, ok = QtGui.QInputDialog.getText(self.loop_table, 'New variable', 'Enter a new variable name', text = old_var)						
			if ok and new_var != old_var:
				old_var = str(old_var)
				new_var = str(new_var)
				
				if new_var in var_list:
					self.experiment.notify("A variable with the name '%s' already exists" % new_var)
					return
				
				for i in self.matrix:
					if old_var in self.matrix[i]:
						val = self.matrix[i][old_var]
						del self.matrix[i][old_var]
						self.matrix[i][new_var] = val
					
			self.refresh_loop_table()
			self.apply_edit_changes()				
			
	def remove_cyclevar(self):
	
		"""
		Remove a variable
		"""
		
		var_list = self.cyclevar_list()
		if var_list == None:
			return
			
		var, ok = QtGui.QInputDialog.getItem(self.experiment.ui.centralwidget, "Remove variable", "Which variable do you want to remove?", var_list)
		if ok:
			var = str(var)
			for i in self.matrix:
				if var in self.matrix[i]:
					del self.matrix[i][var]
					
			self.refresh_loop_table()
			self.apply_edit_changes()								
		
	def cyclevar_count(self):
	
		"""
		Returns the number of cycle vars
		"""
		
		l = []
		c = 0
		for cycle in self.matrix:			
			for var in self.matrix[cycle]:
				if var not in l:
					l.append(var)
					c += 1
		return c		
		
	def cycle_count(self):
	
		"""
		Returns the number of cycles
		"""
		
		return max(self.get("cycles"), len(self.matrix))
			
		
	def refresh_loop_table(self, lock = True):
	
		"""
		Build the table that contains all
		the cyclevars
		"""
				
		if lock:
			self.lock = True
				
		# Don't clear and resize the table if this is not necessary, because
		# this makes the cursor jump		
		if self.loop_table.rowCount() != self.cycles or self.loop_table.columnCount() != self.cyclevar_count():		
			self.loop_table.clear()
			self.loop_table.setRowCount(self.cycles)			
			self.loop_table.setColumnCount(self.cyclevar_count())

		# Determine the order in which the columns are displayed		
		column_order = []		
		if self.cyclevar_list() != None:		
			if self.has("column_order"):
				for var in str(self.get("column_order")).split(";"):
					if var in self.cyclevar_list():
						column_order.append(var)					
			for var in self.cyclevar_list():
				if var not in column_order:
					column_order.append(var)
				
		# Create the column headers
		i = 0
		for var in column_order:
			self.loop_table.setHorizontalHeaderItem(i, QtGui.QTableWidgetItem(var))
			i += 1
		
		# Fill the table
		var_columns = {}
		new_column = 0				
		for cycle in self.matrix:			
			for var in self.matrix[cycle]:							
				col = column_order.index(var)										
				self.loop_table.setItem(cycle, col, QtGui.QTableWidgetItem(str(self.matrix[cycle][var])))				
				
		# Store the number of cycles and the column order
		self.set("cycles", max(self.get("cycles"), self.cycle_count()))								
		self.set("column_order", ";".join(column_order))
		
		if lock:
			self.lock = False
		
	def wizard_process(self, d, l = []):
	
		"""
		Fills the cyclevars based on a dictionary of
		variables and levels
		"""

		if len(d) == 0:
			for var, val in l:
				if self.i not in self.matrix:
					self.matrix[self.i] = {}
				self.matrix[self.i][var] = val
			self.i += 1
			return
			
		var = d.keys()[0]

		for val in d[var]:
			_d = copy.copy(d)
			del _d[var]	

			self.wizard_process(_d, l + [(var, val)])		
		
	def wizard(self):
	
		"""
		Present the variable wizard
		"""
		
		a = QtGui.QDialog(self.experiment.main_window.ui.centralwidget)
		a.ui = libqtopensesame.loop_wizard_dialog_ui.Ui_Dialog()
		a.ui.setupUi(a)	
		a.ui.table_example.hide()
		
		a.ui.table_wizard.setRowCount(255)
		a.ui.table_wizard.setColumnCount(255)
		
		if a.exec_() == QtGui.QDialog.Accepted:			
		
			# First read the table into a dictionary of variables
			var_dict = {}				
			for col in range(a.ui.table_wizard.columnCount()):
				var = None
				for row in range(a.ui.table_wizard.rowCount()):
					item = a.ui.table_wizard.item(row, col)
					if item == None:
						break
					s = str(item.text())									
					if row == 0:
						var = self.experiment.sanitize(s, True)						
						var_dict[var] = []
					elif var != None:
						var_dict[var].append(self.experiment.sanitize(s))
						
			self.i = 0
			self.matrix = {}
			self.wizard_process(var_dict)	
			self.set("cycles", len(self.matrix))
			self.refresh_loop_table()
					
					
	def init_edit_widget(self):
	
		"""
		Build the loop edit widget
		"""
		
		self.lock = True
		
		libqtopensesame.qtitem.qtitem.init_edit_widget(self, False)
		
		row = 3
		self.edit_grid.addWidget(QtGui.QLabel("Item to run"), row, 0)
		self.edit_item = self.experiment.item_combobox(self.item, [self.name])
		self.edit_item.setToolTip("Select the item that is called by the loop")
		
		QtCore.QObject.connect(self.edit_item, QtCore.SIGNAL("currentIndexChanged(int)"), self.apply_edit_changes)
		self.edit_grid.addWidget(self.edit_item, row, 1)
				
		row += 1
		self.edit_grid.addWidget(QtGui.QLabel("Repeat"), row, 0)
		
		self.spin_repeat = QtGui.QDoubleSpinBox()
		self.spin_repeat.setMinimum(0)
		self.spin_repeat.setMaximum(1000000)
		self.spin_repeat.setToolTip("The number of times that all cycles are repeat. The number of times that the 'item to run' is executed is [repeat] x [number of cycles]. Values below 1 mean that not all cycles are executed.")		
		self.spin_repeat.valueChanged.connect(self.apply_edit_changes)
		self.edit_grid.addWidget(self.spin_repeat, row, 1)
		
		row += 1
		
		self.combobox_order = QtGui.QComboBox()
		self.combobox_order.addItem("random")
		self.combobox_order.setItemIcon(0, self.experiment.icon("random"))
		self.combobox_order.addItem("sequential")
		self.combobox_order.setItemIcon(1, self.experiment.icon("sequential"))
		self.combobox_order.setToolTip("The order in which the cycles are executed. If set to random, ranomization occurs over all [repeat] x [number of cycles] runs.")

		self.edit_grid.addWidget(QtGui.QLabel("Order"), row, 0)		
		self.edit_grid.addWidget(self.combobox_order, row, 1)
		QtCore.QObject.connect(self.combobox_order, QtCore.SIGNAL("currentIndexChanged(int)"), self.apply_edit_changes)
		self.edit_grid.addWidget(self.combobox_order, row, 1)													
		
		row += 1
		self.button_add_cycle = QtGui.QPushButton(self.experiment.icon("add"), "Add cycle")
		self.button_add_cycle.setIconSize(QtCore.QSize(16,16))
		self.button_add_cycle.setToolTip("Add a single cycle")
		QtCore.QObject.connect(self.button_add_cycle, QtCore.SIGNAL("clicked()"), self.add_cycle)

		self.button_add_cycles = QtGui.QPushButton(self.experiment.icon("add"), "Add multiple cycles")
		self.button_add_cycles.setIconSize(QtCore.QSize(16,16))
		self.button_add_cycles.setToolTip("Add multiple single cycles")		
		QtCore.QObject.connect(self.button_add_cycles, QtCore.SIGNAL("clicked()"), self.add_cycles)

		self.button_remove_cycle = QtGui.QPushButton(self.experiment.icon("delete"), "Remove cycle")
		self.button_remove_cycle.setIconSize(QtCore.QSize(16,16))
		self.button_remove_cycle.setToolTip("Remove the last cycle")		
		QtCore.QObject.connect(self.button_remove_cycle, QtCore.SIGNAL("clicked()"), self.remove_cycle)		

		self.button_add_cyclevar = QtGui.QPushButton(self.experiment.icon("add"), "Add variable")
		self.button_add_cyclevar.setIconSize(QtCore.QSize(16,16))
		self.button_add_cyclevar.setToolTip("Add a variable")		
		QtCore.QObject.connect(self.button_add_cyclevar, QtCore.SIGNAL("clicked()"), self.add_cyclevar)

		self.button_rename_cyclevar = QtGui.QPushButton(self.experiment.icon("rename"), "Rename variable")
		self.button_rename_cyclevar.setIconSize(QtCore.QSize(16,16))
		self.button_rename_cyclevar.setToolTip("Rename a variable")		
		QtCore.QObject.connect(self.button_rename_cyclevar, QtCore.SIGNAL("clicked()"), self.rename_cyclevar)
		
		self.button_remove_cyclevar = QtGui.QPushButton(self.experiment.icon("delete"), "Remove variable")
		self.button_remove_cyclevar.setIconSize(QtCore.QSize(16,16))
		self.button_remove_cyclevar.setToolTip("Remove a variable")		
		QtCore.QObject.connect(self.button_remove_cyclevar, QtCore.SIGNAL("clicked()"), self.remove_cyclevar)
		
		self.button_wizard = QtGui.QPushButton(self.experiment.icon("wizard"), "Variable wizard")
		self.button_wizard.setIconSize(QtCore.QSize(16,16))
		self.button_wizard.setToolTip("Easy way to create large variable tables")		
		QtCore.QObject.connect(self.button_wizard, QtCore.SIGNAL("clicked()"), self.wizard)		
				
		hbox = QtGui.QHBoxLayout()		
		hbox.addWidget(self.button_add_cycle)
		hbox.addWidget(self.button_add_cycles)
		hbox.addWidget(self.button_remove_cycle)
		hbox.addWidget(self.button_add_cyclevar)
		hbox.addWidget(self.button_rename_cyclevar)		
		hbox.addWidget(self.button_remove_cyclevar)
		hbox.addStretch()
		hbox.addWidget(self.button_wizard)		
		hbox.setMargin(0)
		
		widget = QtGui.QWidget()
		widget.setLayout(hbox)
		self.edit_vbox.addSpacing(16)
		self.edit_vbox.addWidget(widget)				
				
		self.loop_table = loop_table(self, self.cycles, self.cyclevar_count())		
		self.edit_vbox.addWidget(self.loop_table)
		
		self.lock = False
		
		return self._edit_widget		
					
	def edit_widget(self):
	
		"""
		Set the controls from the variables
		"""
		
		self.lock = True
		
		libqtopensesame.qtitem.qtitem.edit_widget(self)
		
		self.refresh_loop_table(lock = False)
		
		self.edit_item.deleteLater()
		self.edit_item = self.experiment.item_combobox(self.item, [self.name])
		QtCore.QObject.connect(self.edit_item, QtCore.SIGNAL("currentIndexChanged(int)"), self.apply_edit_changes)
		self.edit_grid.addWidget(self.edit_item, 3, 1)
		
		# For some reason, refilling the combobox, rather than recreating it, causes a nasty
		# loop. Not sure why.
		# self.experiment.item_combobox(self.item, self.parents(), self.edit_item)
		
		try:
			self.spin_repeat.setValue(float(self.get("repeat")))
		except:
			self.experiment.notify("'%s' is not a valid value for repeat. Expecting a positive numeric value.")
			self.spin_repeat.setValue(1)
			self.set("repeat", 1)
			
		self.combobox_order.setCurrentIndex(self.combobox_order.findText(str(self.get("order"))))								
		
		self.lock = False
		return self._edit_widget
		
	def apply_edit_changes(self, dummy = None):
	
		"""
		Apply all the changes made using the edit widget. Notably,
		set the repeat, cycles and all the cyclevars
		"""
		
		if not libqtopensesame.qtitem.qtitem.apply_edit_changes(self, False) or self.lock:
			return
			
		self.lock = True
		
		item = str(self.edit_item.currentText())
		self.set("item", item)		
		self.set("repeat", self.spin_repeat.value()) 
		self.set("order", str(self.combobox_order.currentText()))
		
		self.matrix = {}
		for row in range(self.loop_table.rowCount()):
			self.matrix[row] = {}
			for col in range(self.loop_table.columnCount()):							
										
				var = str(self.loop_table.horizontalHeaderItem(col).text())
				
				cell = self.loop_table.item(row, col)
				if cell == None:
					val = ""
				else:				
					val = self.auto_type(str(self.loop_table.item(row, col).text()))
					
				self.matrix[row][var] = val
				
		row = self.loop_table.currentRow()
		column = self.loop_table.currentColumn()
				
		self.experiment.main_window.refresh(self.name)
		
		self.loop_table.setCurrentCell(row, column)
		
		self.lock = False
		
	def build_item_tree(self, toplevel, items):
	
		"""
		Construct an item tree
		"""
	
		widget = QtGui.QTreeWidgetItem(toplevel)
		widget.setText(0, self.name)
		widget.setIcon(0, self.experiment.icon("loop"))
		widget.name = self.name
		widget.setToolTip(0, "Type: %s\nDescription: %s" % (self.item_type, self.description))		
		toplevel.addChild(widget)	
	
		if self.item in self.experiment.items and self.item != None and self.item.strip() != "":
			if self.experiment.items[self.item] not in items:
				items.append(self.experiment.items[self.item])
			self.experiment.items[self.item].build_item_tree(widget, items)
			
		widget.setExpanded(True)			
					
		return items										
				
	def is_offspring(self, item):
	
		"""
		Checks if the item is offspring
		of the current item
		"""
		
		return self.item == item or (self.item in self.experiment.items and self.experiment.items[self.item].is_offspring(item))
		
		
