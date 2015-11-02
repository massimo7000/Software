from tkinter import *

import tkinter.ttk

class frmMainLayout:
	def __init__(self, parent):

		Widgets={}

		Widgets.update({"menumain" : Menu(master=parent)})
		Widgets.update({"file" : Menu(master=Widgets['menumain'])})
		Widgets.update({"help" : Menu(master=Widgets['menumain'])})
		Widgets.update({"frame1" : Frame(master=parent)})
		Widgets.update({"btnUno" : Button(master=Widgets['frame1'])})
		Widgets.update({"btnDue" : Button(master=Widgets['frame1'])})
		Widgets.update({"btnTre" : Button(master=Widgets['frame1'])})
		Widgets.update({"btnQuattro" : Button(master=Widgets['frame1'])})
		Widgets.update({"btnCinque" : Button(master=Widgets['frame1'])})
		Widgets.update({"frame2" : Frame(master=parent)})
		Widgets.update({"lblTest" : Label(master=Widgets['frame2'])})
		Widgets.update({"entTest" : Entry(master=Widgets['frame2'])})
		Widgets.update({"frame3" : Frame(master=parent)})
		Widgets.update({"scrollbar" : Scrollbar(master=Widgets['frame3'])})
		Widgets.update({"listbox" : Listbox(master=Widgets['frame3'])})
		Widgets.update({"frame4" : Frame(master=parent)})
		Widgets.update({"checkbutton" : Checkbutton(master=Widgets['frame4'])})
		Widgets.update({"radiobutton" : Radiobutton(master=Widgets['frame4'])})
		Widgets.update({"radiobutton1" : Radiobutton(master=Widgets['frame4'])})
		Widgets.update({"combobox" : ttk.Combobox(master=Widgets['frame4'])})
		Widgets.update({"progressbar" : ttk.Progressbar(master=parent)})
		Widgets.update({"canvas" : Canvas(master=parent)})

		Widgets["frame1"].config(pady=10, border=5, padx=10, relief=GROOVE)
		Widgets["btnUno"].config(command=parent.evento1, text='Button 1')
		Widgets["btnDue"].config(command=parent.evento2, text='Button 2')
		Widgets["btnTre"].config(command=parent.evento3, text='Button 3')
		Widgets["btnQuattro"].config(command=parent.evento4, text='Button 4')
		Widgets["btnCinque"].config(command=parent.evento5, text='Button 5')
		Widgets["frame2"].config(pady=10, border=5, padx=10, relief=GROOVE)
		Widgets["lblTest"].config(text='Test label')
		Widgets["entTest"].config(width=30)
		Widgets["frame3"].config(pady=10, border=5, padx=10, relief=GROOVE)
		Widgets["scrollbar"].config(orient=VERTICAL, command=Widgets['listbox'].yview)
		Widgets["listbox"].config(width=14, font=('courier', 8, 'bold'), yscrollcommand=Widgets['scrollbar'].set)
		Widgets["frame4"].config(pady=10, border=5, padx=10, relief=GROOVE)
		Widgets["checkbutton"].config(text='checkbutton label')
		Widgets["radiobutton"].config(value=1, text='radiobutton label1')
		Widgets["radiobutton1"].config(value=2, text='radiobutton label2')
		Widgets["combobox"].config(text='combobox')
		Widgets["progressbar"].config(value=100, maximum=200, length=400)
		Widgets["canvas"].config(height=200, bg='#FF0000', width=200)

		Widgets["frame1"].grid(row=0, column=0, pady=4, padx=4)
		Widgets["btnUno"].grid(row=0, column=0, pady=4, padx=4)
		Widgets["btnDue"].grid(row=1, column=0, pady=4, padx=4)
		Widgets["btnTre"].grid(row=2, column=0, pady=4, padx=4)
		Widgets["btnQuattro"].grid(row=3, column=0, pady=4, padx=4)
		Widgets["btnCinque"].grid(row=4, column=0, pady=4, padx=4)
		Widgets["frame2"].grid(row=1, column=0, pady=4, padx=4)
		Widgets["lblTest"].pack(side=LEFT)
		Widgets["entTest"].pack(side=LEFT)
		Widgets["frame3"].grid(row=2, column=0, pady=4, padx=4)
		Widgets["scrollbar"].pack(side=RIGHT, fill=Y)
		Widgets["listbox"].pack()
		Widgets["frame4"].grid(row=0, column=1, pady=4, padx=4)
		Widgets["checkbutton"].grid(row=0, column=0, pady=4, padx=4)
		Widgets["radiobutton"].grid(row=1, column=0, pady=4, padx=4)
		Widgets["radiobutton1"].grid(row=2, column=0, pady=4, padx=4)
		Widgets["combobox"].grid(row=3, column=0, pady=4, padx=4)
		Widgets["progressbar"].grid(row=1, column=1, pady=4, padx=4)
		Widgets["canvas"].grid(row=0, column=2, pady=4, padx=4)

		Widgets.update({"entTest_StringVar" : StringVar()})
		Widgets["entTest"]["text"]=Widgets["entTest_StringVar"]

		Widgets.update({"radiobutton_IntVar" : IntVar()})
		Widgets["radiobutton"]["variable"]=Widgets["radiobutton_IntVar"]
		Widgets["radiobutton1"]["variable"]=Widgets["radiobutton_IntVar"]

		parent.config(menu=Widgets["menumain"])
		Widgets["menumain"].add_cascade(label='File', menu=Widgets["file"])
		Widgets["file"].add_command(label='item1', command=parent.itemfile1)
		Widgets["file"].add_command(label='item2', command=parent.itemfile2)
		Widgets["file"].add_separator()
		Widgets["file"].add_command(label='item3', command=parent.itemfile3)
		Widgets["menumain"].add_cascade(label='Help', menu=Widgets["help"])
		Widgets["help"].add_command(label='item1', command=parent.itemhelp1)
		Widgets["help"].add_separator()
		Widgets["help"].add_command(label='item2', command=parent.itemhelp2)
		Widgets["help"].add_command(label='item3', command=parent.itemhelp3)

		self.Widgets = Widgets