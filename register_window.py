import PySimpleGUI as sg
import user_registration as ur


def register_window():
    sg.theme('DarkAmber')
    layout = [
              [sg.Text('Hello')],
              [sg.Text('Name'), sg.InputText(key='-name-')],
              [sg.Text('Email'), sg.InputText(key='-email-')],
              [sg.Text('Password'), sg.InputText(key='-password-')],
              [sg.Text('Confirm Password'), sg.InputText(key='-repeat_password-')],
              [sg.Button('Register')]
              ]
    window = sg.Window('Sign Up', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Register':
            name = values['-name-']
            email = values['-email-']
            password = values['-password-']
            repeat_password = values['-repeat_password-']
            out = ur.create_user(name, email, password, repeat_password)
            if out:
                window.close()
                return out


def email_confirmation_window(generated_code):
    sg.theme('DarkAmber')
    layout = [
              [sg.Text('Confirmation code')],
              [sg.InputText(key='-code-')],
              [sg.Button('Confirm'), sg.Button('Return')]
              ]
    window = sg.Window('Confirmation', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Confirm':
            code = values['-code-']
            if code == generated_code:
                window.close()
                return True
            else:
                return False
        elif event == 'Return':
            window.close()
            register_window()
