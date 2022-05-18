from user import User
import sqlite3
import os.path
import PySimpleGUI as sg
from categories import *


def check_db():  # creates the dummy database if it doesn't exist
    if not os.path.exists('AllBuy.db'):
        connection = sqlite3.connect('AllBuy.db')
        cursor = connection.cursor()
        create_workspace = '''CREATE TABLE costumers(
                                costumer_id VARCHAR(40) PRIMARY KEY,
                                costumer_name VARCHAR(255) NOT NULL,
                                costumer_email VARCHAR(255) UNIQUE NOT NULL ,
                                costumer_password VARCHAR(16) NOT NULL,
                                join_date TIMESTAMP
                              );
                              CREATE TABLE product (
                                  category INTEGER,
                                  id VARCHAR(40) PRIMARY KEY,
                                  name VARCHAR(255),
                                  brand VARCHAR(255),
                                  model VARCHAR(255),
                                  description VARCHAR(4000),
                                  price INTEGER,
                                  currency VARCHAR(1),
                                  add_time TIMESTAMP
                              );
                              CREATE TABLE laptop(
                                  id VARCHAR(40) PRIMARY KEY,
                                  processor VARCHAR(255),
                                  ram INTEGER,
                                  display_size FLOAT,
                                  display_quality VARCHAR(255),
                                  ssd BOOLEAN,
                                  storage_size INTEGER,
                                  graphics BOOLEAN,
                                  vram INTEGER,
                                  FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE
                              );
                              CREATE TABLE tablet(
                                  id VARCHAR(40) PRIMARY KEY,
                                  processor VARCHAR(255),
                                  ram INTEGER,
                                  display_size FLOAT,
                                  display_quality VARCHAR(255),
                                  network BOOLEAN,
                                  storage_size INTEGER,
                                  battery INTEGER,
                                  FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE
                              );
                              CREATE TABLE smartphone(
                                  id VARCHAR(40) PRIMARY KEY,
                                  processor VARCHAR(255),
                                  ram INTEGER,
                                  display_size FLOAT,
                                  display_quality VARCHAR(255),
                                  dual_sim BOOLEAN,
                                  storage_size INTEGER,
                                  battery INTEGER,
                                  FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE
                              );
                              CREATE TABLE review(
                                  id VARCHAR(40) PRIMARY KEY,
                                  grade FLOAT,
                                  description VARCHAR(4000),
                                  FOREIGN KEY (id) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE
                              );
                              CREATE TABLE basket(
                                  user VARCHAR(40),
                                  product VARCHAR(40),
                                  FOREIGN KEY (user) REFERENCES costumers(id) on DELETE CASCADE on UPDATE CASCADE
                                  FOREIGN KEY (product) REFERENCES product(id) on DELETE CASCADE on UPDATE CASCADE
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
        cursor = connection.cursor()
        add_user = f''' INSERT INTO costumers(costumer_id, costumer_name, costumer_email, costumer_password, join_date) 
                      VALUES ('{user.id}', '{user.name}', '{user.email}', '{user.password}', '{user.join_date}');'''
        cursor.execute(add_user)
        connection.commit()
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
        add = f''' INSERT INTO product VALUES ({laptop.category}, '{laptop._id}', '{laptop.name}', '{laptop.brand}', '{laptop.model}', '{laptop.description}', {laptop.price}, '{laptop.currency}', '{laptop.add_time}');'''
        cursor.execute(add)
        add = f'''INSERT INTO laptop VALUES ('{laptop._id}', '{laptop.processor}', {laptop.ram}, {laptop.display_size}, '{laptop.display_quality}', {laptop.ssd}, {laptop.storage}, {laptop.graphics}, {laptop.vram}); '''
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
        add = f''' INSERT INTO product VALUES ({tablet.category}, '{tablet._id}', '{tablet.name}', '{tablet.brand}', '{tablet.model}', '{tablet.description}', {tablet.price}, '{tablet.currency}', '{tablet.add_time}');'''
        cursor.execute(add)
        add = f'''INSERT INTO tablet VALUES ('{tablet._id}', '{tablet.processor}', {tablet.ram}, {tablet.display_size}, '{tablet.display_quality}', {tablet.network}, {tablet.storage}, {tablet.battery});'''
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
        add = f''' INSERT INTO product VALUES ({smartphone.category}, '{smartphone._id}', '{smartphone.name}', '{smartphone.brand}', '{smartphone.model}', '{smartphone.description}', {smartphone.price}, '{smartphone.currency}', '{smartphone.add_time}');'''
        cursor.execute(add)
        add = f'''INSERT INTO smartphone VALUES ('{smartphone._id}', '{smartphone.processor}', {smartphone.ram}, {smartphone.display_size}, '{smartphone.display_quality}', {smartphone.double_sim}, {smartphone.storage}, {smartphone.battery}); '''
        cursor.execute(add)
        connection.commit()
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


def get_all_products():
    try:
        connection = sqlite3.connect('AllBuy.db')
        output = []
        cursor = connection.cursor()
        cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, laptop.processor, laptop.ram, laptop.display_size, laptop.display_quality, laptop.ssd, laptop.storage_size, laptop.graphics, laptop.vram, product.description, product.price, product.currency, product.add_time
                from product JOIN laptop ON product.id = laptop.id''')
        product_data = cursor.fetchall()  # searches for products
        for object in product_data:
            output.append(Tablet(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4], processor=object[5], ram=object[6], battery=object[7], display_size=object[8], display_quality=object[9], network=object[10], storage=object[11], description=object[12],price=object[13], currency=object[14], add_time=object[15]))
        cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, tablet.processor, tablet.ram, tablet.battery, tablet.display_size, tablet.display_quality, tablet.network, tablet.storage_size, product.description, product.price, product.currency, product.add_time
        from product JOIN tablet ON product.id = tablet.id''')
        product_data = cursor.fetchall()  # searches for products
        for object in product_data:
            output.append(Tablet(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4], processor=object[5], ram=object[6], battery=object[7], display_size=object[8], display_quality=object[9], network=object[10], storage=object[11], description=object[12],price=object[13], currency=object[14], add_time=object[15]))
        cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, smartphone.processor, smartphone.ram, smartphone.display_size, smartphone.display_quality, smartphone.dual_sim, smartphone.storage_size, smartphone.battery, product.description, product.price, product.currency, product.add_time
        from product JOIN smartphone ON product.id = smartphone.id''')
        product_data = cursor.fetchall()  # searches for products
        for object in product_data:
            output.append(Smartphone(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4], processor=object[5], ram=object[6], battery=object[11], display_size=object[7], display_quality=object[8], storage=object[10], double_sim=object[9], description=object[12], price=object[13], currency=object[14], add_time=object[15]))
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
        product_data = cursor.fetchall()  # searches for products
        out = []
        for data in product_data:
            if data[0] == 1:
                command = f'''SELECT product.category, product.id, product.name, product.brand, product.model, laptop.processor, laptop.ram, laptop.display_size, laptop.display_quality, laptop.ssd, laptop.storage_size, laptop.graphics, laptop.vram, product.description, product.price, product.currency, product.add_time
                from product JOIN laptop ON product.id = laptop.id  WHERE product.id = '{data[1]}' '''
                cursor.execute(command)
                object = cursor.fetchall()
                out.append(
                        Laptop(object[2], object[3], object[4], object[5], object[6], object[7], object[8], object[9],
                               object[10], object[11], object[12], object[13], object[14], object[15], object[1],
                               object[16], object[0]))

            elif data[0] == 2:
                cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, tablet.processor, tablet.ram, tablet.battery, tablet.display_size, tablet.display_quality, tablet.network, tablet.storage_size, product.description, product.price, product.currency, product.add_time
        from product JOIN tablet ON product.id = tablet.id  WHERE product.id = '{data[1]}' ''')
                object = cursor.fetchall()[0]
                out.append(
                    Tablet(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4],
                           processor=object[5], ram=object[6], battery=object[7], display_size=object[8],
                           display_quality=object[9], network=object[10], storage=object[11], description=object[12],
                           price=object[13], currency=object[14], add_time=object[15]))

            elif data[0] == 3:
                cursor.execute(f'''SELECT product.category, product.id, product.name, product.brand, product.model, smartphone.processor, smartphone.ram, smartphone.display_size, smartphone.display_quality, smartphone.dual_sim, smartphone.storage_size, smartphone.battery, product.description, product.price, product.currency, product.add_time
        from product JOIN smartphone ON product.id = smartphone.id  WHERE product.id = '{data[1]}' ''')
                object = cursor.fetchall()[0]
                out.append(
                    Smartphone(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4],
                               processor=object[5], ram=object[6], battery=object[11], display_size=object[7],
                               display_quality=object[8], storage=object[10], double_sim=object[9],
                               description=object[12], price=object[13], currency=object[14], add_time=object[15]))
        print(out)
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
        filter = f'''SELECT product.category, product.id, product.name, product.brand, product.model, laptop.processor, laptop.ram, laptop.display_size, laptop.display_quality, laptop.ssd, laptop.storage_size, laptop.graphics, laptop.vram, product.description, product.price, product.currency, product.add_time 
        FROM product JOIN laptop ON product.id = laptop.id 
        WHERE laptop.ram = {parameters['ram']} AND '''
        if 'brand' in keys:
            filter += f"product.brand = '{parameters['brand']}' AND "
        if 'processor' in keys:
            filter += f"tablet.processor = '{parameters['processor']}' AND "
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
            out.append(Laptop(object[2], object[3], object[4], object[5], object[6], object[7], object[8], object[9], object[10], object[11], object[12], object[13], object[14], object[15],object[1], object[16], object[0]))
        print(out)
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
        filter = f'''SELECT product.category, product.id, product.name, product.brand, product.model, tablet.processor, tablet.ram, tablet.battery, tablet.display_size, tablet.display_quality, tablet.network, tablet.storage_size, product.description, product.price, product.currency, product.add_time
        from product JOIN tablet ON product.id = tablet.id  WHERE tablet.ram = {parameters['ram']} AND  product.brand = '{parameters['brand']}' AND '''
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
            output.append(Tablet(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4], processor=object[5], ram=object[6], battery=object[7], display_size=object[8], display_quality=object[9], network=object[10], storage=object[11], description=object[12],price=object[13], currency=object[14], add_time=object[15]))
        print(output)
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
        filter = f'''SELECT product.category, product.id, product.name, product.brand, product.model, smartphone.processor, smartphone.ram, smartphone.display_size, smartphone.display_quality, smartphone.dual_sim, smartphone.storage_size, smartphone.battery, product.description, product.price, product.currency, product.add_time
        from product JOIN smartphone ON product.id = smartphone.id  WHERE smartphone.ram = {parameters['ram']} AND  product.brand = '{parameters['brand']}' AND '''
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
            if parameters['screen_size'] == '>7`':
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
            output.append(Smartphone(category=object[0], _id=object[1], name=object[2], brand=object[3], model=object[4], processor=object[5], ram=object[6], battery=object[11], display_size=object[7], display_quality=object[8], storage=object[10], double_sim=object[9], description=object[12], price=object[13], currency=object[14], add_time=object[15]))
        print(output)
        return output
    except sqlite3.Error as er:
        print(f'Error: {er}')
    finally:
        if connection:
            cursor.close()
            connection.close()


# add review
# add to basket


