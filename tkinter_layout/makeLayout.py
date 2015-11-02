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

from xml.dom.minidom import parse

class makeLayout:

	def __init__(self, sNameLayout):

		self.agg_menu = False

		document = parse(sNameLayout + ".xml")

		sFilePy = "from tkinter import *\n\n"
		sFilePy += "import tkinter.ttk\n\n"
		sFilePy += "class " + sNameLayout + ":\n"
		sFilePy += "\tdef __init__(self, parent):\n"
		sFilePy += "\n"
		sFilePy += "\t\tWidgets={}\n"
		sFilePy += "\n"
		sFilePy += self.makeInstance(document.childNodes, "")
		sFilePy += "\n"
		sFilePy += self.makeConfig(document.childNodes)
		sFilePy += "\n"
		sFilePy += self.makeGridPackPlace(document.childNodes)
		sFilePy += "\n"
		sFilePy += self.makeStringVar(document.childNodes)
		sFilePy += "\n"
		sFilePy += self.makeIntVar(document.childNodes)
		sFilePy += "\n"
		sFilePy += self.makeMenu(document.childNodes, "")
		sFilePy += "\n"
		sFilePy += "\t\tself.Widgets = Widgets"

		f = open(sNameLayout + ".py","w")
		f.write(sFilePy)
		f.close()

	def makeInstance(self, nodes, sParent):

		sFilePy = ""
		for node in nodes:
			if node.nodeType == node.ELEMENT_NODE:

				# preparo dizionario controlli
				sInstance = ""
				if node.tagName != "Root" and node.tagName != "Menuitem" and node.tagName != "Separator":
					sInstance = "\t\tWidgets.update({\"" + node.attributes["id"].value + "\" : " + node.tagName + "("

				# se e root metti parent della classe padre
				if sParent == "root":
					sInstance += "master=parent, "
				else:
					sInstance += "master=Widgets['" + sParent + "'], "

				# dizionario del controllo
				if node.tagName != "Root" and node.tagName != "Menuitem" and node.tagName != "Separator":
					sInstance = sInstance[:-2]
					sInstance += ")})\n"
					sFilePy += sInstance

				# chiamata ricorsiva
				sFilePy += self.makeInstance(node.childNodes, node.attributes["id"].value)

		return sFilePy

	def makeConfig(self, nodes):

		sFilePy = ""
		for node in nodes:
			if node.nodeType == node.ELEMENT_NODE:

				# preparo dizionario controlli
				sInstance = ""
				if node.tagName != "Root" and node.tagName != "Menu" and node.tagName != "Menuitem" and node.tagName != "Separator":

					sInstance = "\t\tWidgets[\"" + node.attributes["id"].value + "\"].config("

					# itero tutti gli attributi scartando id, grid, pack, place
					for i in node.attributes.keys():
						if i != "grid" and i != "pack" and i != "place" and i != "id" and i != "idintvar":
							sInstance += i + "=" + node.attributes[i].value + ", "

					# dizionario del controllo
					sInstance = sInstance[:-2]
					sInstance += ")\n"
					sFilePy += sInstance

				# chiamata ricorsiva
				sFilePy += self.makeConfig(node.childNodes)

		return sFilePy

	def makeGridPackPlace(self, nodes):

		sFilePy = ""
		for node in nodes:
			if node.nodeType == node.ELEMENT_NODE:

				# metodo grid
				sInstance = ""
				if node.attributes.get("grid"):
					sInstance = "\t\tWidgets[\"" + node.attributes["id"].value + "\"].grid(" + node.attributes["grid"].value + ")\n"

				# metodo pack
				if node.attributes.get("pack"):
					sInstance = "\t\tWidgets[\"" + node.attributes["id"].value + "\"].pack(" + node.attributes["pack"].value + ")\n"

				# metodo place
				if node.attributes.get("place"):
					sInstance = "\t\tWidgets[\"" + node.attributes["id"].value + "\"].place(" + node.attributes["place"].value + ")\n"

				# aggiungi dizionario controllo
				sFilePy += sInstance

				# chiamata ricorsiva
				sFilePy += self.makeGridPackPlace(node.childNodes)

		return sFilePy

	def makeStringVar(self, nodes):

		sFilePy = ""
		for node in nodes:
			if node.nodeType == node.ELEMENT_NODE:
				if node.tagName == "Entry":

					sInstance = ""

					# lego variabile stringa a controllo Entry
					sInstance += "\t\tWidgets.update({\"" + node.attributes["id"].value + "_StringVar\" : StringVar()})\n"

					# lego variabile stringa a controllo Entry
					sInstance += "\t\tWidgets[\"" + node.attributes["id"].value + "\"][\"text\"]=Widgets[\"" + node.attributes["id"].value + "_StringVar\"]\n"

					# aggiungi dizionario controllo
					sFilePy += sInstance

				# chiamata ricorsiva
				sFilePy += self.makeStringVar(node.childNodes)

		return sFilePy

	def makeIntVar(self, nodes):

		sFilePy = ""
		oneVar = False
		for node in nodes:
			if node.nodeType == node.ELEMENT_NODE:
				if node.tagName == "Radiobutton":

					sInstance = ""

					# lego variabile int a controllo Radiobutton
					if not oneVar:
						sInstance += "\t\tWidgets.update({\"" + node.attributes["idintvar"].value + "_IntVar\" : IntVar()})\n"
						oneVar = True

					# lego variabile int a controllo Radiobutton
					sInstance += "\t\tWidgets[\"" + node.attributes["id"].value + "\"][\"variable\"]=Widgets[\"" + node.attributes["idintvar"].value + "_IntVar\"]\n"

					# aggiungi dizionario controllo
					sFilePy += sInstance

				# chiamata ricorsiva
				sFilePy += self.makeIntVar(node.childNodes)

		return sFilePy

	def makeMenu(self, nodes, sParent):

		sFilePy = ""
		for node in nodes:
			if node.nodeType == node.ELEMENT_NODE:

				sInstance = ""
				if node.tagName == "Menu" and node.attributes["id"].value != "menumain":
					if not self.agg_menu:
						self.agg_menu = True
						sInstance += "\t\tparent.config(menu=Widgets[\"menumain\"])\n"

					sInstance += "\t\tWidgets[\"menumain\"].add_cascade(label='" + node.attributes["label"].value + "', menu=Widgets[\"" + node.attributes["id"].value + "\"])\n"
					sFilePy += sInstance

				if node.tagName == "Menuitem":
					sInstance = "\t\tWidgets[\"" + sParent + "\"].add_command(" + node.attributes["command"].value + ")\n"
					sFilePy += sInstance

				if node.tagName == "Separator":
					sInstance = "\t\tWidgets[\"" + sParent + "\"].add_separator()\n"
					sFilePy += sInstance

				# chiamata ricorsiva
				sFilePy += self.makeMenu(node.childNodes, node.attributes["id"].value)

		return sFilePy
