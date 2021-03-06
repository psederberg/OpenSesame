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

from libopensesame import item, exceptions
import openexp.response
import shlex
import random

class loop(item.item):

	def __init__(self, name, experiment, string = None):
	
		"""
		Initialize the loop
		"""
	
		self.cycles = 1
		self.repeat = 1
		self.matrix = {}
		self.order = "random"
		self.description = "Repeatedly runs another item"		
		self.item_type = "loop"
		self.item = ""
		item.item.__init__(self, name, experiment, string)
		
	def from_string(self, string):
	
		"""
		Read a loop from a string
		"""

		for i in string.split("\n"):
							
			self.parse_variable(i)						
			
			# Extract the item to run
			i = shlex.split(i.strip())
			if len(i) > 0:
				if i[0] == "run" and len(i) > 1:				
					self.item = i[1]
					
				if i[0] == "setcycle" and len(i) > 3:
				
					cycle = int(i[1])
					var = i[2]
					val = i[3]
					try:
						if int(val) == float(val):
							val = int(val)
						else:
							val = float(val)
					except:
						pass
				
					if cycle not in self.matrix:
						self.matrix[cycle] = {}
					self.matrix[cycle][var] = val
					
	def run(self):
	
		"""
		Run the loop
		"""
	
		# First generate a list
		l = []
		
		j = 0

		# Walk through all complete repeats
		whole_repeats = int(self.repeat)		
		for j in range(whole_repeats):
			for i in range(self.cycles):
				l.append( (j, i) )

		# Add the leftover repeats		
		partial_repeats = self.repeat - whole_repeats
		if partial_repeats > 0:
			all_cycles = range(self.cycles)
			sample = random.sample(all_cycles, int(len(all_cycles) * partial_repeats))
			for i in sample:
				l.append( (j, i) )
						
		# Randomize the list if necessary
		if self.order == "random":
			random.shuffle(l)
			
		# Walk through the list
		for j, i in l:
			if self.item in self.experiment.items:
		
				# Set the variables from the matrix
				if i in self.matrix:
					for var in self.matrix[i]:
						val = self.matrix[i][var]
						if type(val) == str:
							exec("self.experiment.%s = \"%s\"" % (var, val))
						else:
							exec("self.experiment.%s = %s" % (var, val))
							
				# Flush the responses to catch escape presses
				openexp.response.flush()							
		
				if eval("self.experiment.items[\"%s\"].prepare()" % self.item):
					exec("self.experiment.items[\"%s\"].run()" % self.item)
				else:
					raise exceptions.runtime_error("Failed to prepare item '%s', which is called by loop item '%s'" % (self.item, self.name))
					
			else:
				raise exceptions.runtime_error("Could not find item '%s', which is called by loop item '%s'" % (self.item, self.name))
								
		return True
		
	def to_string(self):
	
		"""
		Encode as string
		"""
	
		s = item.item.to_string(self, "loop")
		for i in self.matrix:
			for var in self.matrix[i]:
				s += "\tsetcycle %d %s \"%s\"\n" % (i, var, self.matrix[i][var])
		s += "\trun %s\n" % self.item
		return s
		
	def var_info(self):
	
		"""
		Give a list of dictionaries with variable descriptions
		"""
		
		l = item.item.var_info(self)

		var_list = {}

		for i in self.matrix:
			for var in self.matrix[i]:
				if var not in var_list:
					var_list[var] = []
				var_list[var].append(str(self.matrix[i][var]))
				
		for var in var_list:
			l.append( (var, "<i>" + ", ".join(var_list[var]) + "</i>"))
		
		return l		
