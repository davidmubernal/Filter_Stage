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
import kcomp
from filter_stage_fun import filter_stage_fun

__dir__ = os.path.dirname(__file__)

# Botón para hacer el FilterStage, tamaño predefinido
class _FilterStageCmd:
    
    def Activated(self):
        # what is done when the command is clicked
        
        filter_stage_fun(move_l = 60,
                         nut_hole = 4,
                         tens_stroke_Var = 15,
                         base_w = 20, 
                         wall_thick_Var = 3)  
                         
    def GetResources(self):
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
        return not FreeCAD.ActiveDocument is None

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

        # ---- row 0: Move distance
        # Label:
        self.move_l_Label = QtGui.QLabel("Move distance:")
        # Spin Box that takes doubles
        self.move_l_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.move_l_Value.setValue(60)
        # suffix to indicate the units
        self.move_l_Value.setSuffix(' mm')

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.move_l_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.move_l_Value,0,1,1,1)

        # ---- row 1: Base width
        # Label:
        self.base_w_Label = QtGui.QLabel("Base width:")  #5/10/15/20/30/40
        # Spin Box that takes doubles
        self.ComboBox_base_w = QtGui.QComboBox()
        # Diferents base
        self.TextBase_W = ["10mm","15mm","20mm","30mm","40mm"] ############### 5mm don't work well ################
        self.ComboBox_base_w.addItems(self.TextBase_W)
        self.ComboBox_base_w.setCurrentIndex(self.TextBase_W.index('20mm'))

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.base_w_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_base_w,1,1,1,1)
                
        # ---- row 2: Tensioner Stroke
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

        # ---- row 3: Wall thick
        # Label:
        self.wall_th_Label = QtGui.QLabel("Wall thick:")
        # Spin Box that takes doubles
        self.wall_th_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.wall_th_Value.setValue(3)
        # suffix to indicate the units
        self.wall_th_Value.setSuffix(' mm')

        # row 3, column 0, rowspan 1, colspan 1
        layout.addWidget(self.wall_th_Label,3,0,1,1)
        # row 3, column 1, rowspan 1, colspan 1
        layout.addWidget(self.wall_th_Value,3,1,1,1)

        # ---- row 4: Nut Type
        #Label:
        self.nut_hole_Label = QtGui.QLabel("Nut Type:")   

        # Combo Box that have multiple choice
        self.ComboBox_Nut_Hole = QtGui.QComboBox()
        # Type of Nut
        self.TextNutType = ["M3","M4","M5","M6"]
        self.ComboBox_Nut_Hole.addItems(self.TextNutType)
        # Indicate inicial value in ComboBox
        self.ComboBox_Nut_Hole.setCurrentIndex(self.TextNutType.index('M3'))

        # row 4, column 0, rowspan 1, colspan 1
        layout.addWidget(self.nut_hole_Label,4,0,1,1)
        # row 4, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_Nut_Hole,4,1,1,1)


    # Ok and Cancel buttons are created by default in FreeCAD Task Panels
    # What is done when we click on the ok button.

    def accept(self):
        self.selec_base = {0: 5, 1: 10, 2: 15, 3: 20, 4: 30, 5: 40}
        move_l = self.move_l_Value.value()
        nut_hole = 3 + self.ComboBox_Nut_Hole.currentIndex()  #Index star in 0, first value = 3
        tens_stroke = self.tens_stroke_Value.value()
        base_w = self.selec_base[self.ComboBox_base_w.currentIndex()]
        wall_thick = self.wall_th_Value.value()

        filter_stage_fun(move_l, nut_hole, tens_stroke, base_w, wall_thick)
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