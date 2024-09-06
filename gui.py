import functions

import FreeSimpleGUI as sg

Label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter To-do")
Add_button = sg.Button("Add")
window = sg.Window('My To-do App', layout=[[Label, input_box, Add_button]])
window.read()
window.close()