# -*- coding: utf-8 -*-
# FreeCAD script for the commands of the filter stage workbench
# (c) 2018 David Muñoz Bernal

#***************************************************************************
#*   (c) David Muñoz Bernal                                                *
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   FreeCAD is distributed in the hope that it will be useful,            *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************/

import PySide
from PySide import QtCore, QtGui
import FreeCAD
import FreeCADGui
import Part
import os
from filter_stage_fun import filter_stage_fun

__dir__ = os.path.dirname(__file__)

"""                    ##########      TEST FUNCTION       ##########
def MakeBox(box_len = 1, box_wid = 1, box_hei = 1, boxname='box'):
    doc = FreeCAD.ActiveDocument
    box =  doc.addObject("Part::Box",boxname)
    box.Length = box_len
    box.Width  = box_wid
    box.Height = box_hei
 """                   ##########      TEST FUNCTION       ##########

# GUI command that links the Python script
class _FilterStageCmd:
    """Command to create a box"""

    
    def Activated(self):
        # what is done when the command is clicked
        
        filter_stage_fun()
                        #pulley_r = ,
                         #pulley_h = ,
                         #pulley_c = ,
                         #tens_stroke = 15,
                         #base_w = 
                         
    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Filter_Stage',
            'Filter Stage')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            '',
            'Creates a new filter stage')
        return {
            'Pixmap': __dir__ + '/icons/Filter_Stage_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

# Task Panel creation: the task panel has to have:
#   1. a widget called self.form
#   2. reject and accept methods (if needed)
class FilterStageSimpleTaskPanel:
    def __init__(self,widget):
        self.form = widget

    # Ok and Cancel buttons are created by default in FreeCAD Task Panels
    # What is done when we click on the ok button.
    def accept(self):
        filter_stage_fun()
        FreeCADGui.Control.closeDialog() #close the dialog

    # What is done when we click on the cancel button.
    # commented because this is the default behaviour
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

# GUI command that links the Python script
"""
class _FilterStageDialogCmd:
    Command to create a box with a very simple dialog
    

    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        baseWidget = QtGui.QWidget()
        panel = FilterStageSimpleTaskPanel(baseWidget)
        # having a panel with a widget in self.form and the accept and 
        # reject functions (if needed), we can open it:
        FreeCADGui.Control.showDialog(panel)

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'FilterStage_D',
            'Filter Stage Dialog')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'FilterStage_D',
            'Creates a box using a task panel dialog')
        return {
            'Pixmap': __dir__ + '/icons/Filter_Stage_Dialog_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None
"""

class FilterStageEdgePTaskPanel:                                    ##############     IMPORTANT       ##############
    def __init__(self,widget):
        self.form = widget
        # The layout will be a grid, since the form is an argument
        # we dont need this statement afterwards: self.form.setLayout(layout)
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Pulley Radio
        # Label:
        self.pulley_r_Label = QtGui.QLabel("Pulley Radio:")
        # Spin Box that takes doubles
        self.pulley_r_Value = QtGui.QDoubleSpinBox()
        # Default value                                             ##############     IMPORTANT       ##############
        self.pulley_r_Value.setValue(1)
        # suffix to indicate the units                              ##############     IMPORTANT       ##############
        self.pulley_r_Value.setSuffix(' mm')

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.pulley_r_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.pulley_r_Value,0,1,1,1)

        # ---- row 1: Pulley height
        # Label:
        self.pulley_h_Label = QtGui.QLabel("Pulley height:")
        # Spin Box that takes doubles
        self.pulley_h_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.pulley_h_Value.setValue(1)
        # suffix to indicate the units
        self.pulley_h_Value.setSuffix(' mm')

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.pulley_h_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.pulley_h_Value,1,1,1,1)

        # ---- row 2: Pulley center height
        # Label:
        self.pulley_c_Label = QtGui.QLabel("Pulley center height:")
        # Spin Box that takes doubles
        self.pulley_c_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.pulley_c_Value.setValue(1)
        # suffix to indicate the units
        self.pulley_c_Value.setSuffix(' mm')

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.pulley_c_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.pulley_c_Value,2,1,1,1)

        # ---- row 3: Tensioner stroke
        # Label:
        self.tens_stroke_Label = QtGui.QLabel("Tensioner stroke:")
        # Spin Box that takes doubles
        self.tens_stroke_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.tens_stroke_Value.setValue(1)
        # suffix to indicate the units
        self.tens_stroke_Value.setSuffix(' mm')

        # row 3, column 0, rowspan 1, colspan 1
        layout.addWidget(self.tens_stroke_Label,3,0,1,1)
        # row 3, column 1, rowspan 1, colspan 1
        layout.addWidget(self.tens_stroke_Value,3,1,1,1)
        
        # ---- row 4: Base width
        # Label:
        self.base_w_Label = QtGui.QLabel("Base width:")
        # Spin Box that takes doubles
        self.base_w_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.base_w_Value.setValue(1)
        # suffix to indicate the units
        self.base_w_Value.setSuffix(' mm')

        # row 4, column 0, rowspan 1, colspan 1
        layout.addWidget(self.base_w_Label,4,0,1,1)
        # row 4, column 1, rowspan 1, colspan 1
        layout.addWidget(self.base_w_Value,4,1,1,1)

    # Ok and Cancel buttons are created by default in FreeCAD Task Panels
    # What is done when we click on the ok button.
    def accept(self):
        pulley_r = self.pulley_r_Value.value()
        pulley_h = self.pulley_h_Value.value()
        pulley_c = self.pulley_c_Value.value()
        tens_stroke = self.tens_stroke_Value.value()
        base_w = self.base_w_Value.value()
        filter_stage_fun(pulley_r, pulley_h, pulley_c, tens_stroke, base_w)
        FreeCADGui.Control.closeDialog() #close the dialog

    # What is done when we click on the cancel button.
    # commented because this is the default behaviour
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

# GUI command that links the Python script
class _FilterStageEdgePCmd:
    """Command to create a box with a dialog where you can set the Edge length
    """

    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        baseWidget = QtGui.QWidget()
        panel = FilterStageEdgePTaskPanel(baseWidget)
        # having a panel with a widget in self.form and the accept and 
        # reject functions (if needed), we can open it:
        FreeCADGui.Control.showDialog(panel)

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Filter_Stage_PBox',
            'Edge Parameter Filter Stage Dialog')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Filter_Stage_PBox',
            'Creates a box using a dialog to choose the edge length')
        return {
            'Pixmap': __dir__ + '/icons/Filter_Stage_Edge_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None


FreeCADGui.addCommand('Filter_Stage_filter_stage', _FilterStageCmd())
#FreeCADGui.addCommand('Filter_Stage_Dialog', _FilterStageDialogCmd())
FreeCADGui.addCommand('Filter_Stage_EdgeP', _FilterStageEdgePCmd())