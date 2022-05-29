import datetime
import uuid


class User:

    def __init__(self, name, email, password, _id=str(uuid.uuid1()),
                 join_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self.id = _id
        self.name = name
        self.email = email
        self.password = password
        self.join_date = join_date
