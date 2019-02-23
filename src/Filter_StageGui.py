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


# GUI command that links the Python script
class _FilterStageCmd:
    
    def Activated(self):
        # what is done when the command is clicked
        
        filter_stage_fun(belt_h = 15,
                         nut_hole = 4,
                         tens_stroke_Var = 15,
                         base_w = 20,    #Don't do anythink
                         wall_thick_Var = 3) 
                         
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

class FilterStageModTaskPanel:                                    
    def __init__(self,widget):
        self.form = widget
        # The layout will be a grid, since the form is an argument
        # we dont need this statement afterwards: self.form.setLayout(layout)
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Pulley Radio
        # Label:
        self.nut_hole_Label = QtGui.QLabel("Nut Type:")     #Métrica de la tuerca
        # Spin Box that takes doubles
        self.nut_hole_Value = QtGui.QDoubleSpinBox()
        # Default value                                             
        self.nut_hole_Value.setValue(4)
        # suffix to indicate the units                              
        self.nut_hole_Value.setSuffix(' mm')

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.nut_hole_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.nut_hole_Value,0,1,1,1)

        # ---- row 1: Pulley height
        # Label:
        self.belt_h_Label = QtGui.QLabel("Belt height:")
        # Spin Box that takes doubles
        self.belt_h_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.belt_h_Value.setValue(15)
        # suffix to indicate the units
        self.belt_h_Value.setSuffix(' mm')

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.belt_h_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.belt_h_Value,1,1,1,1)

        # ---- row 2: Tensioner stroke
        # Label:
        self.tens_stroke_Label = QtGui.QLabel("Tensioner stroke:")
        # Spin Box that takes doubles
        self.tens_stroke_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.tens_stroke_Value.setValue(15)
        # suffix to indicate the units
        self.tens_stroke_Value.setSuffix(' mm')

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.tens_stroke_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.tens_stroke_Value,2,1,1,1)
        
        # ---- row 3: Pulley center height
        # Label:
        self.base_w_Label = QtGui.QLabel("Base width:")
        # Spin Box that takes doubles
        self.base_w_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.base_w_Value.setValue(20)
        # suffix to indicate the units
        self.base_w_Value.setSuffix(' mm')

        # row 3, column 0, rowspan 1, colspan 1
        layout.addWidget(self.base_w_Label,3,0,1,1)
        # row 3, column 1, rowspan 1, colspan 1
        layout.addWidget(self.base_w_Value,3,1,1,1)

        
        # ---- row 4: Base width
        # Label:
        self.wall_th_Label = QtGui.QLabel("Wall thick:")
        # Spin Box that takes doubles
        self.wall_th_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.wall_th_Value.setValue(3)
        # suffix to indicate the units
        self.wall_th_Value.setSuffix(' mm')

        # row 4, column 0, rowspan 1, colspan 1
        layout.addWidget(self.wall_th_Label,4,0,1,1)
        # row 4, column 1, rowspan 1, colspan 1
        layout.addWidget(self.wall_th_Value,4,1,1,1)

    # Ok and Cancel buttons are created by default in FreeCAD Task Panels
    # What is done when we click on the ok button.
    def accept(self):
        belt_h = self.belt_h_Value.value()
        nut_hole = self.nut_hole_Value.value()
        tens_stroke = self.tens_stroke_Value.value()
        base_w = self.base_w_Value.value()
        wall_thick = self.wall_th_Value.value()

        filter_stage_fun(belt_h, nut_hole, tens_stroke, base_w, wall_thick)
            #pulley_h => belt_pos_h
            #nut_hole => bolttens_mtr
            #tens_stroke => tens_stroke_Var
            #base_w => aluprof_w
            #wall_thick => wall_thick_Var
        FreeCADGui.Control.closeDialog() #close the dialog

    # What is done when we click on the cancel button.
    # commented because this is the default behaviour
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

# GUI command that links the Python script
class _FilterStageModCmd:

    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        baseWidget = QtGui.QWidget()
        panel = FilterStageModTaskPanel(baseWidget)
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
            'Creates a Filter Stage with set parametres')
        return {
            'Pixmap': __dir__ + '/icons/Filter_Stage_Mod_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None


FreeCADGui.addCommand('Filter_Stage_filter_stage', _FilterStageCmd())
FreeCADGui.addCommand('Filter_Stage_Mod', _FilterStageModCmd())