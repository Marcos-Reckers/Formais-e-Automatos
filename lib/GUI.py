import PySimpleGUI as sg

def seleciona_arquivo():
    """Cria a janela para procurar e criar a base de dados"""
    layout = [
        [sg.Text('Caminho para seu arquivo')],
        [sg.Combo(sg.user_settings_get_entry('-filenames-', []), default_value=sg.user_settings_get_entry(
            '-last filename-', ''), size=(80, 1), key='-FILENAME-'), sg.FileBrowse()],
        [sg.Button('Go'), sg.Button('Exit')]
    ]
    
    event, values = sg.Window('Insira o caminho para o seu arquivo', layout).read(close=True)
    
    if event == 'Go':
        sg.user_settings_set_entry(
            '-filenames-', list(set(sg.user_settings_get_entry('-filenames-', []) + [values['-FILENAME-'], ])))
        sg.user_settings_set_entry('-last filename-', values['-FILENAME-'])
    
    return values['-FILENAME-']

def popup(title: str, inputs: list[str])->str:
    buttons:list = [sg.Button(x)for x in inputs]
    layout = [  
                [sg.Text(title)],
                buttons
            ]
    
    # Create the Window
    event, values = sg.Window(title, layout, element_justification='center').read(close=True)
    # Event Loop to process "events" and get the "values" of the inputs
    
    return event

def popup_text(title: str, question:str)->str:
    layout = [  
                [sg.Text(title)],
                [sg.Text(question), sg.InputText(key='-INPUT-')],
                [sg.Button('enviar')]
            ]
    
    # Create the Window
    event, values = sg.Window(title, layout, element_justification='center').read(close=True)
    # Event Loop to process "events" and get the "values" of the inputs
    
    return values['-INPUT-']

def popup_error(title: str, message:str) -> None:
    layout = [  
                [sg.Text(title)],
                [sg.Text(message)],
                [sg.Button('Ok')]
            ]
    
    # Create the Window
    event, values = sg.Window(title, layout, element_justification='center').read(close=True)
    # Event Loop to process "events" and get the "values" of the inputs