from user import User
import random
import smtplib
import re
import database_func as df
import register_window as rw
import PySimpleGUI as sg


def check_email(email):
    if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
        return True
    else:
        return False


def email_verification(name, email, code):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        try:
            server.login('allbuyco2022@gmail.com', 'onxvgueeekrealob')

            subject = 'Verify Email Address'
            body = f'Hi {name}! This is a AllBuy!\n\tThis is a verification message. Your code is: {code}.'

            msg = f'Subject: {subject}\n\n{body}'

            server.sendmail('allbuyco2022@gmail.com', f'{email}', msg)
        except smtplib.SMTPAuthenticationError as error:
            print(f'Something is wrong with sender data {error}')


def create_user(name, email, password, repeat_password):
    if len(name) != 0:
        if check_email(email):
            if len(password) in range(8, 17):
                if password == repeat_password:
                    random_code = ''.join([str(random.randint(0, 9)) for i in range(6)])
                    email_verification(name, email, random_code)
                    # add new import
                    if rw.email_confirmation_window(random_code):
                        user = User(name, email, password)
                        df.add_costumer(user)
                        return user
                    else:
                        sg.popup_error('Wrong code!', title='ERROR', font=('Bahnschrift', 16), line_width=150)
                else:
                    sg.popup_error('Passwords do not match!', title='ERROR', font=('Bahnschrift', 16), line_width=150)
            else:
                sg.popup_error('Password to short or to long!\nShould be from 8 to 16 characters',
                               title='ERROR', font=('Bahnschrift', 16), line_width=150)
        else:
            sg.popup_error('Not right format of email!', title='ERROR', font=('Bahnschrift', 16), line_width=150)
    else:
        sg.popup_error('User must have a name!', title='ERROR', font=('Bahnschrift', 16), line_width=150)
