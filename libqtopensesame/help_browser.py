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

from PyQt4 import QtCore, QtGui
import os.path

class help_browser(QtGui.QTextBrowser):

	"""
	A HTML browser for viewing help files
	"""
	
	def __init__(self, path, item, substitutions = [], parent = None):
	
		"""
		Constructor
		"""
	
		QtGui.QTextBrowser.__init__(self, parent)
		
		self.tab_name = "__help__%s__" % item
		
		self.setOpenExternalLinks(True)
		
		if os.path.exists(path):			
			html = open(path, "r").read()
		else:		
			html = "<b>No help available</b>"		
			
		html += "<hr /><p><i>Could not find an answer? You can ask questions and find more documentation on <a href='http://www.cogsci.nl/opensesame'>www.cogsci.nl/opensesame</a>.</i></p>"			
		
		for old, new in substitutions:
			html = html.replace(old, new)
		
		self.setHtml(html)
		
		
