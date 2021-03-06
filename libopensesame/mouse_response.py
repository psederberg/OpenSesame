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

from libopensesame import item, exceptions, generic_response
import openexp.response
import openexp.exceptions

class mouse_response(item.item, generic_response.generic_response):

	def __init__(self, name, experiment, string = None):
	
		"""
		Initialize the loop
		"""
		
		self.show_cursor = "yes"
		self.item_type = "mouse_response"
		self.timeout = "infinite"	
		self.description = "Collects mouse responses"
		self.auto_response = 1
		
		self.resp_codes = {}
		self.resp_codes[None] = "timeout"
		self.resp_codes[1] = "left_button"
		self.resp_codes[2] = "middle_button"
		self.resp_codes[3] = "right_button"
		self.resp_codes[4] = "scroll_up"
		self.resp_codes[5] = "scroll_down"
		
		item.item.__init__(self, name, experiment, string)	
		
	def prepare(self):
	
		"""
		Prepare the allowed responses for the mouse_response item
		"""
		
		item.item.prepare(self)		
		
		self._allowed_responses = []					 
		if self.has("allowed_responses"):
			for r in str(self.get("allowed_responses")).split(";"):			
				if r in self.resp_codes.values():
					for code, resp in self.resp_codes.items():
						if resp == r:
							self._allowed_responses.append(code)
				else:
					try:
						r = int(r)
						if r in self.resp_codes:
							self._allowed_responses.append(r)
						else:
							raise exceptions.runtime_error("Unknown allowed_response '%s' in mouse_response item '%s'" % (r, self.name))
					except ValueError:
						raise exceptions.runtime_error("Unknown allowed_response '%s' in mouse_response item '%s'" % (r, self.name))						
					
			if len(self._allowed_responses) == 0:
				raise exceptions.runtime_error("'%s' are not valid allowed responses in keyboard_response '%s'" % (self.get("allowed_responses"), self.name))
		else:
			self._allowed_responses = None
			
		if self.experiment.auto_response:
			self._resp_func = self.auto_responder
		else:
			self._resp_func = openexp.response.get_mouse		

		self.prepare_timeout()			
						
		return True		
						
	def run(self):
	
		"""
		Run the mouse_response item
		"""
	
		# Record the onset of the current item
		self.set_item_onset()
				
		if self.show_cursor == "yes":
			openexp.response.set_mouse_cursor_visible(True)
		
		# If no start response interval has been set, set it to the onset of
		# the current response item
		if self.experiment.start_response_interval == None:
			self.experiment.start_response_interval = self.get("time_%s" % self.name)

		# Get the response
		self.experiment.end_response_interval, resp, pos = self._resp_func(self._allowed_responses, self._timeout)
		
		# Do some bookkeeping
		self.experiment.response_time = self.experiment.end_response_interval - self.experiment.start_response_interval	
		self.experiment.cursor_x = pos[0]
		self.experiment.cursor_y = pos[1]
		self.experiment.total_response_time += self.experiment.response_time
		self.experiment.total_responses += 1
		self.experiment.response = self.resp_codes[resp]
				
		if self.has("correct_response"):
			correct_response = self.get("correct_response")			
			try:
				correct_response = self.resp_codes[int(correct_response)]
			except:
				pass			
		else:
			correct_response = "undefined"
			
		self.process_response(correct_response)	
		
		openexp.response.set_mouse_cursor_visible(False)				
				
		# Report success
		return True
				
	def to_string(self):
	
		"""
		Encode the keyboard_response as string
		"""
	
		s = item.item.to_string(self, "mouse_response")
		return s
		
	def var_info(self):
	
		"""
		Give a list of dictionaries with variable descriptions
		"""
		
		l = item.item.var_info(self)
		l.append( ("response", "<i>Depends on response</i>") )
		l.append( ("correct", "<i>Depends on response</i>") )
		l.append( ("response_time", "<i>Depends on response</i>") )
		l.append( ("cursor_x", "<i>Depends on response</i>") )
		l.append( ("cursor_y", "<i>Depends on response</i>") )
		l.append( ("average_response_time", "<i>Depends on response</i>") )
		l.append( ("avg_rt", "<i>Depends on response</i>") )		
		l.append( ("accuracy", "<i>Depends on response</i>") )		
		l.append( ("acc", "<i>Depends on response</i>") )		
						
		return l					
