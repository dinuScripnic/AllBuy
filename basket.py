class Basket:

    def __init__(self, buyer_id):
        self.buyer_id = buyer_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)


# def show_basket():
#
