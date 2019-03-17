# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# -- Function Print and Export Object
# ----------------------------------------------------------------------------
# -- (c) David Muñoz Bernal
# ----------------------------------------------------------------------------
# -- This function set the object to yhe print position and export the object.
import os
import sys
import FreeCAD
import FreeCADGui
import PySide
from PySide import QtCore, QtGui

def print_export(objSelect):
    show_message = True
    nema = 'motorholder'
    if  nema in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,1,0),180) 
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif objSelect.Name == 'idler_tensioner':
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,1,0),90)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif objSelect.Name == 'tensioner_holder':
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,0),-90)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif objSelect.Name == 'filter_holder':
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    else:
        FreeCAD.Console.PrintMessage('This object is not a workbench object.\n')
        show_message = False

    if show_message == True:
        FreeCAD.Console.PrintMessage("You select" + objSelect.Name + " to change to print position and export.\n")
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
