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
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showerror

class frmMain(Tk):

	def __init__(self, parent):

		Tk.__init__(self, parent)

		self.startX = 0
		self.startY = 0
		self.oldX = 0
		self.oldY = 0
		self.gridAlignX = 5
		self.gridAlignY = 5
		self.widgetSelect = None
		self.startResize = False

		self._fraMain = Frame(self, relief="groove", border="3")
		self._fraMain.place(x=225, y=0, width="1024", height="640")

		self.__fraTools = Frame(self, relief="groove", border="3")
		self.__fraTools.place(x=0, y=0, width="225", height="640")
		self.__fraTools.grid_rowconfigure(0, weight=100)
		self.__fraTools.grid_columnconfigure(0, weight=100)

		scrY = Scrollbar(self.__fraTools)
		scrY.grid(row=0, column=2, sticky=N+S)

		self.__listbox = Listbox(self.__fraTools, relief="groove",  \
						border=0, yscrollcommand=scrY.set)
		self.__listbox.bind("<<ListboxSelect>>", self.proprieta_click)

		self.__lblProprieta = Label(self.__fraTools, text="None")
		self.__lblProprieta.grid(row=1, column=0, columnspan=2, sticky=W)

		self.__proprieta = StringVar()
		ent = Entry(self.__fraTools, text=self.__proprieta)
		ent.grid(row=2, column=0, columnspan=2, sticky=E+W )

		self.__saveproprieta = Button(self.__fraTools, text="Salva proprieta' Widget", fg="#00A000")
		self.__saveproprieta.grid(row=3, column=0, columnspan=2, sticky=E+W)
		self.__saveproprieta.bind("<Button-1>", self.saveproprieta_click)

		btn = Button(self.__fraTools, text="Frame", fg="#0000FF")
		btn.grid(row=4, column=0, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)

		btn = Button(self.__fraTools, text="Label", fg="#0000FF")
		btn.grid(row=4, column=1, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)

		btn = Button(self.__fraTools, text="Entry", fg="#0000FF")
		btn.grid(row=5, column=0, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)

		btn = Button(self.__fraTools, text="Button", fg="#0000FF")
		btn.grid(row=5, column=1, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)

		btn = Button(self.__fraTools, text="Checkbutton", fg="#0000FF")
		btn.grid(row=6, column=0, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)

		btn = Button(self.__fraTools, text="Canvas", fg="#0000FF")
		btn.grid(row=6, column=1, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)

		btn = Button(self.__fraTools, text="tkinter.ttk.Progressbar", fg="#0000FF")
		btn.grid(row=7, column=0, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)

		btn = Button(self.__fraTools, text="Listbox", fg="#0000FF")
		btn.grid(row=7, column=1, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)

		btn = Button(self.__fraTools, text="tkinter.ttk.Combobox", fg="#0000FF")
		btn.grid(row=8, column=0, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)

		btn = Button(self.__fraTools, text="Radiobutton", fg="#0000FF")
		btn.grid(row=8, column=1, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)

		btn = Button(self.__fraTools, text="Text", fg="#0000FF")
		btn.grid(row=9, column=0, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)
		
		btn = Button(self.__fraTools, text="Scrollbar", fg="#0000FF")
		btn.grid(row=9, column=1, padx=2, pady=2, sticky=W+E)
		btn.bind("<Button-1>", self.new_widget_click)

		btn = Button(self.__fraTools, text="New Form", font="serif 8 bold", fg="#FF0000")
		btn.grid(row=10, column=0, padx=2, pady=2, sticky=W+E)
		btn.bind("<ButtonRelease-1>", self.newForm)

		btn = Button(self.__fraTools, text="Edit widget", font="serif 8 bold", fg="#FF0000")
		btn.grid(row=10, column=1, padx=2, pady=2, sticky=W+E)
		btn.bind("<ButtonRelease-1>", self.editWidget)
		self.__lblEditWidget = StringVar()
		btn["textvariable"] = self.__lblEditWidget
		self.__lblEditWidget.set("Edit widget")

		btn = Button(self.__fraTools, text="Load layout", font="serif 8 bold")
		btn.grid(row=11, column=0, padx=2, pady=2, sticky=W+E)
		btn.bind("<ButtonRelease-1>", self.loadLayout)

		btn = Button(self.__fraTools, text="Save layout", font="serif 8 bold")
		btn.grid(row=11, column=1, padx=2, pady=2, sticky=W+E)
		btn.bind("<ButtonRelease-1>", self.saveLayout)

		scrY.config(command=self.__listbox.yview)
		self.__listbox.grid(row=0, column=0, sticky=N+S+E+W, columnspan=2)

	def new_widget_click(self, event):

		widgetd = {}
		exec("widgetd.update({'widget' : " + event.widget["text"] + "(self._fraMain)" + "})")
		w = widgetd["widget"]
		w.name = "name = nessuno"

		try:
			w["relief"]="groove"
		except:
			pass

		try:
			w["height"]="10"
		except:
			pass

		try:
			w["border"]="2"
		except:
			pass

		try:
			w["width"]="10"
		except:
			pass

		try:
			w["height"]="10"
		except:
			pass

		if event.widget["text"] == "Frame":
			w["width"]="100"
			w["height"]="100"

		if event.widget["text"] == "Canvas":
			w["width"]="100"
			w["height"]="100"
			w["relief"]="ridge"
			w["border"]="2"

		if event.widget["text"] == "Label":
			w["width"]="10"
			w["height"]="0"
			w["text"]="Label"

		if event.widget["text"] == "Listbox":
			w["width"]="10"
			w["height"]="5"

		if event.widget["text"] == "Button":
			w["width"]="10"
			w["height"]="2"
			w["text"]="Button"
			w["relief"]="raised"

		if event.widget["text"] == "Checkbutton":
			w["width"]="10"
			w["height"]="2"
			w["text"]="Checkbutton"

		if event.widget["text"] == "Radiobutton":
			w["width"]="10"
			w["height"]="2"
			w["text"]="Radiobutton"

		w.place(x=10, y=10)
		w.bind("<Button-1>", self.mouse_click)
		w.bind("<B1-Motion>", self.mouse_move)
		w.bind("<ButtonRelease-1>", self.mouse_release)
		w.bind("<Motion>", self.mouse_resize)

	def mouse_click(self, event):

		if self.__lblEditWidget.get() == "Del. widget":
			event.widget.destroy()
			return

		self.widgetSelect = event.widget
		self.startX = event.x
		self.startY = event.y
		self.oldX = event.widget.winfo_x()
		self.oldY = event.widget.winfo_y()

		try:
			event.widget.lift()
		except:
			pass

		self.proprieta_fill(event.widget)

	def mouse_move(self, event):

		if self.startResize:
			event.widget.place(width=int(event.x / self.gridAlignX) * self.gridAlignX, \
								height=int(event.y / self.gridAlignY) * self.gridAlignY)
		else:
			self.oldX += (event.x - self.startX)
			self.oldY += (event.y - self.startY)
			self.oldX = int(self.oldX / self.gridAlignX) * self.gridAlignX
			self.oldY = int(self.oldY / self.gridAlignY) * self.gridAlignY
			event.widget.place(x=self.oldX, y=self.oldY)

	def mouse_resize(self, event):

		self.startResize = False
		if event.x > (event.widget.winfo_width() - 5):
			event.widget["cursor"] = "sizing"
			self.startResize = True
			return
		else:
			if self.__lblEditWidget.get() == "Del. widget":
				event.widget["cursor"] = "pirate"
			else:
				event.widget["cursor"] = "fleur"

		if event.y > (event.widget.winfo_height()) - 5:
			event.widget["cursor"] = "sizing"
			self.startResize = True
			return
		else:
			if self.__lblEditWidget.get() == "Del. widget":
				event.widget["cursor"] = "pirate"
			else:
				event.widget["cursor"] = "fleur"

	def mouse_release(self, event):

		if event.widget.master.master != event.widget.master:
			if event.widget.winfo_x() < 0 or \
				(event.widget.winfo_width() + event.widget.winfo_x()) > event.widget.master.winfo_width() or \
				event.widget.winfo_y() < 0 or \
				(event.widget.winfo_height() + event.widget.winfo_y()) > event.widget.master.winfo_height():

				self.firstPos = False
				if event.widget.master.master == self:
					self.cloneWidgets(event.widget, self._fraMain)
				else:
					self.cloneWidgets(event.widget, event.widget.master.master)
				event.widget.unbind("<Button-1>")
				event.widget.unbind("<B1-Motion>")
				event.widget.unbind("<ButtonRelease-1>")
				event.widget.unbind("<Motion>")
				event.widget.destroy()

				return

		wTarget = self.getWidgetColl(event.widget.master, event.widget)

		if wTarget != None and self.__fraTools != wTarget:
			self.firstPos = False
			self.cloneWidgets(event.widget, wTarget)
			event.widget.unbind("<Button-1>")
			event.widget.unbind("<B1-Motion>")
			event.widget.unbind("<ButtonRelease-1>")
			event.widget.unbind("<Motion>")
			event.widget.destroy()

	def cloneWidgets(self, wSource, wTarget):

		widgetd = {}
		if type(wSource).__name__ == "Canvas":
			exec("widgetd.update({'widget' : " + type(wSource).__name__ + "(wTarget, border=\"2\", relief=\"ridge\")" + "})")
		else:
			addttk = ""
			if type(wSource).__name__ == "Combobox":
				addttk = "tkinter.ttk."
			if type(wSource).__name__ == "Progressbar":
				addttk = "tkinter.ttk."
			exec("widgetd.update({'widget' : " + addttk + type(wSource).__name__ + "(wTarget)" + "})")
		wTarget = widgetd["widget"]		

		self.copyProp(wSource, wTarget)
		if type(wSource).__name__ == "Button":
			wTarget["relief"] = "raised"

		if not self.firstPos:
			self.firstPos = True
			wTarget.place(x=10, y=10, \
					width=wSource.place_info()["width"], \
					height=wSource.place_info()["height"])
		else:
			wTarget.place(x=wSource.place_info()["x"], \
					y=wSource.place_info()["y"], \
					width=wSource.place_info()["width"], \
					height=wSource.place_info()["height"])

		wTarget.place()
		wTarget.bind("<Button-1>", self.mouse_click)
		wTarget.bind("<B1-Motion>", self.mouse_move)
		wTarget.bind("<ButtonRelease-1>", self.mouse_release)
		wTarget.bind("<Motion>", self.mouse_resize)

		for wSourceChild in wSource.winfo_children():
			self.cloneWidgets(wSourceChild, wTarget)

	def copyProp(self, wSource, wTarget):

		wTarget.name = wSource.name
		for key in wSource.keys():
			try:
				wTarget[key] = wSource[key]
			except:
				pass

	def getWidgetColl(self, wParent, wCurrent):

		for w in wParent.winfo_children():
			if w != wCurrent and wCurrent.master != w:
				if  wCurrent.winfo_x() > (w.winfo_x() - wCurrent.winfo_width()) and \
					wCurrent.winfo_x() < (w.winfo_x() + w.winfo_width()) and \
					wCurrent.winfo_y() > (w.winfo_y() - wCurrent.winfo_height()) and \
					wCurrent.winfo_y() < (w.winfo_y() + w.winfo_height()):
					return w
			self.getWidgetColl(w, wCurrent)

	def saveproprieta_click(self, event):

		lbl = self.__lblProprieta["text"].strip()
		pro = self.__proprieta.get().strip()
		if lbl == "name":
			self.widgetSelect.name = "name = " + pro
			self.__proprieta.set(pro)
		else:
			self.widgetSelect[lbl] = pro
			self.__proprieta.set(pro)

	def proprieta_click(self, event):

		divprop = self.__listbox.get(self.__listbox.curselection()[0]).split("=")
		self.__lblProprieta["text"] = divprop[0].strip()
		self.__proprieta.set(divprop[1].strip())

	def proprieta_fill(self, widget):

		self.__listbox.delete(0, END)
		self.__listbox.insert(END, widget.name)
		for key in widget.keys():
			try:
				self.__listbox.insert(END, key + " = " + str(widget[key]) )
			except:
				pass

	def loadLayout(self, event):
		fname = askopenfilename(filetypes=(("Form layout files", "*.py"),
                                           ("All files", "*.*") ))
		if fname:
			try:
				del sys.modules[fname[fname.rfind("/")+1:][:-3]]				
			except:
				pass
			self.newFormRecur(self._fraMain)
			exec("import " + fname[fname.rfind("/")+1:][:-3] )			
			exec(fname[fname.rfind("/")+1:][:-3] + ".loadLayout(self)")
			
	def saveLayout(self, event):

		fname = asksaveasfilename(filetypes=(("Form layout files", "*.py"),
                                            ("All files", "*.*") ))
		if fname:

			numvar1 = 0

			sPy = "from tkinter import *\n"
			sPy += "import tkinter.ttk\n"
			sPy += "def loadLayout(self):\n"
			sPy += self.saveLayoutRecur(self._fraMain, numvar1)
			sPy +=  "\tpass"

			f = open(fname[fname.rfind("/")+1:],"w")
			f.write(sPy)
			f.close()

	def saveLayoutRecur(self, widget, numvar1):

		sPy = ""
		for w in widget.winfo_children():
			addttk = ""
			if type(w).__name__ == "Combobox":
				addttk = "tkinter.ttk."
			if type(w).__name__ == "Progressbar":
				addttk = "tkinter.ttk."

			addbor = ""
			if type(w).__name__ == "Frame":
				addbor = ", border=\"2\""

			if type(w).__name__ == "Canvas":
				addbor = ", border=\"2\", relief=\"ridge\""

			if type(w).__name__ == "Label":
				addbor = ", border=\"2\""

			if type(w).__name__ == "Listbox":
				addbor = ", border=\"2\""

			if type(w).__name__ == "Button":
				addbor = ", border=\"2\""

			if type(w).__name__ == "Checkbutton":
				addbor = ", border=\"2\""

			if type(w).__name__ == "Radiobutton":
				addbor = ", border=\"2\""

			if type(w).__name__ == "Text":
				addbor = ", border=\"2\""

			if type(w).__name__ == "Entry":
				addbor = ", border=\"2\""

			if numvar1 == 0:
				sPy += "\tnumvar" + str(numvar1+1) + "=" + addttk + type(w).__name__ + "(self._fraMain" + addbor + ")\n"
			else:
				sPy += "\tnumvar" + str(numvar1+1) + "=" + addttk + type(w).__name__ + "(numvar" + str(numvar1) + addbor + ")\n"
			for key in w.keys():
				try:
					w[key] = w[key]
					if key == "cursor":
						w[key] = "arrow"
					sPy += "\tnumvar" + str(numvar1+1) + "[\"" + key + "\"]=\"" + w[key] + "\"\n"
				except:
					pass
			sPy += "\tnumvar" + str(numvar1+1) + ".name=\"" + w.name + "\"\n"
			sPy += "\tnumvar" + str(numvar1+1) + ".place(" + \
					"x=" + str(w.winfo_x()) + "," + \
					"y=" + str(w.winfo_y()) + "," + \
					"width=" + str(w.winfo_width()) + "," + \
					"height=" + str(w.winfo_height()) + ")\n"
			sPy += "\tnumvar" + str(numvar1+1) + ".bind(\"<Button-1>\", self.mouse_click)\n"
			sPy += "\tnumvar" + str(numvar1+1) + ".bind(\"<B1-Motion>\", self.mouse_move)\n"
			sPy += "\tnumvar" + str(numvar1+1) + ".bind(\"<ButtonRelease-1>\", self.mouse_release)\n"
			sPy += "\tnumvar" + str(numvar1+1) + ".bind(\"<Motion>\", self.mouse_resize)\n"
			sPy += "\n"
			numvar1 += 1
			sPy += self.saveLayoutRecur(w, numvar1)
			numvar1 -= 1

		return sPy

	def newForm(self, event):
		self.newFormRecur(self._fraMain)

	def newFormRecur(self, widget):
		for w in widget.winfo_children():
			try:
				w.destroy()
				self.newFormRecur(w)
			except:
				pass

	def editWidget(self, event):
		if event.widget["text"] == "Edit widget":
			self.__lblEditWidget.set("Del. widget")
		else:
			self.__lblEditWidget.set("Edit widget")

root = frmMain(None)
root.wm_title("Tkinter form layout by Formisano Massimo - Italia - Roma - 333/6430347")
root.geometry("1250x640+0+0")
#root.state("zoomed")
mainloop()
