from tkinter import *
import tkinter.ttk
def loadLayout(self):
	numvar1=Frame(self._fraMain, border="2")
	numvar1["relief"]="groove"
	numvar1["background"]="SystemButtonFace"
	numvar1["bg"]="SystemButtonFace"
	numvar1["cursor"]="arrow"
	numvar1["highlightbackground"]="SystemButtonFace"
	numvar1["highlightcolor"]="SystemWindowFrame"
	numvar1["takefocus"]="0"
	numvar1.name="name = nessuno"
	numvar1.place(x=154,y=209,width=175,height=235)
	numvar1.bind("<Button-1>", self.mouse_click)
	numvar1.bind("<B1-Motion>", self.mouse_move)
	numvar1.bind("<ButtonRelease-1>", self.mouse_release)
	numvar1.bind("<Motion>", self.mouse_resize)

	numvar2=Listbox(numvar1, border="2")
	numvar2["activestyle"]="underline"
	numvar2["background"]="SystemWindow"
	numvar2["bg"]="SystemWindow"
	numvar2["cursor"]="arrow"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemButtonText"
	numvar2["font"]="TkDefaultFont"
	numvar2["foreground"]="SystemButtonText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["relief"]="groove"
	numvar2["selectbackground"]="SystemHighlight"
	numvar2["selectforeground"]="SystemHighlightText"
	numvar2["selectmode"]="browse"
	numvar2["state"]="normal"
	numvar2["takefocus"]=""
	numvar2["xscrollcommand"]=""
	numvar2["yscrollcommand"]=""
	numvar2["listvariable"]=""
	numvar2.name="name = listbox"
	numvar2.place(x=16,y=16,width=130,height=210)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Scrollbar(numvar1)
	numvar2.name="name = scrollbar"
	numvar2.place(x=151,y=16,width=15,height=210)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar1=Frame(self._fraMain, border="2")
	numvar1["relief"]="groove"
	numvar1["background"]="SystemButtonFace"
	numvar1["bg"]="SystemButtonFace"
	numvar1["cursor"]="arrow"
	numvar1["highlightbackground"]="SystemButtonFace"
	numvar1["highlightcolor"]="SystemWindowFrame"
	numvar1["takefocus"]="0"
	numvar1.name="name = nessuno"
	numvar1.place(x=342,y=207,width=385,height=250)
	numvar1.bind("<Button-1>", self.mouse_click)
	numvar1.bind("<B1-Motion>", self.mouse_move)
	numvar1.bind("<ButtonRelease-1>", self.mouse_release)
	numvar1.bind("<Motion>", self.mouse_resize)

	numvar2=Label(numvar1, border="2")
	numvar2["activebackground"]="SystemButtonFace"
	numvar2["activeforeground"]="SystemButtonText"
	numvar2["anchor"]="center"
	numvar2["background"]="SystemButtonFace"
	numvar2["bg"]="SystemButtonFace"
	numvar2["bitmap"]=""
	numvar2["compound"]="none"
	numvar2["cursor"]="arrow"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemButtonText"
	numvar2["font"]="TkDefaultFont"
	numvar2["foreground"]="SystemButtonText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["image"]=""
	numvar2["justify"]="center"
	numvar2["relief"]="groove"
	numvar2["state"]="normal"
	numvar2["takefocus"]="0"
	numvar2["text"]="Telefono"
	numvar2["textvariable"]=""
	numvar2.name="name = nessuno"
	numvar2.place(x=22,y=147,width=76,height=21)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Label(numvar1, border="2")
	numvar2["activebackground"]="SystemButtonFace"
	numvar2["activeforeground"]="SystemButtonText"
	numvar2["anchor"]="center"
	numvar2["background"]="SystemButtonFace"
	numvar2["bg"]="SystemButtonFace"
	numvar2["bitmap"]=""
	numvar2["compound"]="none"
	numvar2["cursor"]="arrow"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemButtonText"
	numvar2["font"]="TkDefaultFont"
	numvar2["foreground"]="SystemButtonText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["image"]=""
	numvar2["justify"]="center"
	numvar2["relief"]="groove"
	numvar2["state"]="normal"
	numvar2["takefocus"]="0"
	numvar2["text"]="Citta'"
	numvar2["textvariable"]=""
	numvar2.name="name = nessuno"
	numvar2.place(x=22,y=122,width=76,height=21)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Label(numvar1, border="2")
	numvar2["activebackground"]="SystemButtonFace"
	numvar2["activeforeground"]="SystemButtonText"
	numvar2["anchor"]="center"
	numvar2["background"]="SystemButtonFace"
	numvar2["bg"]="SystemButtonFace"
	numvar2["bitmap"]=""
	numvar2["compound"]="none"
	numvar2["cursor"]="arrow"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemButtonText"
	numvar2["font"]="TkDefaultFont"
	numvar2["foreground"]="SystemButtonText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["image"]=""
	numvar2["justify"]="center"
	numvar2["relief"]="groove"
	numvar2["state"]="normal"
	numvar2["takefocus"]="0"
	numvar2["text"]="Indirizzo"
	numvar2["textvariable"]=""
	numvar2.name="name = nessuno"
	numvar2.place(x=22,y=97,width=76,height=21)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Label(numvar1, border="2")
	numvar2["activebackground"]="SystemButtonFace"
	numvar2["activeforeground"]="SystemButtonText"
	numvar2["anchor"]="center"
	numvar2["background"]="SystemButtonFace"
	numvar2["bg"]="SystemButtonFace"
	numvar2["bitmap"]=""
	numvar2["compound"]="none"
	numvar2["cursor"]="arrow"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemButtonText"
	numvar2["font"]="TkDefaultFont"
	numvar2["foreground"]="SystemButtonText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["image"]=""
	numvar2["justify"]="center"
	numvar2["relief"]="groove"
	numvar2["state"]="normal"
	numvar2["takefocus"]="0"
	numvar2["text"]="Cognome"
	numvar2["textvariable"]=""
	numvar2.name="name = nessuno"
	numvar2.place(x=22,y=72,width=76,height=21)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Label(numvar1, border="2")
	numvar2["activebackground"]="SystemButtonFace"
	numvar2["activeforeground"]="SystemButtonText"
	numvar2["anchor"]="center"
	numvar2["background"]="SystemButtonFace"
	numvar2["bg"]="SystemButtonFace"
	numvar2["bitmap"]=""
	numvar2["compound"]="none"
	numvar2["cursor"]="arrow"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemButtonText"
	numvar2["font"]="TkDefaultFont"
	numvar2["foreground"]="SystemButtonText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["image"]=""
	numvar2["justify"]="center"
	numvar2["relief"]="groove"
	numvar2["state"]="normal"
	numvar2["takefocus"]="0"
	numvar2["text"]="Nome"
	numvar2["textvariable"]=""
	numvar2.name="name = nessuno"
	numvar2.place(x=22,y=47,width=76,height=21)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Label(numvar1, border="2")
	numvar2["activebackground"]="SystemButtonFace"
	numvar2["activeforeground"]="SystemButtonText"
	numvar2["anchor"]="center"
	numvar2["background"]="SystemButtonFace"
	numvar2["bg"]="SystemButtonFace"
	numvar2["bitmap"]=""
	numvar2["compound"]="none"
	numvar2["cursor"]="arrow"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemButtonText"
	numvar2["font"]="verdana 10 bold"
	numvar2["foreground"]="SystemButtonText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["image"]=""
	numvar2["justify"]="center"
	numvar2["relief"]="groove"
	numvar2["state"]="normal"
	numvar2["takefocus"]="0"
	numvar2["text"]="Anagrafica clienti"
	numvar2["textvariable"]=""
	numvar2.name="name = nessuno"
	numvar2.place(x=22,y=17,width=350,height=25)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Entry(numvar1, border="2")
	numvar2["background"]="SystemWindow"
	numvar2["bg"]="SystemWindow"
	numvar2["cursor"]="arrow"
	numvar2["disabledbackground"]="SystemButtonFace"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemWindowText"
	numvar2["font"]="TkTextFont"
	numvar2["foreground"]="SystemWindowText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["insertbackground"]="SystemWindowText"
	numvar2["invalidcommand"]=""
	numvar2["invcmd"]=""
	numvar2["justify"]="left"
	numvar2["readonlybackground"]="SystemButtonFace"
	numvar2["relief"]="groove"
	numvar2["selectbackground"]="SystemHighlight"
	numvar2["selectforeground"]="SystemHighlightText"
	numvar2["show"]=""
	numvar2["state"]="normal"
	numvar2["takefocus"]=""
	numvar2["textvariable"]=""
	numvar2["validate"]="none"
	numvar2["validatecommand"]=""
	numvar2["vcmd"]=""
	numvar2["xscrollcommand"]=""
	numvar2.name="name = nome"
	numvar2.place(x=102,y=47,width=270,height=20)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Entry(numvar1, border="2")
	numvar2["background"]="SystemWindow"
	numvar2["bg"]="SystemWindow"
	numvar2["cursor"]="arrow"
	numvar2["disabledbackground"]="SystemButtonFace"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemWindowText"
	numvar2["font"]="TkTextFont"
	numvar2["foreground"]="SystemWindowText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["insertbackground"]="SystemWindowText"
	numvar2["invalidcommand"]=""
	numvar2["invcmd"]=""
	numvar2["justify"]="left"
	numvar2["readonlybackground"]="SystemButtonFace"
	numvar2["relief"]="groove"
	numvar2["selectbackground"]="SystemHighlight"
	numvar2["selectforeground"]="SystemHighlightText"
	numvar2["show"]=""
	numvar2["state"]="normal"
	numvar2["takefocus"]=""
	numvar2["textvariable"]=""
	numvar2["validate"]="none"
	numvar2["validatecommand"]=""
	numvar2["vcmd"]=""
	numvar2["xscrollcommand"]=""
	numvar2.name="name = cognome"
	numvar2.place(x=102,y=72,width=270,height=20)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Entry(numvar1, border="2")
	numvar2["background"]="SystemWindow"
	numvar2["bg"]="SystemWindow"
	numvar2["cursor"]="arrow"
	numvar2["disabledbackground"]="SystemButtonFace"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemWindowText"
	numvar2["font"]="TkTextFont"
	numvar2["foreground"]="SystemWindowText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["insertbackground"]="SystemWindowText"
	numvar2["invalidcommand"]=""
	numvar2["invcmd"]=""
	numvar2["justify"]="left"
	numvar2["readonlybackground"]="SystemButtonFace"
	numvar2["relief"]="groove"
	numvar2["selectbackground"]="SystemHighlight"
	numvar2["selectforeground"]="SystemHighlightText"
	numvar2["show"]=""
	numvar2["state"]="normal"
	numvar2["takefocus"]=""
	numvar2["textvariable"]=""
	numvar2["validate"]="none"
	numvar2["validatecommand"]=""
	numvar2["vcmd"]=""
	numvar2["xscrollcommand"]=""
	numvar2.name="name = indirizzo"
	numvar2.place(x=102,y=97,width=270,height=20)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Entry(numvar1, border="2")
	numvar2["background"]="SystemWindow"
	numvar2["bg"]="SystemWindow"
	numvar2["cursor"]="arrow"
	numvar2["disabledbackground"]="SystemButtonFace"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemWindowText"
	numvar2["font"]="TkTextFont"
	numvar2["foreground"]="SystemWindowText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["insertbackground"]="SystemWindowText"
	numvar2["invalidcommand"]=""
	numvar2["invcmd"]=""
	numvar2["justify"]="left"
	numvar2["readonlybackground"]="SystemButtonFace"
	numvar2["relief"]="groove"
	numvar2["selectbackground"]="SystemHighlight"
	numvar2["selectforeground"]="SystemHighlightText"
	numvar2["show"]=""
	numvar2["state"]="normal"
	numvar2["takefocus"]=""
	numvar2["textvariable"]=""
	numvar2["validate"]="none"
	numvar2["validatecommand"]=""
	numvar2["vcmd"]=""
	numvar2["xscrollcommand"]=""
	numvar2.name="name = citta"
	numvar2.place(x=102,y=122,width=270,height=20)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Entry(numvar1, border="2")
	numvar2["background"]="SystemWindow"
	numvar2["bg"]="SystemWindow"
	numvar2["cursor"]="arrow"
	numvar2["disabledbackground"]="SystemButtonFace"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemWindowText"
	numvar2["font"]="TkTextFont"
	numvar2["foreground"]="SystemWindowText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["insertbackground"]="SystemWindowText"
	numvar2["invalidcommand"]=""
	numvar2["invcmd"]=""
	numvar2["justify"]="left"
	numvar2["readonlybackground"]="SystemButtonFace"
	numvar2["relief"]="groove"
	numvar2["selectbackground"]="SystemHighlight"
	numvar2["selectforeground"]="SystemHighlightText"
	numvar2["show"]=""
	numvar2["state"]="normal"
	numvar2["takefocus"]=""
	numvar2["textvariable"]=""
	numvar2["validate"]="none"
	numvar2["validatecommand"]=""
	numvar2["vcmd"]=""
	numvar2["xscrollcommand"]=""
	numvar2.name="name = telefono"
	numvar2.place(x=102,y=147,width=270,height=20)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Button(numvar1, border="2")
	numvar2["activebackground"]="SystemButtonFace"
	numvar2["activeforeground"]="SystemButtonText"
	numvar2["anchor"]="center"
	numvar2["background"]="SystemButtonFace"
	numvar2["bg"]="SystemButtonFace"
	numvar2["bitmap"]=""
	numvar2["command"]=""
	numvar2["compound"]="none"
	numvar2["cursor"]="arrow"
	numvar2["default"]="disabled"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemButtonText"
	numvar2["font"]="TkDefaultFont"
	numvar2["foreground"]="SystemButtonText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["image"]=""
	numvar2["justify"]="center"
	numvar2["overrelief"]=""
	numvar2["relief"]="raised"
	numvar2["state"]="normal"
	numvar2["takefocus"]=""
	numvar2["text"]="scrivi dati"
	numvar2["textvariable"]=""
	numvar2.name="name = scrividati"
	numvar2.place(x=97,y=207,width=70,height=30)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	numvar2=Checkbutton(numvar1, border="2")
	numvar2["activebackground"]="SystemButtonFace"
	numvar2["activeforeground"]="SystemWindowText"
	numvar2["anchor"]="center"
	numvar2["background"]="SystemButtonFace"
	numvar2["bg"]="SystemButtonFace"
	numvar2["bitmap"]=""
	numvar2["command"]=""
	numvar2["compound"]="none"
	numvar2["cursor"]="arrow"
	numvar2["disabledforeground"]="SystemDisabledText"
	numvar2["fg"]="SystemWindowText"
	numvar2["font"]="TkDefaultFont"
	numvar2["foreground"]="SystemWindowText"
	numvar2["highlightbackground"]="SystemButtonFace"
	numvar2["highlightcolor"]="SystemWindowFrame"
	numvar2["image"]=""
	numvar2["justify"]="center"
	numvar2["offrelief"]="raised"
	numvar2["offvalue"]="0"
	numvar2["onvalue"]="1"
	numvar2["overrelief"]=""
	numvar2["relief"]="groove"
	numvar2["selectcolor"]="SystemWindow"
	numvar2["selectimage"]=""
	numvar2["state"]="normal"
	numvar2["takefocus"]=""
	numvar2["text"]="Prova checkbutton"
	numvar2["textvariable"]=""
	numvar2["tristateimage"]=""
	numvar2["tristatevalue"]=""
	numvar2.name="name = chkTest"
	numvar2.place(x=102,y=177,width=185,height=25)
	numvar2.bind("<Button-1>", self.mouse_click)
	numvar2.bind("<B1-Motion>", self.mouse_move)
	numvar2.bind("<ButtonRelease-1>", self.mouse_release)
	numvar2.bind("<Motion>", self.mouse_resize)

	pass