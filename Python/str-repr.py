class footballer:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"Footballer: {self.name} {self.surname} Age: {self.age}"
    def __repr__(self):
        return f'Footballer"{self.name}"," Suurname: " {self.surname}", Age: {self.age})'

footballer1 = footballer("Lionel", "Messi", 36)

print(footballer1)
print(repr(footballer1))


