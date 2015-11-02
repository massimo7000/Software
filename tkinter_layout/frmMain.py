#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  ---------------------------------------------------------------------
#  Realizzato da
#  Formisano Massimo
#  Nazione : Italia
#  Citta' : Roma
#  Cap : 00168
#  Cellulare : 336430347
#  email : borlisdeveloper@hotmail.com

from makeLayout import *
from tkinter import *
import tkinter.ttk

class frmMain(Tk):

	def __init__(self, parent):

		Tk.__init__(self, parent)

		# crea layout
		makeLayout("frmMainLayout")

		# importa layout
		from frmMainLayout import frmMainLayout

		# istanza layout Widgets
		self.W = frmMainLayout(self)

		# istanza listbox
		listbox = self.W.Widgets["listbox"]

		# fill item
		listbox.delete(0, END)
		for item in range(50):
			listbox.insert(END, "item " + str(item))

		# istanza combobox
		combobox = self.W.Widgets["combobox"]

		# fill item
		combobox.config(values = ["item 0", "item 1", "item 2"])

	def itemfile1(self):
		self.W.Widgets["entTest_StringVar"].set("click su menu file item1")
	
	def itemfile2(self):
		self.W.Widgets["entTest_StringVar"].set("click su menu file item2")
	
	def itemfile3(self):
		self.W.Widgets["entTest_StringVar"].set("click su menu file item3")
	
	def itemhelp1(self):
		self.W.Widgets["entTest_StringVar"].set("click su menu help item1")
	
	def itemhelp2(self):
		self.W.Widgets["entTest_StringVar"].set("click su menu help item2")
	
	def itemhelp3(self):
		self.W.Widgets["entTest_StringVar"].set("click su menu help item3")
		
	def evento1(self):
		self.W.Widgets["entTest_StringVar"].set("button 1")

	def evento2(self):
		self.W.Widgets["entTest_StringVar"].set("button 2")

	def evento3(self):
		self.W.Widgets["entTest_StringVar"].set("button 3")

	def evento4(self):
		self.W.Widgets["entTest_StringVar"].set("button 4")

	def evento5(self):
		self.W.Widgets["entTest_StringVar"].set("button 5")

root = frmMain(None)
root.wm_title("layout xml")
mainloop()
