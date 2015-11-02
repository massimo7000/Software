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

from tkinter import *
import tkinter.ttk

class frmMain(Tk):

	def __init__(self, parent):

		Tk.__init__(self, parent)

		self._fraMain = self
		
		import tkLayout
		tkLayout.loadLayout(self)
		
		self.findWidget(self, "scrollbar")
		scrY = self.widgetFind
		self.findWidget(self, "listbox")
		listbox = self.widgetFind
		listbox["yscrollcommand"] = scrY.set
		scrY.config(command=listbox.yview)
		for i in range(50):
			listbox.insert(END, "item " + str(i))		
		
	def mouse_click(self, event):
		if event.widget.name == "name = scrividati":		
			
			svar = StringVar()
			self.findWidget(self, "nome")
			self.widgetFind["textvariable"] = svar
			svar.set("massimo")
			
			svar = StringVar()
			self.findWidget(self, "cognome")
			self.widgetFind["textvariable"] = svar			
			svar.set("formisano")
			
			svar = StringVar()
			self.findWidget(self, "indirizzo")
			self.widgetFind["textvariable"] = svar
			svar.set("via pinco pallino, 1")
			
			svar = StringVar()
			self.findWidget(self, "citta")
			self.widgetFind["textvariable"] = svar
			svar.set("roma")
			
			svar = StringVar()
			self.findWidget(self, "telefono")
			self.widgetFind["textvariable"] = svar
			svar.set("333/6430347")
			
			self.findWidget(self, "chkTest")
			self.widgetFind.select()
			
	def mouse_move(self, event):
		pass

	def mouse_resize(self, event):
		pass

	def mouse_release(self, event):
		pass

	def findWidget(self, widget, name):
		
		for w in widget.winfo_children():						
			prop = w.name.split("=")			
			if prop[1].strip() == name:			
				self.widgetFind = w
			self.findWidget(w, name)
		
root = frmMain(None)
root.wm_title("Tkinter App by Formisano Massimo - Italia - Roma - 333/6430347")
root.geometry("1024x640+0+0")
#root.state("zoomed")
mainloop()
