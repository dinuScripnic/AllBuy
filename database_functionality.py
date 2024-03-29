from user import User
import sqlite3
import os.path
import PySimpleGUI as sg
from categories import *
import random


def check_db():  # creates the dummy database if it doesn't exist
    if not os.path.exists('AllBuy.db'):
        print('Create Database')
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        create_workspace = '''CREATE TABLE costumers(
                              costumer_id VARCHAR(40) PRIMARY KEY,
                              costumer_name VARCHAR(255) NOT NULL,
                              costumer_email VARCHAR(255) UNIQUE NOT NULL ,
                              costumer_password VARCHAR(16) NOT NULL,
                              join_date TIMESTAMP);'''
        cursor.execute(create_workspace)
        connection.commit()
        create_workspace = '''CREATE TABLE product(
                              category INTEGER,
                              id VARCHAR(40) PRIMARY KEY,
                              name VARCHAR(255),
                              brand VARCHAR(255),
                              model VARCHAR(255),
                              description VARCHAR(4000),
                              price INTEGER,
                              currency VARCHAR(1),
                              add_time TIMESTAMP);'''
        cursor.execute(create_workspace)
        connection.commit()
        create_workspace = '''CREATE TABLE laptop(
                              id VARCHAR(40) PRIMARY KEY,
                              processor VARCHAR(255),
                              ram INTEGER,
                              display_size FLOAT,
                              display_quality VARCHAR(255),
                              ssd BOOLEAN,
                              storage_size INTEGER,
                              graphics BOOLEAN,
                              vram INTEGER,
                              image VARCHAR(255));
                              FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE);'''
        cursor.execute(create_workspace)
        connection.commit()
        create_workspace = '''CREATE TABLE tablet(
                                  id VARCHAR(40) PRIMARY KEY,
                                  processor VARCHAR(255),
                                  ram INTEGER,
                                  display_size FLOAT,
                                  display_quality VARCHAR(255),
                                  network BOOLEAN,
                                  storage_size INTEGER,
                                  battery INTEGER,
                                  image VARCHAR(255))
                                  FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE
                              );'''
        cursor.execute(create_workspace)
        connection.commit()
        create_workspace = '''CREATE TABLE smartphone(
                              id VARCHAR(40) PRIMARY KEY,
                              processor VARCHAR(255),
                              ram INTEGER,
                              display_size FLOAT,
                              display_quality VARCHAR(255),
                              dual_sim BOOLEAN,
                              storage_size INTEGER,
                              battery INTEGER,
                              image VARCHAR(255))
                              FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE);'''
        cursor.execute(create_workspace)
        connection.commit()
        create_workspace = '''CREATE TABLE review(
                              id VARCHAR(40),
                              grade FLOAT,
                              description VARCHAR(4000),
                              FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE);'''
        cursor.execute(create_workspace)
        connection.commit()
        create_workspace = '''CREATE TABLE basket(
                              user VARCHAR(40),
                              product VARCHAR(40),
                              category INTEGER ,
                              FOREIGN KEY (user) REFERENCES costumers(costumer_id) on DELETE CASCADE on UPDATE CASCADE
                              FOREIGN KEY (product) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE);'''
        cursor.execute(create_workspace)
        connection.commit()
        connection.close()


def add_costumer(user):  # adds user ot database, required for register
    """

        :param user: object of class User
        :return: same User, but in process used is added in database

    """
    try:  # works only if email is unique
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        add_user = f''' INSERT INTO costumers(costumer_id, costumer_name, costumer_email, costumer_password, join_date) 
                        VALUES ("{user.id}", "{user.name}", "{user.email}", "{user.password}", "{user.join_date}");'''
        cursor.execute(add_user)
        connection.commit()
        return user
    except sqlite3.IntegrityError:  # check if email is unique
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
                sg.popup("Logged in")
                return user
            else:
                sg.popup_error('Wrong Password!', title='ERROR', font=('Bahnschrift', 16), line_width=150)
        else:
            sg.popup_error('User not found', title='ERROR', font=('Bahnschrift', 16), line_width=150)
    finally:
        if connection:
            cursor.close()
            connection.close()


