import datetime
import uuid


class Product:

    def __init__(self, name, brand, model, description, price, currency, _id=uuid.uuid1(),
                 add_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self._id = _id
        self.name = name
        self.brand = brand
        self.model = model
        self.description = description
        self.price = price
        self.currency = currency
        self.add_time = add_time


class Laptop(Product):

    def __init__(self, name, brand, model, processor, ram, display_size, display_quality, ssd, storage, graphics, vram,
                 description, price, currency, _id=uuid.uuid1(), add_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self.__init__(name, brand, model, description, price, currency, _id=uuid.uuid1(),
                      add_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self._id = _id
        self.name = name
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.display_size = display_size
        self.display_quality = display_quality
        self.ssd = ssd
        self.storage = storage
        self.graphics = graphics
        self.vram = vram
        self.description = description
        self.price = price
        self.currency = currency
        self.add_time = add_time


class Tablet(Product):

    def __init__(self, name, brand, model, processor, ram, battery, storage,  display_size, display_quality, network,
                 description, price, currency, _id=uuid.uuid1(), add_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self.__init__(name, brand, model, description, price, currency, _id=uuid.uuid1(),
                      add_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self._id = _id
        self.name = name
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.battery = battery
        self.storage = storage
        self.display_size = display_size
        self.display_quality = display_quality
        self.network = network
        self.description = description
        self.price = price
        self.currency = currency
        self.add_time = add_time


class Smartphone(Product):

    def __init__(self, name, brand, model, processor, ram, battery, storage,  display_size, display_quality, double_sim,
                 description, price, currency, _id=uuid.uuid1(), add_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self.__init__(name, brand, model, description, price, currency, _id=uuid.uuid1(),
                      add_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self._id = _id
        self.name = name
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.battery = battery
        self.storage = storage
        self.display_size = display_size
        self.display_quality = display_quality
        self.double_sim = double_sim
        self.description = description
        self.price = price
        self.currency = currency
        self.add_time = add_time
