import datetime
import uuid


class Laptop:

    def __init__(self, name, price, brand, processor, display_size, display_quality, ram, storage_type, storage_size,
                 video_card_type, video_card_memory, color):
        self.category = 1
        self.name = name
        self.id = uuid.uuid1()
        self.price = price
        self.brand = brand
        self.processor = processor
        self.display_size = display_size
        self.display_quality = display_quality
        self.ram = ram
        self.storage_type = storage_type
        self.storage_size = storage_size
        self.video_card_type = video_card_type
        self.video_card_memory = video_card_memory
        self.color = color
        self.time_od_adding = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

