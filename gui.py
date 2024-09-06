import functions

import FreeSimpleGUI as sg

Label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter To-do", key='todo')
Add_button = sg.Button("Add")
window = sg.Window('My To-do App',
                   layout=[[Label, input_box, Add_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case  sg.WIN_CLOSED:
            break


window.close()
