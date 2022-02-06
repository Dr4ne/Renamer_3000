import maya.cmds as cmds
import pymel.core as pm
import maya.OpenMayaUI as mui
import shiboken2

from PySide2 import QtGui
from PySide2 import QtWidgets
from functools import partial


class Tools:
    def tools_rename(self):
        selection = cmds.ls(selection=True)
        if len(selection) == 0:
            pm.confirmDialog(t='error', button="Continue", message="No selection       ")
        else:
            text_input = lineEdit01.text()
            if len(text_input) == 0:
                pm.confirmDialog(t='error', button="Continue", message="No text input       ")
            else:
                for sel_obj in selection:
                    pm.rename(sel_obj, lineEdit01.text())


    def find_del(self):
        selection = cmds.ls(selection=True)
        if len(selection) == 0:
            pm.confirmDialog(t='error', button="Continue", message="No selection       ")
        else:
            text_find = lineEdit02.text()
            if len(text_find) == 0:
                pm.confirmDialog(t='error', button="Continue", message="No text input       ")
            else:
                if text_find not in selection[0]:
                    pm.confirmDialog(t='error', button="Continue", message="Text input NOT found       ")
                else:
                    for sel_obj in selection:
                        new_name = sel_obj.replace(str(text_find), "")
                        pm.rename(sel_obj, new_name)

    def find_rep(self, *args):
        selection = cmds.ls(selection=True)
        if len(selection) == 0:
            pm.confirmDialog(t='error', button="Continue", message="No selection       ")
        else:
            text_input = lineEdit01.text()
            text_find = lineEdit02.text()
            if len(text_find) == 0:
                pm.confirmDialog(t='error', button="Continue", message="No text input       ")
            else:
                if text_find not in selection[0]:
                    pm.confirmDialog(t='error', button="Continue", message="Text input NOT found       ")
                else:
                    for sel_obj in selection:
                        new_name = sel_obj.replace(str(text_find), str(text_input))
                        pm.rename(sel_obj, new_name)

    def add_left(self, *args):
        selection = cmds.ls(selection=True)
        if len(selection) == 0:
            pm.confirmDialog(t='error', button="Continue", message="No selection       ")
        else:
            text_input = lineEdit01.text()
            text_find = lineEdit02.text()
            if len(text_find) == 0:
                pm.confirmDialog(t='error', button="Continue", message="No text input       ")
            else:
                for sel_obj in selection:
                    new_name = str(text_input) + str(sel_obj)
                    pm.rename(sel_obj, new_name)


    def add_right(self, *args):
        selection = cmds.ls(selection=True)
        if len(selection) == 0:
            pm.confirmDialog(t='error', button="Continue", message="No selection       ")
        else:
            text_input = lineEdit01.text()
            text_find = lineEdit02.text()
            if len(text_find) == 0:
                pm.confirmDialog(t='error', button="Continue", message="No text input       ")
            else:
                for sel_obj in selection:
                    new_name = str(sel_obj) + str(text_input)
                    pm.rename(sel_obj, new_name)


def get_maya_window():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(pointer), QtWidgets.QWidget)


tools = Tools()

# def className_U1():
windowName = 'Renamer 9000'

# check for existing window
if cmds.window('Renamer 9000', exists=True):
    cmds.deleteUI('Renamer 9000', wnd=True)

# create a window
parent = get_maya_window()
window = QtWidgets.QMainWindow(parent)
window.setObjectName(windowName)
window.setWindowTitle(windowName)

# create fonts
font = QtGui.QFont("Segoe UI Semibold")
font.setPointSize(10)
font.setBold(False)
font2 = QtGui.QFont("Segoe UI Semibold")
font2.setPointSize(13)
font2.setBold(True)
font3 = QtGui.QFont("Segoe UI Semibold")
font3.setPointSize(8)
font3.setBold(False)

# create a widget
widget = QtWidgets.QWidget()
window.setCentralWidget(widget)

# create a layout
layout = QtWidgets.QVBoxLayout(widget)  # horizontal QtGui.QHBoxLayout()

pixmap = QtGui.QPixmap('G:/Projects/02 - Misc/PyCharm/9000.jpg')
label = QtWidgets.QLabel()
label.setPixmap(pixmap)
layout.addWidget(label)

# create text field 01
lineEdit01 = QtWidgets.QLineEdit("New name")
lineEdit01.setFont(font3)
layout.addWidget(lineEdit01)

phoneLabel = QtWidgets.QLabel("&Phone:")
phoneLabel.setBuddy(lineEdit01)

buttons_min_size_x = 235
buttons_min_size_y = 30
buttons_max_size_x = 4000
buttons_max_size_y = 300

button = QtWidgets.QPushButton("Rename")
layout.addWidget(button)
button.setFont(font)
button.setMinimumSize(buttons_min_size_x, buttons_min_size_y)
button.setMaximumSize(buttons_max_size_x, buttons_max_size_y)
button.setStyleSheet("background-color: rgb(128,128,128); color: rgb(255,255,255)")
button.clicked.connect(partial(tools.tools_rename))

button = QtWidgets.QPushButton("Add <---")
layout.addWidget(button)
button.setFont(font)
button.setMinimumSize(buttons_min_size_x, buttons_min_size_y)
button.setMaximumSize(buttons_max_size_x, buttons_max_size_y)
button.setStyleSheet("background-color: rgb(128,128,128); color: rgb(255,255,255)")
button.clicked.connect(partial(tools.add_left, 'Adnan'))

button = QtWidgets.QPushButton("Add --->")
layout.addWidget(button)
button.setFont(font)
button.setMinimumSize(buttons_min_size_x, buttons_min_size_y)
button.setMaximumSize(buttons_max_size_x, buttons_max_size_y)
button.setStyleSheet("background-color: rgb(128,128,128); color: rgb(255,255,255)")
button.clicked.connect(partial(tools.add_right, 'Adnan'))

# create text field 02
lineEdit02 = QtWidgets.QLineEdit("Find")
lineEdit02.setFont(font3)
layout.addWidget(lineEdit02)

button = QtWidgets.QPushButton("Find and Delete")
layout.addWidget(button)
button.setFont(font)
button.setMinimumSize(buttons_min_size_x, buttons_min_size_y)
button.setMaximumSize(buttons_max_size_x, buttons_max_size_y)
button.setStyleSheet("background-color: rgb(128,128,128); color: rgb(255,255,255)")
button.clicked.connect(partial(tools.find_del))

button = QtWidgets.QPushButton("Find and Replace")
layout.addWidget(button)
button.setFont(font)
button.setMinimumSize(buttons_min_size_x, buttons_min_size_y)
button.setMaximumSize(buttons_max_size_x, buttons_max_size_y)
button.setStyleSheet("background-color: rgb(128,128,128); color: rgb(255,255,255)")
button.clicked.connect(partial(tools.find_rep, 'Adnan'))

closeButton = QtWidgets.QPushButton('Close')
layout.addWidget(closeButton)
closeButton.setFont(font2)
closeButton.clicked.connect(window.close)

window.show()
