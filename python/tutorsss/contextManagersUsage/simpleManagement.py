
# Imagine a system that manages personal information, and you'll enter an account.
# While youre in there, you want to make sure the account remains open for the duration of the usage.

class person_manager():
    def __init__(self, passwordEntry: str) -> 'person_manager':
        self.password: str = "123456"
        
        if passwordEntry == self.password: #Authentication
            self.name: str = "atila"
            self.age: int = 20
        else: 
            print("wrong password, ending entrance")
            return None

    def __enter__(self):
        print("Logging into account information")
        return self

    def __exit__(self, exc_type, exc_value, traceback): #Handling of errors on exit of with block
        print("Logging out, ending account") 
        #* In reality, it can be data from a DB, that wouldn't be deleted after closure...

    def isMature(self) -> str: # Can do some logics with the class
        if self.age >= 18:
            return (f"{self.name} is not a minor")

if __name__ == "__main__":
    #With correct password
    with person_manager("123456") as person:
        print(f"Hello, your name is {person.name}")
        print(person.isMature())