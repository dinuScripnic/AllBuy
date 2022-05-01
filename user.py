import datetime
import uuid


class User:

    def __init__(self, name, email, password):
        self.id = str(uuid.uuid1())
        self.name = name
        self.email = email
        self.password = password
        self.join_date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        self.basket = None
        self.selling = None

    def assign_basket(self, basket):
        self.basket = basket
        basket.buyer_id = self.id
