from user import User
import random
import smtplib
import re
import database_func as df
import register_window as rw
import PySimpleGUI as sg


def check_email(email):

    """
        :param email: email that has to be checked if is valid format
        :return: true/ false if email is valid
    """
    if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
        return True
    else:
        return False


def email_verification(name, email, code):
    """

    :param name: user_name
    :param email: user_email
    :param code: randomly generated to verify email
    :return: sends email to mentioned email address with the code in order to verify if this email belongs to our user
    """
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
    """
    :param name: user name
    :param email: user
    :param password:
    :param repeat_password:
    :return: handles all the operations to get user_data, check it, validate it and send to database
    """
    if len(name) != 0:  # check if name is long enough
        if check_email(email):  # check email validity using regex
            if len(password) in range(8, 17):  # check if password is long enough
                if password == repeat_password:  # check if passwords match
                    # generates the verification code
                    random_code = ''.join([str(random.randint(0, 9)) for i in range(6)])
                    # verifies email
                    email_verification(name, email, random_code)
                    # add new import
                    if rw.email_confirmation_window(random_code):
                        # creates an object of class user
                        user = User(name, email, password)
                        # adds to database
                        df.add_costumer(user)
                        # returns user for later usage
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


def email_finish(user, products, price):
    """

    :param name: user_name
    :param email: user_email
    :param code: randomly generated to verify email
    :return: sends email to mentioned email address with the code in order to verify if this email belongs to our user
    """
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        try:
            server.login('allbuyco2022@gmail.com', 'onxvgueeekrealob')

            subject = 'Purchase Successful'
            for product in products:
                products += f'{product}, '
            body = f'Hi {user.name}! This is a AllBuy!\n\tYour  Your code is: {code}.'

            msg = f'Subject: {subject}\n\n{body}'
            print(msg)

            # server.sendmail('allbuyco2022@gmail.com', f'{email}', msg)
        except smtplib.SMTPAuthenticationError as error:
            print(f'Something is wrong with sender data {error}')

