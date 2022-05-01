from user import User
import random
import smtplib
import re
import database_func as df
import register_window as rw
import PySimpleGUI as sg
import psycopg2


def check_user_not_exist(email):
        # email = f'\'{email}\''
        try:
            connection = psycopg2.connect(user='postgres', password='Dinu2003', host='localhost', port='5432',
                                          database='AllBuy')
            cursor = connection.cursor()
            # search if user email is unique
            cursor.execute(f'SELECT * from user_data WHERE email = \'{email}\'')
            if cursor.fetchall():
                return False
            else:
                return True
        except (Exception, psycopg2.Error) as error:
            # popup error
            print(error)
        finally:
            if connection:
                cursor.close()
                connection.close()


def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
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
    if check_email(email):
        if check_user_not_exist(email):
            if len(password) >= 8:
                if password == repeat_password:
                    random_code = ''.join([str(random.randint(0, 9)) for i in range(6)])
                    email_verification(name, email, random_code)
                    # add new import
                    if rw.email_confirmation_window(random_code):
                        user = User(name, email, password)
                        df.add_user(user)
                        return user
                    else:
                        sg.popup_error('Wrong code')
                else:
                    sg.popup_error('Passwords do not match')
            else:
                sg.popup_error('Password to short')
        else:
            sg.popup_error('Email already in use')
    else:
        sg.popup_error('Not valid email')
