import datetime


class User:

    def __init__(self, _id, name, email, password):
        self.id = _id
        self.name = name
        self.email = email
        self.password = password
        self.join_date = datetime.now()
        self.basket = None

    def assign_basket(self, basket):
        self.basket = basket
        basket.buyer_id = self.id
