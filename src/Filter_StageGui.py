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
from filter_stage_fun import filter_stage_fun, filter_holder_fun, tensioner_fun, motor_holder_fun
from print_export_fun import print_export
__dir__ = os.path.dirname(__file__)

# Botón para hacer el FilterStage, tamaño predefinido
#class _FilterStageCmd:
#    
#    def Activated(self):
#        # what is done when the command is clicked
        
#        filter_stage_fun(move_l = 60,
#                         nut_hole = 4,
#                         tens_stroke_Var = 15,
#                         base_w = 20, 
#                         wall_thick_Var = 3) 
                         
#    def GetResources(self):
#        MenuText = QtCore.QT_TRANSLATE_NOOP(
#            'Filter_Stage',
#            'Filter Stage')
#        ToolTip = QtCore.QT_TRANSLATE_NOOP(
#            '',
#            'Creates a new filter stage')
#        return {
#            'Pixmap': __dir__ + '/icons/Filter_Stage_cmd.svg',
#            'MenuText': MenuText,
#            'ToolTip': ToolTip}
#    def IsActive(self):
#        return not FreeCAD.ActiveDocument is None

class FilterStageTaskPanel:                                    
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
        self.base_w_Label = QtGui.QLabel("Base width:")  #10/15/20/30/40
        # Spin Box that takes doubles
        self.ComboBox_base_w = QtGui.QComboBox()
        # Diferents base
        self.TextBase_W = ["10mm","15mm","20mm","30mm","40mm"] 
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
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.Control.closeDialog() #close the dialog

    # What is done when we click on the cancel button.
    # commented because this is the default behaviour
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

# GUI command that links the Python script
class _FilterStageCmd:

    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        baseWidget = QtGui.QWidget()
        panel = FilterStageTaskPanel(baseWidget)
        # having a panel with a widget in self.form and the accept and 
        # reject functions (if needed), we can open it:
        FreeCADGui.Control.showDialog(panel)

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Filter_Stage_',
            'Set Parameter Filter Stage')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Filter_Stage',
            'Creates a Filter Stage with set parametres')
        return {
            'Pixmap': __dir__ + '/icons/Filter_Stage_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

########################################################################################################
# Botón Filter Holder 
class _FilterHolderCmd:
    
    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        Widget_FilterHolder = QtGui.QWidget()
        Panel_FilterHolder = FilterHolderTaskPanel(Widget_FilterHolder)
        FreeCADGui.Control.showDialog(Panel_FilterHolder) 

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Filter Holder',
            'Filter Holder')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            '',
            'Creates a new Filter Holder')
        return {
            'Pixmap': __dir__ + '/icons/Filter_Holder_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class FilterHolderTaskPanel:
    def __init__(self, widget):
        self.form = widget
        # The layout will be a grid
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Filter Lenth ----
        # Label:
        self.Filter_Length_Label = QtGui.QLabel("Filter Length")
        # Spin Box that takes doubles
        self.Filter_Length_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Filter_Length_Value.setValue(60)
        # suffix to indicate the units
        self.Filter_Length_Value.setSuffix(' mm')

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Length_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Length_Value,0,1,1,1)

        # ---- row 1: Filter Width ----
        # Label:
        self.Filter_Width_Label = QtGui.QLabel("Filter Width")
        # Spin Box that takes doubles
        self.Filter_Width_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Filter_Width_Value.setValue(25)
        # suffix to indicate the units
        self.Filter_Width_Value.setSuffix(' mm')

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Width_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Width_Value,1,1,1,1)

        # ---- row 2: Set Holder ----
        self.Set_Label = QtGui.QLabel("See Set")
        self.ComboBox_Set = QtGui.QComboBox()
        # Type for ComboBox
        self.TextSet = ["No","Yes"]
        self.ComboBox_Set.addItems(self.TextSet)
        # Indicate inicial value in ComboBox
        self.ComboBox_Set.setCurrentIndex(self.TextSet.index('No'))

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Set_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_Set,2,1,1,1)

    def accept(self):
        Filter_Length = self.Filter_Length_Value.value()
        Filter_Width = self.Filter_Width_Value.value()
        Set_Select = self.ComboBox_Set.currentIndex()

        filter_holder_fun(Filter_Length, Filter_Width, Set_Select)
        
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.Control.closeDialog() #close the dialog
    
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

