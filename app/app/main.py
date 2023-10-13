import PySimpleGUI as sg
import excell

button_size=(30,2)
sg.theme('LightGreen5')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Normalizar Tablas')],
            [sg.Text('Directorio de archivo excell') ],
            [[sg.InputText(size=(60,30)),sg.FileBrowse(key="-IN-")]],
            [sg.Text("Nuevo Archivo")],
            [ sg.InputText(size=(60,30),key="-OUT-"), sg.FolderBrowse("Folder")],
            [sg.Text("Nombre de hoja"),sg.InputText(size=(60,30),key="SHEET")],
            [sg.Button('Ok',size=button_size) , sg.Button('Cancel',size=button_size)] ]

# Create the Window
window = sg.Window('Normalizador Excel', layout,size=(600,250))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event =="Ok":
        file=values["-IN-"]
        out=values["-OUT-"]
        sheet=values["SHEET"]
        excell.run_procedure(file,sheet,out)
        pass

window.close()





