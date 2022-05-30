import PySimpleGUI as sg
import user_functionality as ur


def register_window():
    sg.theme("NeutralBlue")
    layout = [
        [sg.Text("Welcome to AllBuy!", font=("Bookman Old Style", 13))],
        [sg.Text("We wish you successful shopping!", font=("Bookman Old Style", 13))],
        [
            sg.Text("Name", size=(15, 1), font=("Bookman Old Style", 11)),
            sg.InputText(key="-name-"),
        ],
        [
            sg.Text("Email", size=(15, 1), font=("Bookman Old Style", 11)),
            sg.InputText(key="-email-"),
        ],
        [
            sg.Text("Password", size=(15, 1), font=("Bookman Old Style", 11)),
            sg.InputText(key="-password-"),
        ],
        [
            sg.Text("Confirm Password", size=(15, 1), font=("Bookman Old Style", 11)),
            sg.InputText(key="-repeat_password-"),
        ],
        [sg.Button("Register", font=("Bookman Old Style", 10), size=(10, 1))],
    ]
    window = sg.Window("Sign Up", layout, element_justification="c", size=(450, 220))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Register":
            out = ur.create_user(
                values["-name-"],
                values["-email-"],
                values["-password-"],
                values["-repeat_password-"],
            )
            if out:
                window.close()
                return out


def email_confirmation_window(generated_code):
    sg.theme("NeutralBlue")
    layout = [
        [sg.Text("Confirmation code", font=("Bookman Old Style", 12))],
        [sg.InputText(key="-code-", size=(30, 1))],
        [
            sg.Button("Confirm", font=("Bookman Old Style", 10), size=(7, 1)),
            sg.Button("Return", font=("Bookman Old Style", 10), size=(7, 1)),
        ],
    ]
    window = sg.Window("Confirmation", layout, element_justification="c")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Confirm":
            if values["-code-"] == generated_code:
                window.close()
                return True
            else:
                return False
        elif event == "Return":
            window.close()
            register_window()
