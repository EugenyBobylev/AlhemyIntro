import json
from models import Person, Order
from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)

person = Person()
person.name = "Ольга Охманюк"
person.email = "ohmanyukov@mail.ru"
person.phone = "+79246432292"
person.is_customer = True
json_str = json.dumps(person, cls=AlchemyEncoder)
print(json_str)

person2 = Person.from_json(json_str)
print(person2)

