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
import openexp.canvas
import openexp.exceptions
import openexp.response
import shlex

class sketchpad(item.item):

	def __init__(self, name, experiment, string = None):
		
		self.duration = "keypress"
		self.start_response_interval = "no"
		self.items = []
		self.item_type = "sketchpad"
		self.numeric_attrs = "x", "y", "x1", "y1", "r", "w", "h", "scale", "font_size", "penwidth", "arrow_size", "center", "fill", "orient", "freq", "phase", "stdev", "size"
		
		if not hasattr(self, "description"):
			self.description = "Displays stimuli"		
		item.item.__init__(self, name, experiment, string)
		
	def unfix_coordinates(self, item):
	
		"""
		Interprets the coordinates based on whether coordinates
		is set to absolute or relative.
		Raw coordinates -> Raw/ relative
		"""
		
		item = item.copy()
		if self.get("coordinates") == "relative":
			for var in item:
				if var in ["x", "x1", "x2"]:
					item[var] -= self.get("width") / 2
				if var in ["y", "y1", "y2"]:
					item[var] -= self.get("height") / 2
		return item		
		
	def fix_coordinates(self, item):
	
		"""
		Interprets the coordinates based on whether coordinates
		is set to absolute or relative.
		Raw/ relative -> Raw coordinates
		"""
		
		item = item.copy()
		if self.get("coordinates") == "relative":
			for var in item:
				if var in ["x", "x1", "x2"]:
					item[var] += self.get("width") / 2
				if var in ["y", "y1", "y2"]:
					item[var] += self.get("height") / 2
		return item
		
	def check_type(self, item):
	
		"""
		Throw an exception if an attribute which should be numeric is not
		"""
		
		for attr in item:
			if attr in self.numeric_attrs and type(item[attr]) == str:
				raise exceptions.runtime_error("'%s' should be numeric, not '%s', in sketchpad '%s'" % (attr, item[attr], self.name))
		
	def prepare(self):			
	
		"""
		Draw the canvas in preparation, so we can dump
		it without delay in the run phase
		"""
		
		item.item.prepare(self)		

		# Build the canvas	
		try:
			self.canvas = openexp.canvas.canvas(self.experiment, self.get("background"), self.get("foreground"))
		except ValueError as e:
			raise exceptions.runtime_error("An invalid background or foreground color has been specified")			

		for _item in self.items:
		
			if eval(self.compile_cond(_item["show_if"])):
		
				# Replace all variables by the actual values. In text, floats should
				# be rounded, but not in other variables
				tmp = {}
				for var in _item:
					if var == "text":
						tmp[var] = self.eval_text(_item[var], round_float = True)
					else:
						tmp[var] = self.eval_text(_item[var])
				
				# Check if the types are proper, i.e. no non-numeric Y-values etc.
				self.check_type(tmp)
				
				# Translate the coordinates to absolute (if necessary)
				_item = self.fix_coordinates(tmp)			
		
				# Set the foreground color and the penwidth
				try:
					self.canvas.set_fgcolor(_item["color"])
				except ValueError as e:
					raise exceptions.runtime_error("'%s' is not a valid color in sketchpad '%s'" % (_item["color"], self.name))							
				self.canvas.set_penwidth(_item["penwidth"])
					
				# Draw the items
				if _item["type"] == "rect":
					self.canvas.rect(_item["x"], _item["y"], _item["w"], _item["h"], _item["fill"] == 1)
				elif _item["type"] == "circle":
					self.canvas.ellipse(_item["x"] - 0.5 * _item["r"], _item["y"] - 0.5 * _item["r"], _item["r"], _item["r"], _item["fill"] == 1)
				elif _item["type"] == "ellipse":
					self.canvas.ellipse(_item["x"], _item["y"], _item["w"], _item["h"], _item["fill"] == 1)
				elif _item["type"] == "fixdot":
					self.canvas.fixdot(_item["x"], _item["y"])
				elif _item["type"] == "arrow":
					self.canvas.arrow(_item["x1"], _item["y1"], _item["x2"], _item["y2"], _item["arrow_size"])
				elif _item["type"] == "line":
					self.canvas.line(_item["x1"], _item["y1"], _item["x2"], _item["y2"])
				elif _item["type"] == "textline":
					self.canvas.set_font(_item["font_family"], _item["font_size"])
					self.canvas.text(self.experiment.unsanitize(str(_item["text"])), _item["center"] == 1, _item["x"], _item["y"])
				elif _item["type"] == "image":
					try:
						self.canvas.image(self.experiment.get_file(_item["file"]), _item["center"] == 1, _item["x"], _item["y"], _item["scale"])
					except openexp.exceptions.canvas_error as e:
					
						# Drawing an image can fail because the image format is not recognized or because the image file
						# cannot be found
						if self.experiment.file_in_pool(_item["file"]):					
							raise exceptions.runtime_error("'%s' is not a supported image format in sketchpad '%s'" % (_item["file"], self.name))
						else:
							raise exceptions.runtime_error("'%s' could not be found in sketchpad '%s'. Make sure that the file is present in the file pool (or specify the full location of the image in the script editor)." % (_item["file"], self.name))
							
				elif _item["type"] == "gabor":
					self.canvas.gabor(_item["x"], _item["y"], _item["orient"], _item["freq"], _item["env"], _item["size"], _item["stdev"], _item["phase"], _item["color1"], _item["color2"], _item["bgmode"])
				elif _item["type"] == "noise":
					self.canvas.noise_patch(_item["x"], _item["y"], _item["env"], _item["size"], _item["stdev"], _item["color1"], _item["color2"], _item["bgmode"])
					
					
		self.prepare_duration()
											
		return True		
		
	def run(self):
	
		"""
		Show the display
		"""				
	
		# Show
		self.set_item_onset(self.canvas.show())			
		if self.start_response_interval == "yes":
			self.experiment.start_response_interval = self.get("time_%s" % self.name)

		# And wait
		self._duration_func()		
			
		return True		
		
	def parse_item(self, l):
	
		"""
		Parse the generic draw attributes, that apply
		to all drawing primitives
		"""
		
		item = {}
		
		item["penwidth"] = 1
		item["color"] = self.get("foreground")
		item["type"] = "undefined"
		item["fill"] = 0
		item["arrow_size"] = 20
		item["center"] = 1
		item["scale"] = 1.0
		item["font_family"] = self.experiment.font_family
		item["font_size"] = self.experiment.font_size
		
		item["orient"] = 0
		item["freq"] = 0.1
		item["env"] = "gaussian"
		item["size"] = 96
		item["stdev"] = 12
		item["phase"] = 0
		item["color1"] = "white"
		item["color2"] = "black"
		item["bgmode"] = "avg"
		
		item["show_if"] = "always"
		
		for i in l:				
			j = i.find("=")
			if j != -1:
				var = i[:j]
				val = i[j+1:]
				item[var] = self.auto_type(val)
			
		return item
		
	def parse_rect_ellipse(self, line, l, item, item_type):
	
		"""
		Parse a rectangle
		"""
		
		if len(l) < 6:
			raise exceptions.script_error("Invalid draw %s command '%s', expecting 'draw %s [x] [y] [w] [h]'" % (item_type, line, item_type))
			
		item["type"] = item_type
			
		item["x"] = self.auto_type(l[2])
		item["y"] = self.auto_type(l[3])
		item["w"] = self.auto_type(l[4])
		item["h"] = self.auto_type(l[5])
		
		return item
		
	def parse_circle(self, line, l, item):
	
		"""
		Parse a circle
		"""
		
		if len(l) < 5:
			raise exceptions.script_error("Invalid draw circle command '%s', expecting 'draw circle [x] [y] [r]'" % line)
			
		item["type"] = "circle"
		item["x"] = self.auto_type(l[2])
		item["y"] = self.auto_type(l[3])
		item["r"] = self.auto_type(l[4])
		
		return item
		
	def parse_fixdot(self, line, l, item):
	
		"""
		Parse fixation dot
		"""
	
		item["type"] = "fixdot"				
		if len(l) > 3:
			item["x"] = self.auto_type(l[2])
			item["y"] = self.auto_type(l[3])
		else:
			item["x"] = self.get("width") / 2
			item["y"] = self.get("height") / 2
		return item
		
	def parse_line_arrow(self, line, l, item, item_type):
		
		"""
		Parse a line or arrow
		"""
		
		if len(l) < 6:
			raise exceptions.script_error("Invalid draw %s command '%s', expecting 'draw %s [x1] [y1] [x2] [y2]'" % (item_type, line, item_type))
			
		item["type"] = item_type
			
		item["x1"] = self.auto_type(l[2])
		item["y1"] = self.auto_type(l[3])
		item["x2"] = self.auto_type(l[4])
		item["y2"] = self.auto_type(l[5])
		
		return item	
		
	def parse_textline(self, line, l, item):
	
		"""
		Parse text
		"""
	
		if len(l) < 3:
			raise exceptions.script_error("Invalid draw textline command '%s', expecting 'draw textline [x] [y] [text]' or 'draw textline [text]'" % line)
			
		item["type"] = "textline"
		try:
			item["x"] = self.auto_type(l[2])
			item["y"] = self.auto_type(l[3])
			item["text"] = l[4]
		except:
			item["x"] = self.get("width") / 2
			item["y"] = self.get("height") / 2	
			item["text"] = l[2]
						
		return item
		
	def parse_image(self, line, l, item):
	
		"""
		Parse image
		"""
	
		if len(l) < 3:
			raise exceptions.script_error("Invalid draw image command '%s', expecting 'draw image [x] [y] [file]' or 'draw textline [file]'" % line)
			
		item["type"] = "image"
		try:
			item["x"] = self.auto_type(l[2])
			item["y"] = self.auto_type(l[3])
			item["file"] = l[4]
		except:
			item["x"] = self.get("width") / 2
			item["y"] = self.get("height") / 2	
			item["file"] = l[2]
						
		return item		
		
	def parse_gabor(self, line, l, item):
	
		"""
		Parse Gabor patch				
		"""
		
		if len(l) < 4:
			raise exceptions.script_error("Invalid draw image command '%s', expecting 'draw gabor [x] [y] [orient] [freq]'" % line)
			
		item["type"] = "gabor"
		item["x"] = self.auto_type(l[2])
		item["y"] = self.auto_type(l[3])						
		
		return item
		
	def parse_noise(self, line, l, item):
	
		"""
		Parse Gabor patch				
		"""
		
		if len(l) < 4:
			raise exceptions.script_error("Invalid draw image command '%s', expecting 'draw noise [x] [y]'" % line)
			
		item["type"] = "noise"
		item["x"] = self.auto_type(l[2])
		item["y"] = self.auto_type(l[3])						
		
		return item				
			
	def from_string(self, string):
	
		"""
		Read a sketchpad from string
		"""
		
		for line in string.split("\n"):
			if not self.parse_variable(line):
				l = shlex.split(line)
				if len(l) > 0:
										
					if l[0] == "draw":
				
						item = self.parse_item(l)
						if l[1] in ("circle",):
							item = self.parse_circle(line, l, item)
						elif l[1] in ("rectangle", "rect"):
							item = self.parse_rect_ellipse(line, l, item, "rect")
						elif l[1] in ("fixdot", "fixation"):
							item = self.parse_fixdot(line, l, item)
						elif l[1] in ("ellipse", "oval"):
							item = self.parse_rect_ellipse(line, l, item, "ellipse")
						elif l[1] in ("arrow",):
							item = self.parse_line_arrow(line, l, item, "arrow")
						elif l[1] in ("line",):
							item = self.parse_line_arrow(line, l, item, "line")
						elif l[1] in ("textline",):
							item = self.parse_textline(line, l, item)
						elif l[1] in ("image", "bitmap"):
							item = self.parse_image(line, l, item)
						elif l[1] in ("gabor"):
							item = self.parse_gabor(line, l, item)
						elif l[1] in ("noise"):
							item = self.parse_noise(line, l, item)
						else:
							raise exceptions.script_error("Unknown draw command '%s'" % line)

						self.items.append(item)
					
					else:
					
						raise exceptions.script_error("Unknown command '%s'" % line)
					
	def relativize(self, item, compensation, varlist):
	
		"""
		Reset coordinates so that 0, 0 is the center
		"""
	
		for var in varlist:
			if var in item:
				item[var] -= compensation			
		return item
			
	def item_to_string(self, _item):
	
		"""
		Encode item as string
		"""
				
		if _item["type"] == "rect":
			return "draw rect %s %s %s %s fill=%s penwidth=%s color=%s show_if=\"%s\"" % (_item["x"], _item["y"], _item["w"], _item["h"], _item["fill"], _item["penwidth"], _item["color"], _item["show_if"])
		elif _item["type"] == "circle":
			return "draw circle %s %s %s fill=%s penwidth=%s color=%s show_if=\"%s\"" % (_item["x"], _item["y"], _item["r"], _item["fill"], _item["penwidth"], _item["color"], _item["show_if"])			
		elif _item["type"] == "ellipse":
			return "draw ellipse %s %s %s %s fill=%s penwidth=%s color=%s show_if=\"%s\"" % (_item["x"], _item["y"], _item["w"], _item["h"], _item["fill"], _item["penwidth"], _item["color"], _item["show_if"])
		elif _item["type"] == "fixdot":
			return "draw fixdot %s %s color=%s show_if=\"%s\"" % (_item["x"], _item["y"], _item["color"], _item["show_if"])
		elif _item["type"] == "arrow":
			return "draw arrow %s %s %s %s penwidth=%s color=%s arrow_size=%s show_if=\"%s\"" % (_item["x1"], _item["y1"], _item["x2"], _item["y2"], _item["penwidth"], _item["color"], _item["arrow_size"], _item["show_if"])
		elif _item["type"] == "line":
			return "draw line %s %s %s %s penwidth=%s color=%s show_if=\"%s\"" % (_item["x1"], _item["y1"], _item["x2"], _item["y2"], _item["penwidth"], _item["color"], _item["show_if"])
		elif _item["type"] == "textline":
			return "draw textline %s %s \"%s\" center=%d color=%s font_family=%s font_size=%s show_if=\"%s\"" % (_item["x"], _item["y"], self.experiment.sanitize(_item["text"]), _item["center"], _item["color"], _item["font_family"], _item["font_size"], _item["show_if"])	
		elif _item["type"] == "image":
			return "draw image %s %s \"%s\" scale=%s center=%d show_if=\"%s\"" % (_item["x"], _item["y"], _item["file"], _item["scale"], _item["center"], _item["show_if"])							
		elif _item["type"] == "gabor":
			return "draw gabor %(x)s %(y)s orient=%(orient)s freq=%(freq)s env=%(env)s size=%(size)s stdev=%(stdev)s phase=%(phase)s color1=%(color1)s color2=%(color2)s bgmode=%(bgmode)s show_if=\"%(show_if)s\"" % _item
		elif _item["type"] == "noise":
			return "draw noise %(x)s %(y)s env=%(env)s size=%(size)s stdev=%(stdev)s color1=%(color1)s color2=%(color2)s bgmode=%(bgmode)s show_if=\"%(show_if)s\"" % _item			
				
	def to_string(self):
	
		"""
		Encode sketchpad as string
		"""
	
		s = item.item.to_string(self, self.item_type)
				
		for _item in self.items:
			s += "\t%s\n" % self.item_to_string(_item)				
				
		return s
