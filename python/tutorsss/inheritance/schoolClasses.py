from locale import setlocale, LC_ALL, strxfrm #*For use in sorting arrays of strings in Portuguese-BR
from datetime import date
from random import randint

setlocale(LC_ALL, 'pt_BR.UTF-8')

class schoolClass:
    def __init__(self, name: str, capacity: int, active = True) -> None:
        self.name = name
        self.capacity = capacity
        self.active = active #Default
        
        self.studentsInClass: list['Student'] = [] # 'Student' pois a classe não foi definida antes da linha 4

    def __str__(self) -> str: #* Double Underscore methods (DunderMethods, for short)
        return f"Classe de {self.name}"

    def getActive(self) -> bool:
        return self.active
    
    def subscribeStudent(self, student: 'Student') -> None:
        if len(self.studentsInClass) < self.capacity:
            self.studentsInClass.append(student)
            self.studentsInClass = sorted(self.studentsInClass, key = lambda student: strxfrm(student.name)) #* Resorting every time, not very eficcient
        else:
            print("The class is full! Aborting...")
        
    def getStudentsNumber(self) -> int:
        return len(self.studentsInClass)
    
    def getStudent(self, desiredName: str) -> 'Student':
        for student in self.studentsInClass:
            if student.name == desiredName:
                return student


class Student:
    def __init__(self, name: str, age: int, subscribedClass: schoolClass, active: bool = True) -> None:
        self.name = name
        self.age = age
        self.active = active #Default

        if(subscribedClass.getActive() == True):
            subscribedClass.subscribeStudent(self)
            self.subscribedClass = subscribedClass
        else: 
            print("The class is not active! Aborting...")
        self.testsAttended: list['Test'] = []

    def __str__(self) -> str:
        return f"{self.name}, atualmente aluno de {self.subscribedClass.name}"

    def getActive(self) -> bool:
        return self.active
    
    def deactivate(self) -> None:
        if self.active == True:
            self.active = False
            self.subscribedClass = None
        else:
            print("The student is already inactive")
    
    def reactivate(self) -> None:
        if self.active == False:
            self.active = True
        else:
            print("The student is already active")

    def study(self) -> None:
        if self.active == True and type(self.subscribedClass) == schoolClass:
            print("Studying...")
            #do something here...
        else:
            print("The student is inactive! aborting...")

    def attendTest(self) -> None:
        if self.active == True and type(self.subscribedClass) == schoolClass:
            newTest: 'Test' = Test(f"Teste {len(self.testsAttended) + 1}", self.subscribedClass, self)
            newTest.finish()
            self.testsAttended.append(newTest)
        else:
            print("The student is inactive! aborting...")
        

class Test:

    def __init__(self, name: str, classApplied: schoolClass, student: Student) -> None:
        self.name = name
        self.classApplied = classApplied
        self.student = student

        self.dateFinished: str = None
        self.grade: int = None #Default
    
    def __add__(self, other: 'Test') -> None:
        return self.grade + other
    
    def __radd__(self, other: 'Test') -> None:
        return other + self.grade
    
    def finish(self) -> None:
        self.grade = randint(0, 10) #Completely random integer ;)
        self.dateFinished = (
            date.today().strftime("%d/%m/%Y")
        )
    
    
        

#Manual test
if __name__ == "__main__":
    class1 = schoolClass("Matemática", 45)
    Student("Marx", 18, class1)
    Student("Cristiano", 21, class1)
    Student("Joaquim", 22, class1) #Subscribing some 'filler' students

    student1: Student = Student("Átila", 19, class1)
    print(class1.getStudent("Átila"))

    student1.study()
    student1.study()

    student1.attendTest()
    student1.attendTest()
    student1.attendTest()

    #* getting the Mean of all the tests made till now:
    total: int = 0
    for test in student1.testsAttended:
        total += test
    print(f"Mean: {total / len(student1.testsAttended)}")
    