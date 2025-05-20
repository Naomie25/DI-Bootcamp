from datetime import datetime, date

class Person:
    def __init__(self, name, last_name, birth_date):
        self.name = self.format_name(name)
        self.last_name = self.format_name(last_name)
        self.birth_date = self.parse_birthdate(birth_date)
    
    @classmethod
    def from_age(cls, name, age, last_name):
        age = int(age)
        current_year = datetime.today().year
        birth_year = current_year - age
        birth_date = f'{birth_year}-1-1'
        return cls(name, last_name, birth_date)

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return age

    @staticmethod
    def parse_birthdate(date_string):
        return datetime.strptime(date_string, '%Y-%m-%d').date()

    @staticmethod
    def format_name(s):
        return s.capitalize() if not s[0].isupper() else s
    
    def __str__(self):
        return f"{self.name} was born on {self.birthdate} \n age {self.age} "
    
    def __repr__(self):
        return f"{self.__dict__}"

# Test
p1 = Person("Alice", "Wonder", "1990-02-01")
print(p1.name)              # Alice
print(p1.last_name)         # Wonder
print(p1.age)               # e.g., 34 if current year is 2024

p2 = Person.from_age("Bob", 30, "Smith")
print(p2.birth_date)        # 1994-01-01 if current year is 2024

# Test lowercase name
p3 = Person.from_age("juliana", 35, "schmits")
print(p3.name)              # Juliana
print(p3.last_name)         # Schmits
str=p3.__str__
print(str)

print(p1.__repr__)

