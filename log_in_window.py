import PySimpleGUI as sg
import database_func as df
import register_window as rw


def log_in_window():
    sg.theme("NeutralBlue")
    layout = [
        [sg.Text("Welcome Back!", font=("Bookman Old Style", 14))],
        [
            sg.Text("Email", size=(10, 1), font=("Bookman Old Style", 11)),
            sg.InputText(key="-email-", size=(25, 1)),
        ],
        [
            sg.Text("Password", size=(10, 1), font=("Bookman Old Style", 11)),
            sg.InputText(key="-password-", size=(25, 1)),
        ],
        [
            sg.Button("Log in", font=("Bookman Old Style", 10), size=(10, 1)),
            sg.Button("Register", font=("Bookman Old Style", 10), size=(10, 1)),
        ],
    ]
    window = sg.Window("Log in", layout, element_justification="c", size=(350, 150))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Log in":
            out = df.get_user(values["-email-"], values["-password-"])
            if out:
                window.close()
                return out
        elif event == "Register":
            window.close()
            out = rw.register_window()
            return out


def account(user):
    sg.theme("NeutralBlue")
    layout = [
        [sg.Text("Welcome Back!", font=("Bookman Old Style", 14))],

        [sg.Image(filename='user.jpg')]
    ]
    window = sg.Window("Log in", layout, element_justification="c", size=(350, 150))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Log in":
            out = df.get_user(values["-email-"], values["-password-"])
            if out:
                window.close()
                return out
        elif event == "Register":
            window.close()
            out = rw.register_window()
            return out