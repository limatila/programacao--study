from fcts1 import say_hi, endCode, tspac
from usersClass import Users
#from usersSecondClass import Users

#atributes: name, age, time of use(h), rating
user1 = Users("Atila", 17, 617.8, "gold 4")
user2 = Users("Well", 17, 80.4, "bronze 3")
user3 = Users("Yume", 17, 1249, "silver 3")
user4 = Users("Marx", 17, 1200, "bronze 1")
user5 = Users("Evolutionz", 20, 1470, "diamond 4")

#check minority
def checkAge(user):
    if user.age >= 18:
        print(f"{user.name} is not a minor")
    else:
        print(f"{user.name} is a minor")

#check of everyone
usersPawn = [user1, user2, user3, user4, user5]
for i in usersPawn:
    checkAge(i)

tspac()
print(user1.soma())
#soma time of use + age


tspac()
print(user1.soma())
print(user1.subs())

endCode()