# ComboBox Tutorial 

***

## Need to know  
***
To understand this tutorial it is necessary to know how to make a workbench. If you don't know how to do that then visit this [tutorial][dirTuto].

[dirTuto]: https://github.com/felipe-m/tutorial_freecad_wb

At this moment we know how to do a doble spin widget, but now we will create a ComboBox.  

***

## Do a ComboBox   
***
To create a ComboBox is used the following statement:

    Combo = QtGui.QComboBox()

### Add items  
You can add one item by doing the following:

    Combo.addItem("Item one")

If you like to add more than one item you could repeat this step as many times as items you would like to add.
Also, you could create a list with all the items and only add this list to the ComBox.

    ItemList = ["Item one", "Item two", "Item three"]
    Combo.addItems(ItemList)

### Example  
Now we could do an example of a  Takspanel with a ComboBox:

    class TutorialTaskPanel:                                    
      def __init__(self,widget):
        self.form = widget
        # The layout will be a grid, since the form is an argument
        layout = QtGui.QGridLayout(self.form)
        #Label:
        self.Combo_Label = QtGui.QLabel("Combo:")   

        # Combo Box that have multiple choice
        self.Combo = QtGui.QComboBox()
        # List of values in ComboBox
        self.TextList = ["One","Two","Three"]
        self.Combo.addItems(self.TextIndex)
        # Indicate inicial value in ComboBox
        self.Combo.setCurrentIndex(self.TextIndex.index('One'))

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Combo_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Combo,0,1,1,1)

### Recover value  
Finally, we need to recover the value that has been selected by the user. We get that value from the position that the user has selected:

    TextSelect = self.Combo.currentIndex()
























