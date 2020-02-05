from typing import List, Dict
from models import Person, Order,str_to_dict



def print_all(mylist) -> None:
    for item in mylist:
        print(item)

person = Person()
person.name = "Ольга Охманюк"
person.email = "ohmanyukov@mail.ru"
person.phone = "+79246432292"
person.is_customer = True

str1 = "email=ohmanyukov@mail.ru;id=None; is_customer=True; is_performer=None; name=Ольга Охманюк; phone=+79246432292"
result_dict = str_to_dict(str1)
print(result_dict)

person2 = Person.from_string(str1)
print(person2)


