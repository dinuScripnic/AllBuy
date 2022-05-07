from user import User
import sqlite3
import os.path

import PySimpleGUI as sg


def check_db():  # creates the dummy database if it doesn't exist
    if not os.path.exists('AllBuy.db'):
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        create_workspace = ''' CREATE TABLE costumers(
                              costumer_id VARCHAR(40) PRIMARY KEY,
                              costumer_name VARCHAR(255) NOT NULL,
                              costumer_email VARCHAR(255) UNIQUE NOT NULL ,
                              costumer_password VARCHAR(16) NOT NULL,
                              join_date TIMESTAMP
                              );
        '''
        cursor.execute(create_workspace)
        connection.commit()
        connection.close()


def add_costumer(user):
    """
        :param user: object of class User
        :return: same User, but in process used is added in database
    """
    try:  # works only if email is unique
        connection = sqlite3.connect('AllBuy.db')
        print('acces')
        cursor = connection.cursor()
        add_user = f''' INSERT INTO costumers(costumer_id, costumer_name, costumer_email, costumer_password, join_date) 
                      VALUES ('{user.id}', '{user.name}', '{user.email}', '{user.password}', '{user.join_date}');'''
        cursor.execute(add_user)
        connection.commit()
        print('commited')
        return user
    except sqlite3.IntegrityError:
        sg.popup_error('Email already in use!', title='ERROR', font=('Bahnschrift', 16), line_width=150)
    finally:
        if connection:
            cursor.close()
            connection.close()  # closes connection with database


def get_user(email, password):  # get user out of a database, needed for logging in
    """

        :param email: user email
        :param password: user password
        :return: user class object

    """
    try:
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        cursor.execute(f'SELECT * from costumers WHERE costumer_email = \'{email}\'')
        user_data = cursor.fetchall()  # searches for user
        if user_data:
            user_data = user_data[0]
            if password == user_data[3]:  # check if password is right
                user = User(user_data[1], user_data[2], user_data[3], user_data[0], user_data[4])
                # creates user according to existing data
                sg.popup('Logged in')
                return user
            else:
                sg.popup_error('Wrong Password!', title='ERROR', font=('Bahnschrift', 16), line_width=150)
        else:
            sg.popup_error('User not found', title='ERROR', font=('Bahnschrift', 16), line_width=150)
    finally:
        if connection:
            cursor.close()
            connection.close()


def get_product(searched_name):
    """

        :param searched_name: input from search
        :return: displays items related to

    """
    try:
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        cursor.execute(f'SELECT * from products WHERE name LIKE \'%{searched_name}%\'')
        user_data = cursor.fetchall()  # searches for user

    finally:
        if connection:
            cursor.close()
            connection.close()