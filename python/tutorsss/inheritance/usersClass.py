
class Users():
    def __init__(self, name, age, timuse, rating):
        self.name = name
        self.age = age
        self.timuse = timuse
        self.rating = rating

    def soma(self):
        valor = self.timuse + self.age
        return valor
    