def change_password(user_id, new_password):
    """

        :param user: user class object
        :param new_password: new password
    """
    try:
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        cursor.execute(f'UPDATE costumers SET costumer_password = \'{new_password}\' WHERE costumer_id = \'{user_id}\'')
        connection.commit()
        sg.popup("Password changed")
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


def add_laptop(laptop):
    """

        :param laptop: object of class laptop
        :return: adds to database

    """
    try:
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        if not laptop.vram:
            laptop.vram = 'NULL'
        # adds general data to product table
        add = f'''INSERT INTO product VALUES ({laptop.category}, "{laptop._id}", "{laptop.name}", "{laptop.brand}", "{laptop.model}", "{laptop.description}", {laptop.price}, "{laptop.currency}", "{laptop.add_time}");'''
        cursor.execute(add)
        # add more specific data to laptop table
        add = f'''INSERT INTO laptop VALUES ("{laptop._id}", "{laptop.processor}", {laptop.ram}, {laptop.display_size}, "{laptop.display_quality}", {laptop.ssd}, {laptop.storage}, {laptop.graphics}, {laptop.vram}, "{laptop.image}"); '''
        cursor.execute(add)
        connection.commit()
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


def add_tablet(tablet):
    """

        :param tablet: object of class tablet
        :return: adds to database

    """
    try:
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        # adds general data to product table
        add = f'''INSERT INTO product VALUES ({tablet.category}, "{tablet._id}", "{tablet.name}", "{tablet.brand}", "{tablet.model}", "{tablet.description}", {tablet.price}, "{tablet.currency}", "{tablet.add_time}");'''
        cursor.execute(add)
        # adds more specific data to tablet table
        add = f'''INSERT INTO tablet VALUES ("{tablet._id}", "{tablet.processor}", {tablet.ram}, {tablet.display_size}, "{tablet.display_quality}", {tablet.network}, {tablet.storage}, {tablet.battery}, "{tablet.image}");'''
        cursor.execute(add)
        connection.commit()
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


def add_smartphone(smartphone):

    """

        :param smartphone: object of class smartphone
        :return: adds to database

    """
    try:
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        # adds general data to product table
        add = f'''INSERT INTO product VALUES ({smartphone.category}, "{smartphone._id}", "{smartphone.name}", "{smartphone.brand}", "{smartphone.model}", "{smartphone.description}", {smartphone.price}, "{smartphone.currency}", "{smartphone.add_time}");'''
        cursor.execute(add)
        # adds more general data to smartphone table
        add = f'''INSERT INTO smartphone VALUES ("{smartphone._id}", "{smartphone.processor}", {smartphone.ram}, {smartphone.display_size}, "{smartphone.display_quality}", {smartphone.double_sim}, {smartphone.storage}, {smartphone.battery}, "{smartphone.image}"); '''
        cursor.execute(add)
        connection.commit()
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


