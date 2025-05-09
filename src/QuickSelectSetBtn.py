import MayaTools
from MayaUtil import QMayaWindow
import maya.cmds as cmds
from PySide2.QtWidgets import (QMessageBox, QPushButton, QVBoxLayout)

class QuickSelectSetBtn:
    def Create(self):
        # Get the currently selected objects
        selected_objects = cmds.ls(selection=True)
    # Check if there are any selected objects
        if selected_objects:
        # Create a new set with the selected objects
            set_name = "newSet"
            cmds.sets(selected_objects, name=set_name)
            print(f"Set '{set_name}' created with selected objects.")
        else:
            print("No objects selected.")

        set_name = "newSet"
        command = f'cmds.select("{set_name}")'
        shelf_name = "Animation" 
        icon_path = "commandButton.png"

        if selected_objects:
        # Create the shelf button
            cmds.shelfButton(
                label=set_name,
                image=icon_path,
                command=command,
                parent=shelf_name
                )   
            
            print(f"Shelf button for '{set_name}' added to '{shelf_name}'.")

        else:
            print("no set to add to shelf")
            QMessageBox.critical(self, "Error", "Please Select Something To Make A Set Of!")


class QuickSelectSetWindow(QMayaWindow):
    def __init__(self): #creates constructor for UI Window
        super().__init__()
        self.QuickSelectSet = QuickSelectSetBtn()

        self.masterLayout = QVBoxLayout() #gets the layout from QT
        self.setLayout(self.masterLayout)

        self.createSetBtn = QPushButton("Add Selected To Animation Shelf") # creates and names the auto find button
        self.masterLayout.addWidget(self.createSetBtn) # adds the auto find button to the window
        self.createSetBtn.clicked.connect(self.CreateSetBtnClicked)

        self.setWindowTitle("Add To Shelf: Quick Select Set")

    def CreateSetBtnClicked(self):
        try:
            self.QuickSelectSet.Create() 
        except Exception as e:
            QMessageBox.critical(self, "Error", "Please Select Something To Make A Set Of!")

def Run():
    quickSelectSetWindow = QuickSelectSetWindow()
    quickSelectSetWindow.show()