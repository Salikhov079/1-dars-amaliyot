class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country


adr1 = Address("Bunyodkor 1-tor", "Chilonzor", "O'zbekiston")
adr2 = Address("Chilonzor 3-tor", "Toshkent", "O'zbekiston")

print(adr1.street, adr1.city, adr1.country)
print(adr2.street, adr2.city, adr2.country)


class Person:
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = self.set_age(age)
        self.email = self.set_email(email)
        self.phone = self.set_phone(phone)

    def set_age(self, age):
        if 0 > age:
            raise ValueError("Invalid yosh")
        return age
    
    def set_email(self, email):
        if not email.endswith("@gmail.com"):
            raise ValueError("Invalid email")
        return email
    
    def set_phone(self, phone):
        if len(phone) != 9 or not phone.isdigit():
            raise ValueError("Invalid nomer")
        return phone


    def __str__(self):
        return [self.name, self.age, self.email, self.phone]


per1 = Person("Najmiddin", 17, "najmiddin@gmail.com", "940791530")
per2 = Person("Samandar", 15, "samandar@gmail.com", "909990099")
per3 = Person(input(), int(input()), input(), input())

print(per1.__str__())
print(per2.__str__())
print(per3.__str__())

