import PySimpleGUI as sg
import database_func as df
import register_window as rw


def log_in_window():
    sg.theme('DarkAmber')
    layout = [
              [sg.Text('Hello')],
              [sg.Text('Email'), sg.InputText(key='-email-')],
              [sg.Text('Password'), sg.InputText(key='-password-')],
              [sg.Button('Log in'), sg.Button('Register')]
              ]
    window = sg.Window('Log in', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Log in':
            password = values['-password-']
            email = values['-email-']
            out = df.get_user(email, password)
            if out:
                print(out)
                print(out.join_date)
                window.close()
                return out
        elif event == 'Register':
            window.close()
            rw.register_window()

