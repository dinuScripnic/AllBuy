import psycopg2
from user import User
import PySimpleGUI as sg
# User_data(id(int)(PK),name(str),email(str),password(str),join_date(time))
# make popups nice


def add_user(user):  # needed for registration
    """
    :param user: object of class User
    :return: same User, but in process used is added in database

    """
    _id = f'\'{user.id}\''
    name = f'\'{user.name}\''
    email = f'\'{user.email}\''
    password = f'\'{user.password}\''
    join_date = f'\'{user.join_date}\''
    # gets all re required data and transforms it into proper sql format
    try:
        connection = psycopg2.connect(user='postgres', password='Dinu2003', host='localhost', port='5432',
                                      database='AllBuy')
        cursor = connection.cursor()
        # connects with local database
        add_user = f'''INSERT INTO user_data (id, name, email, password, join_date)
                       VALUES ({_id}, {name}, {email}, {password}, {join_date});'''
        # inserts into existing database
        cursor.execute(add_user)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        # handles errors
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()  # closes connection with database no mater what happened


def get_user(email, password):  # get user out of a database, needed for logging in
    """

    :param email: user email
    :param password: user password
    :return: user class object

    """
    try:
        connection = psycopg2.connect(user='postgres', password='Dinu2003', host='localhost', port='5432',
                                      database='AllBuy')
        cursor = connection.cursor()
        cursor.execute(f'SELECT * from user_data WHERE email = \'{email}\'')
        user_data = cursor.fetchall()  # searches for user
        if user_data:
            user_data = user_data[0]
            if password == user_data[3]:  # check if password is right
                user = User(user_data[1], user_data[2], user_data[3], user_data[0], user_data[4])
                # creates user according to existing data
                sg.popup('Logged in')
                return user
            else:
                sg.popup_error('Wrong password')
        else:
            sg.popup_error('User not found')
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()








# def add_item(item):
#     try:
#         connection = psycopg2.connect(user='postgres', password='Dinu2003', host='localhost', port='5432',
#                                       database='AllBuy')
#         cursor = connection.cursor()
#         create_user = '''CREATE TABLE user_data
#         (id VARCHAR(255) PRIMARY KEY,
#         name VARCHAR(255),
#         email VARCHAR(255) NOT NULL,
#         password VARCHAR(255) NOT NULL,
#         join_date TIMESTAMP NOT NULL);
#         '''
#         cursor.execute(create_user)
#         connection.commit()
#         print('Table added')
#         cursor.execute("SELECT * from user_data")
#         print("Result ", cursor.fetchall())
#     except (Exception, psycopg2.Error) as error:
#         print(error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