########################################################################################################
# Boton Idler Pulley & Belt Tensioner
class _TensionerCmd:
    
    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        Widget_Tensioner = QtGui.QWidget()
        Panel_Tensioner = TensionerTaskPanel(Widget_Tensioner)
        FreeCADGui.Control.showDialog(Panel_Tensioner) 
        

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Tensioner',
            'Tensioner')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            '',
            'Creates a new Tensioner')
        return {
            'Pixmap': __dir__ + '/icons/Tensioner_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class TensionerTaskPanel:
    def __init__(self, widget):
        self.form = widget
        # The layout will be a grid
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Belt High ----
        # Label:
        self.belt_h_Label = QtGui.QLabel("Belt hight:")
        # Spin Box that takes doubles
        self.belt_h_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.belt_h_Value.setValue(10)
        # suffix to indicate the units
        self.belt_h_Value.setSuffix(' mm')

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.belt_h_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.belt_h_Value,0,1,1,1)

        # ---- row 1: Base width ----
        # Label:
        self.base_w_Label = QtGui.QLabel("Base width:")  #10/15/20/30/40
        # Spin Box that takes doubles
        self.ComboBox_base_w = QtGui.QComboBox()
        # Diferents base
        self.TextBase_W = ["10mm","15mm","20mm","30mm","40mm"] 
        self.ComboBox_base_w.addItems(self.TextBase_W)
        self.ComboBox_base_w.setCurrentIndex(self.TextBase_W.index('20mm'))

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.base_w_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_base_w,1,1,1,1)
                
        # ---- row 2: Tensioner Stroke ----
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

        # ---- row 3: Wall thick ----
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

        # ---- row 4: Nut Type ----
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

        # ---- row 5: Set Holder ----
        self.Set_Label = QtGui.QLabel("See Set")
        self.ComboBox_Set = QtGui.QComboBox()
        # Type for ComboBox
        self.TextSet = ["No","Yes"]
        self.ComboBox_Set.addItems(self.TextSet)
        # Indicate inicial value in ComboBox
        self.ComboBox_Set.setCurrentIndex(self.TextSet.index('No'))

        # row 5, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Set_Label,5,0,1,1)
        # row 5, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_Set,5,1,1,1)

    def accept(self):
        IndexNut = {0:3,1:4,2:5,3:6}
        IndexBase = {0: 5, 1: 10, 2: 15, 3: 20, 4: 30, 5: 40}
        tensioner_belt_h = self.belt_h_Value.value()
        nut_hole = IndexNut[self.ComboBox_Nut_Hole.currentIndex()]
        tens_stroke = self.tens_stroke_Value.value()
        base_w = IndexBase[self.ComboBox_base_w.currentIndex()]
        wall_thick = self.wall_th_Value.value()
        Set_Select = self.ComboBox_Set.currentIndex()

        tensioner_fun(base_w,
                      tensioner_belt_h,
                      tens_stroke,
                      wall_thick,
                      nut_hole,
                      Set_Select) 
        
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.Control.closeDialog() #close the dialog
    
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()
    

########################################################################################################
# Botón Step Motor Holder 
class _MotorHolderCmd:
    
    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        Widget_MotorHolder = QtGui.QWidget()
        Panel_MotorHolder = MotorHolderTaskPanel(Widget_MotorHolder)
        FreeCADGui.Control.showDialog(Panel_MotorHolder) 
        

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Motor Holder',
            'Motor Holder')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            '',
            'Creates a new Motor Holder')
        return {
            'Pixmap': __dir__ + '/icons/Motor_Holder_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class MotorHolderTaskPanel:
    def __init__(self, widget):
        self.form = widget
        # The layout will be a grid
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Rail Max High  ----
        # Label:
        self.motor_high_Label = QtGui.QLabel("Rail max High")
        # Spin Box that takes doubles
        self.motor_high_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.motor_high_Value.setValue(40)
        # suffix to indicate the units
        self.motor_high_Value.setSuffix(' mm')

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.motor_high_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.motor_high_Value,0,1,1,1)

        # ---- row 1: Size Holder ----
        self.Size_Holder_Label = QtGui.QLabel("Size")
        self.ComboBox_Size_Holder = QtGui.QComboBox()
        # Type of Nut
        self.TextSizeHolder = ["8","11","14","17","23","34","42"]
        self.ComboBox_Size_Holder.addItems(self.TextSizeHolder)
        # Indicate inicial value in ComboBox
        self.ComboBox_Size_Holder.setCurrentIndex(self.TextSizeHolder.index('11'))

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Size_Holder_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_Size_Holder,1,1,1,1)

        # ---- row 2: Set Holder ----
        self.Set_Label = QtGui.QLabel("See Set")
        self.ComboBox_Set = QtGui.QComboBox()
        # Type for ComboBox
        self.TextSet = ["No","Yes"]
        self.ComboBox_Set.addItems(self.TextSet)
        # Indicate inicial value in ComboBox
        self.ComboBox_Set.setCurrentIndex(self.TextSet.index('No'))

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Set_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_Set,2,1,1,1)

    def accept(self):
        SizeHolder = {0:8, 1:11, 2:14, 3:17, 4:23, 5:34, 6:42}
        self.size_motor = SizeHolder[self.ComboBox_Size_Holder.currentIndex()]
        Set_Select = self.ComboBox_Set.currentIndex()
        h_motor=self.motor_high_Value.value()

        motor_holder_fun(self.size_motor, h_motor, Set_Select) 
        #make objetc with name: "nema" + str(self.size_motor) + "_motorholder"

        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.Control.closeDialog() #close the dialog
    
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

########################################################################################################
## NEW BUTTON TO CHANGE POSITION TO PRINT AND EXPORT ##
class _ChangePosExportCmd:
    def Activated(self):
        objSelect = FreeCADGui.Selection.getSelection()[0]#.Name
        print_export(objSelect)
        
    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Change Pos and Export',
            'Change Pos and Export')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            '',
            'Object select change to print position and export in .stl')
        return {
            'Pixmap': __dir__ + '/icons/Print_Export_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None  
    


#FreeCADGui.addCommand('Filter_Stage_filter_stage', _FilterStageCmd())
FreeCADGui.addCommand('Filter_Stage', _FilterStageCmd())
FreeCADGui.addCommand('Filter_Holder',_FilterHolderCmd())
FreeCADGui.addCommand('Tensioner',_TensionerCmd())
FreeCADGui.addCommand('Motor_Holder',_MotorHolderCmd())
FreeCADGui.addCommand('PosAndExport',_ChangePosExportCmd())