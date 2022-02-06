import maya.cmds as cmds
import pymel.core as pm
from functools import partial

uiFilePath = "D:/Work/Projects/PyCharm/Maya_RegEx.ui"


class UI:

    def __init__(self):
        self.Tools = Tools()

        self.mainWin = cmds.loadUI(uiFile=uiFilePath)

        cmds.button("but_rename", edit=True, command=self.Tools.tools_rename)
        cmds.button("but_find_del", edit=True, command=self.Tools.testprint)
        cmds.button("but_find_rep", edit=True, command=self.Tools.testprint)
        cmds.button("but_add_bef", edit=True, command=self.Tools.testprint)
        cmds.button("but_add_aft", edit=True, command=self.Tools.testprint)
        cmds.button("but_exit", edit=True, command=self.Tools.tools_close_window)

        cmds.showWindow(self.mainWin)

        # create dock and parent main window to it for UI integaration
        dock_layout = cmds.paneLayout(configuration='single', parent=self.mainWin)
        cmds.dockControl(allowedArea='all', area='right', floating=True, content=dock_layout, label='RegEx Renamer')
        cmds.control(self.mainWin, e=True, parent=dock_layout)


class Tools:

    def tools_rename(self, *args):
        # selection = pm.selected()[0:]
        selection = cmds.ls(selection=True)
        if len(selection) == 0:
            pm.confirmDialog(t='error', button="Continue", message="Select at least one Object!")
        else:
            print(selection)
            print("RENAMING")
            new_name = pm.textField('textFieldName', query=True, text=True)
            pm.rename(selection, new_name)


    def testprint(self, *args):
        print("teseeeett roter")

    def tools_close_window(self, *args):
        print('BORDEL')
        if cmds.window(self.mainWin, exists=True):
            cmds.deleteUI(self.mainWin, window=True)


UI()
