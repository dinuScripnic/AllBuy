import PySimpleGUI as sg
import database_functionality as df
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
            # searches for this user in the database
            out = df.get_user(values["-email-"], values["-password-"])
            if out:
                # returns and closes window if everything is ok
                window.close()
                return out

        elif event == "Register":
            # if user wants to register a new profile, closes the logging in and opens a new widget
            window.close()
            out = rw.register_window()
            return out