def get_all_products():
    """

        :return: return a list of all products,
        not the most optimal way in working with big databases, but for now it works

    """
    try:
        connection = sqlite3.connect('AllBuy.db')
        output = []
        cursor = connection.cursor()
        cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, laptop.processor, laptop.ram, laptop.display_size, laptop.display_quality, laptop.ssd, laptop.storage_size, laptop.graphics, laptop.vram, product.description, product.price, product.currency, product.add_time, laptop.image
                           FROM product JOIN laptop ON product.id = laptop.id''')
        product_data = cursor.fetchall()  # searches for all laptops
        for object in product_data:
            # creates products of certain class and assigns to output
            output.append(Laptop(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4],
                              processor=object[5], ram=object[6], display_size=object[7], display_quality=object[8],
                              ssd=object[9], storage=object[10], graphics=object[11], vram=object[12],
                              description=object[13], price=object[14], currency=object[15], add_time=object[16], image=object[17]))
        cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, tablet.processor, tablet.ram, tablet.battery, tablet.display_size, tablet.display_quality, tablet.network, tablet.storage_size, product.description, product.price, product.currency, product.add_time, tablet.image
                           FROM product JOIN tablet ON product.id = tablet.id''')
        product_data = cursor.fetchall()  # searches for tablets
        for object in product_data:
            # creates products of certain class and assigns to output
            output.append(Tablet(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4], processor=object[5], ram=object[6], battery=object[7], display_size=object[8], display_quality=object[9], network=object[10], storage=object[11], description=object[12],price=object[13], currency=object[14], add_time=object[15], image=object[16]))
        cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, smartphone.processor, smartphone.ram, smartphone.display_size, smartphone.display_quality, smartphone.dual_sim, smartphone.storage_size, smartphone.battery, product.description, product.price, product.currency, product.add_time, smartphone.image
                           FROM product JOIN smartphone ON product.id = smartphone.id''')
        product_data = cursor.fetchall()  # searches for smartphones
        for object in product_data:
            # creates products of certain class and assigns to output
            output.append(Smartphone(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4], processor=object[5], ram=object[6], battery=object[11], display_size=object[7], display_quality=object[8], storage=object[10], double_sim=object[9], description=object[12], price=object[13], currency=object[14], add_time=object[15], image=object[16]))
        random.shuffle(output)  # shuffles se we don't always have laptop first
        return output
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


def search_product(searched_name):
    """

        :param searched_name: input from search
        :return: displays items related to

    """
    try:
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        cursor.execute(f'SELECT * from product WHERE name LIKE \'%{searched_name}%\'')
        product_data = cursor.fetchall()  # searches for products with a certain name
        out = []
        for data in product_data:
            if data[0] == 1:
                command = f'''SELECT product.category, product.id, product.name, product.brand, product.model, laptop.processor, laptop.ram, laptop.display_size, laptop.display_quality, laptop.ssd, laptop.storage_size, laptop.graphics, laptop.vram, product.description, product.price, product.currency, product.add_time, laptop.image
                              FROM product JOIN laptop ON product.id = laptop.id WHERE product.id = '{data[1]}' '''
                cursor.execute(command)
                object = cursor.fetchall()[0]
                # creates products of certain class and assigns to output
                out.append(Laptop(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4],
                                  processor=object[5], ram=object[6], display_size=object[7], display_quality=object[8],
                                  ssd=object[9], storage=object[10], graphics=object[11], vram=object[12],
                                  description=object[13], price=object[14], currency=object[15], add_time=object[16], image=object[17]))
            elif data[0] == 2:
                cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, tablet.processor, tablet.ram, tablet.battery, tablet.display_size, tablet.display_quality, tablet.network, tablet.storage_size, product.description, product.price, product.currency, product.add_time, tablet.image
                                   FROM product JOIN tablet ON product.id = tablet.id  WHERE product.id = '{data[1]}' ''')
                object = cursor.fetchall()[0]
                # creates products of certain class and assigns to output
                out.append(
                    Tablet(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4],
                           processor=object[5], ram=object[6], battery=object[7], display_size=object[8],
                           display_quality=object[9], network=object[10], storage=object[11], description=object[12],
                           price=object[13], currency=object[14], add_time=object[15], image=object[16]))

            elif data[0] == 3:
                cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, smartphone.processor, smartphone.ram, smartphone.display_size, smartphone.display_quality, smartphone.dual_sim, smartphone.storage_size, smartphone.battery, product.description, product.price, product.currency, product.add_time, smartphone.image
                                   FROM product JOIN smartphone ON product.id = smartphone.id  WHERE product.id = '{data[1]}' ''')
                object = cursor.fetchall()[0]
                # creates products of certain class and assigns to output
                out.append(
                    Smartphone(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4],
                               processor=object[5], ram=object[6], battery=object[11], display_size=object[7],
                               display_quality=object[8], storage=object[10], double_sim=object[9],
                               description=object[12], price=object[13], currency=object[14], add_time=object[15], image=object[16]))
        return out
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


def filter_laptop(parameters):
    """

        :param parameters: parameters set through filter menu
        :return: list of items that passed the filter

    """
    try:
        keys = parameters.keys()
        out = []
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        filter = f'''SELECT product.category, product.id, product.name, product.brand, product.model, laptop.processor, laptop.ram, laptop.display_size, laptop.display_quality, laptop.ssd, laptop.storage_size, laptop.graphics, laptop.vram, product.description, product.price, product.currency, product.add_time, laptop.image
                     FROM product JOIN laptop ON product.id = laptop.id 
                     WHERE laptop.ram = {parameters['ram']} AND '''
        # generates the sql call for filter function
        if 'brand' in keys:
            filter += f"product.brand = '{parameters['brand']}' AND "
        if 'processor' in keys:
            filter += f"laptop.processor = '{parameters['processor']}' AND "
        if 'graphics' in keys:
            filter += f"laptop.graphics = {parameters['graphics']} AND "
        if 'storage_type' in keys:
            filter += f"laptop.ssd = {parameters['storage_type']} AND "
        if 'storage_size' in keys:
            if parameters['storage_size'] == '512' or parameters['storage_size'] == '1024':
                filter += f"laptop.storage_size = {parameters['storage_size']} AND "
            elif parameters['storage_size'] == '<64':
                filter += f"laptop.storage_size in (128,256) AND "
            elif parameters['storage_size'] == '>1024':
                filter += f"laptop.storage_size > 1024 AND "
        if 'screen_size' in keys:
            if parameters['screen_size'] == '<14':
                filter += f"laptop.display_size <= 14 AND "
            if parameters['screen_size'] == '17.3':
                filter += f"laptop.display_size = 17.3 AND "
            elif parameters['screen_size'] == "14`-16`":
                filter += f"laptop.display_size in (15.6, 16) AND "
        if 'screen_quality' in keys:
            if parameters['screen_quality'] == 'Standard':
                filter += f"laptop.display_quality in ('HD', 'Full HD') AND "
            elif parameters['screen_quality'] == 'Good':
                filter += f"laptop.display_quality in ('Quad HD', '2K') AND "
            elif parameters['screen_quality'] == 'Premium':
                filter += f"laptop.display_quality in ('3K', '4K') AND "
        cursor.execute(filter[:-5])
        objects = cursor.fetchall()
        for object in objects:
            # appends to output laptop
            out.append(Laptop(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4], processor=object[5], ram=object[6], display_size=object[7], display_quality=object[8], ssd=object[9], storage=object[10], graphics=object[11], vram=object[12], description=object[13], price=object[14], currency=object[15], add_time=object[16], image=object[17]))
        return out
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


def filter_tablet(parameters):
    """

        :param parameters: parameters set through filter menu
        :return: list of items that passed the filter

    """
    try:
        keys = parameters.keys()
        output = []
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        filter = f'''SELECT product.category, product.id, product.name, product.brand, product.model, tablet.processor, tablet.ram, tablet.battery, tablet.display_size, tablet.display_quality, tablet.network, tablet.storage_size, product.description, product.price, product.currency, product.add_time, tablet.image
                     FROM product JOIN tablet ON product.id = tablet.id  WHERE tablet.ram = {parameters['ram']} AND  product.brand = '{parameters['brand']}' AND '''
        # generates the sql call for filter function
        if 'processor' in keys:
            filter += f"tablet.processor = '{parameters['processor']}' AND "
        if 'storage_size' in keys:
            if parameters['storage_size'] == '<64':
                filter += f"tablet.storage_size <64 AND "
            elif parameters['storage_size'] == '>512':
                filter += f"tablet.storage_size > 512 AND "
            elif parameters['storage_size'] == '128-256':
                filter += f"tablet.storage_size in (128, 256) AND "
        if 'screen_size' in keys:
            if parameters['screen_size'] == '<10':
                filter += f"tablet.display_size <= 10 AND "
            if parameters['screen_size'] == '10`-12`':
                filter += f"tablet.display_size >10 AND tablet.display_size <12 AND "
            if parameters['screen_size'] == '>12':
                filter += f"tablet.display_size >= 12 AND "
        if 'screen_quality' in keys:
            if parameters['screen_quality'] == 'Standard':
                filter += f"tablet.display_quality in ('HD', 'Full HD') AND "
            elif parameters['screen_quality'] == 'Good':
                filter += f"tablet.display_quality in ('Quad HD', '2K') AND "
            elif parameters['screen_quality'] == 'Premium':
                filter += f"tablet.display_quality in ('3K', '4K') AND "
        cursor.execute(filter[:-5])
        objects = cursor.fetchall()
        for object in objects:
            # appends to output tablets
            output.append(Tablet(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4], processor=object[5], ram=object[6], battery=object[7], display_size=object[8], display_quality=object[9], network=object[10], storage=object[11], description=object[12],price=object[13], currency=object[14], add_time=object[15], image=object[16]))
        return output
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


def filter_smartphone(parameters):
    """

        :param parameters: parameters set through filter menu
        :return: list of items that passed the filter

    """
    try:
        keys = parameters.keys()
        output=[]
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        filter = f'''SELECT product.category, product.id, product.name, product.brand, product.model, smartphone.processor, smartphone.ram, smartphone.display_size, smartphone.display_quality, smartphone.dual_sim, smartphone.storage_size, smartphone.battery, product.description, product.price, product.currency, product.add_time, smartphone.image
                     FROM product JOIN smartphone ON product.id = smartphone.id  WHERE smartphone.ram = {parameters['ram']} AND  product.brand = '{parameters['brand']}' AND '''
        # generates the sql call for filter function
        if 'processor' in keys:
            filter += f"smartphone.processor = '{parameters['processor']}' AND "
        if 'storage_size' in keys:
            if parameters['storage_size'] == '<64':
                filter += f"smartphone.storage_size <64 AND "
            elif parameters['storage_size'] == '>512':
                filter += f"smartphone.storage_size > 512 AND "
            elif parameters['storage_size'] == '128-256':
                filter += f"smartphone.storage_size in (128, 256) AND "
        if 'screen_size' in keys:
            if parameters['screen_size'] == '<5`':
                filter += f"smartphone.display_size <= 5 AND "
            if parameters['screen_size'] == '5`-6`':
                filter += f"smartphone.display_size >5 AND smartphone.display_size <6 AND "
            if parameters['screen_size'] == '>6`':
                filter += f"smartphone.display_size >= 6 AND "
        if 'screen_quality' in keys:
            if parameters['screen_quality'] == 'Standard':
                filter += f"smartphone.display_quality in ('HD', 'Full HD') AND "
            elif parameters['screen_quality'] == 'Good':
                filter += f"smartphone.display_quality in ('Quad HD', '2K') AND "
            elif parameters['screen_quality'] == 'Premium':
                filter += f"smartphone.display_quality in ('3K', '4K') AND "
        cursor.execute(filter[:-5])
        objects = cursor.fetchall()
        for object in objects:
            # appends to output smartphones
            output.append(Smartphone(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4], processor=object[5], ram=object[6], battery=object[11], display_size=object[7], display_quality=object[8], storage=object[10], double_sim=object[9], description=object[12], price=object[13], currency=object[14], add_time=object[15], image=object[16]))
        return output
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


def basket(user_id):
    """

        :param user_id: id of a user with certain basket
        :return: all products from users basket

    """
    try:
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        cursor.execute(f'SELECT category, product FROM basket WHERE user = \'{user_id}\';')
        basket = cursor.fetchall()
        out = []
        for data in basket:
            if data[0] == 1:
                command = f'''SELECT product.category, product.id, product.name, product.brand, product.model, laptop.processor, laptop.ram, laptop.display_size, laptop.display_quality, laptop.ssd, laptop.storage_size, laptop.graphics, laptop.vram, product.description, product.price, product.currency, product.add_time, laptop.image
                                  FROM product JOIN laptop ON product.id = laptop.id WHERE product.id = '{data[1]}' '''
                cursor.execute(command)
                object = cursor.fetchall()[0]
                # creates products of certain class and assigns to output
                out.append(Laptop(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4],
                                  processor=object[5], ram=object[6], display_size=object[7], display_quality=object[8],
                                  ssd=object[9], storage=object[10], graphics=object[11], vram=object[12],
                                  description=object[13], price=object[14], currency=object[15], add_time=object[16],
                                  image=object[17]))
            elif data[0] == 2:
                cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, tablet.processor, tablet.ram, tablet.battery, tablet.display_size, tablet.display_quality, tablet.network, tablet.storage_size, product.description, product.price, product.currency, product.add_time, tablet.image
                                       FROM product JOIN tablet ON product.id = tablet.id  WHERE product.id = '{data[1]}' ''')
                object = cursor.fetchall()[0]
                # creates products of certain class and assigns to output
                out.append(
                    Tablet(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4],
                           processor=object[5], ram=object[6], battery=object[7], display_size=object[8],
                           display_quality=object[9], network=object[10], storage=object[11], description=object[12],
                           price=object[13], currency=object[14], add_time=object[15], image=object[16]))

            elif data[0] == 3:
                cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, smartphone.processor, smartphone.ram, smartphone.display_size, smartphone.display_quality, smartphone.dual_sim, smartphone.storage_size, smartphone.battery, product.description, product.price, product.currency, product.add_time, smartphone.image
                                       FROM product JOIN smartphone ON product.id = smartphone.id  WHERE product.id = '{data[1]}' ''')
                object = cursor.fetchall()[0]
                # creates products of certain class and assigns to output
                out.append(
                    Smartphone(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4],
                               processor=object[5], ram=object[6], battery=object[11], display_size=object[7],
                               display_quality=object[8], storage=object[10], double_sim=object[9],
                               description=object[12], price=object[13], currency=object[14], add_time=object[15],
                               image=object[16]))
        return out
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


def add_to_basket(user_id, product_id, product_category):
    """
            :param user_id: user id
            :param product_id: product id
            :param product_category: product category
            :return: adds product to table basket from database
        """
    try:
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        add_to_basket = f'''INSERT INTO basket VALUES (\'{user_id}\', \'{product_id}\', {product_category});'''
        cursor.execute(add_to_basket)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if connection:
            cursor.close()
            connection.close()


def finish_purchase(user):
    """
        :param user: user id
        :return: deletes basket of this user, finish shopping
    """
    try:  # works only if email is unique
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        delete_basket = f'''DELETE FROM basket WHERE user = \'{user}\';'''
        cursor.execute(delete_basket)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if connection:
            cursor.close()
            connection.close()


def add_review(product_id, grade, review):
    """
            :param product_id: product id
            :param grade: product grade
            :param review: product review
            :return: adds review
        """
    try:
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        add_review = f'''INSERT INTO review VALUES ("{product_id}", "{grade}", "{review}");'''
        cursor.execute(add_review)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if connection:
            cursor.close()
            connection.close()


def see_reviews(product_id):
    try:
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        get_reviews = f'''SELECT grade, description FROM review WHERE id = \'{product_id}\';'''
        cursor.execute(get_reviews)
        out = cursor.fetchall()
        connection.commit()
        return out
    except sqlite3.Error as e:
        print(e)
    finally:
        if connection:
            cursor.close()
            connection.close()
