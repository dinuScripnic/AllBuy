import PySimpleGUI as sg
import user_functionality as ur


def change_password(user):
    layout = [
        [sg.Text('Change Password', size=(20, 1), justification='center', font=("Bookman Old Style", 13))],

        [
            sg.Text("Password", size=(15, 1), font=("Bookman Old Style", 11)),
            sg.InputText(key="-password-", password_char='*'),
        ],
        [
            sg.Text("Confirm Password", size=(15, 1), font=("Bookman Old Style", 11)),
            sg.InputText(key="-repeat_password-", password_char='*'),
        ],
        [sg.Button("Change Password", font=("Bookman Old Style", 10), size=(10, 2))],
    ]
    window = sg.Window("Change Password", layout, element_justification="c", size=(450, 160))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Change Password":
            password = values["-password-"]
            repeat_password = values["-repeat_password-"]
            if ur.change_password(user.id, user.name, user.email, password, repeat_password):
                window.close()
                return True
