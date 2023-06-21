from usersClass import Users
class VipUsers(Users):
    ''' já tomou overwrite: 
    def __init__(self, name, age, timuse, rating):
        self.name = name
        self.age = age
        self.timuse = timuse
        self.rating = rating
'''
#o de cima foi adicionado, porem toma overwrite

    def subs(self):
        valor = self.timuse - self.age
        return valor
    