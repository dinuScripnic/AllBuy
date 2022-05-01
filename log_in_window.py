import PySimpleGUI as sg
import database_func as df
import user_registration as ur


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
            window.close()
        elif event == 'Log in':
            password = values['-password-']
            email = values['-email-']
            out = df.get_user(email, password)
            if out:
                print(out)
                window.close()
        elif event == 'Register':
            window.close()
            register_window()


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
            window.close()
        elif event == 'Register':
            name = values['-name-']
            email = values['-email-']
            password = values['-password-']
            repeat_password = values['-repeat_password-']
            ur.create_user(name, email, password, repeat_password)
            window.close()


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




# def progress_bar():
#     sg.theme('LightBlue2')
#     layout = [[sg.Text('Creating your account...')],
#             [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
#             [sg.Cancel()]]
#
#     window = sg.Window('Working...', layout)
#     for i in range(1000):
#         event, values = window.read(timeout=1)
#         if event == 'Cancel' or event == sg.WIN_CLOSED:
#             break
#         window['progbar'].update_bar(i + 1)
#     window.close()
log_in_window()