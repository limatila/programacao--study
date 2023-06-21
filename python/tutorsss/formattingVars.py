from fcts0 import tspac; from datetime import datetime

myFloat = 13.57902918
myInt = 19512
myStr = "    ok     okboy! UWUsalvy28 lolecoisadecorno"

myPerson = {
    'name':'Atila',
    'age': 18,
    }

myPerson2 = {
    'name': 'Taina',
    'age': '17',
    }

print('his name is {0[name]}, and her age is {1[age]}'.format(myPerson, myPerson2)) #work with classes

print('ok im printing this name: {name}'.format(name=myPerson['name']))

tspac()
print('{:.2f}'.format(myFloat))
print("ok {:010}".format(myInt,))#vai adicionar 0 à esquerda, pelo total de vezes(depois de 0: 20)
print("")
print('mixed up:{:050.3f}'.format(myFloat))#adding 0s and rounding the last 3 digits
print('changing the separators:{:,}'.format(2000**4))
myFloat2 = myFloat * 100 #for the next operation
print('changing and rounding floats:{:,.2f}'.format(myFloat2)) 
print('all mixed up: {:020,.2f}'.format(myFloat2))

tspac()
print(round(myFloat))

tspac()
t = datetime.now() #for library, check the docs
print(t) #my date to format

print('only month(extense)/date, hour/minute:   {:%B %d, %H:%M}'.format(t)) #only the first ':' is interpreted to the code functioning
print('only dayfromtheyear, day of the week, timezone, and some microseconds: \
 {:%j days have passed, %u(1 is monday), %Z(if empty, objs. is naive), %f}'.format(t))

microseconds = float(('{:%f}'.format(t)))
microseconds = float('{:.2f}'.format(microseconds))
microseconds = microseconds/1000
Intsecs = int('{:%S}'.format(t))
sAndMicro = ('{:},{:.2f}'.format(Intsecs, microseconds)) #nao consigo mudar a virgula no display??
print('')
print(sAndMicro + '  is the seconds and microseconds')


