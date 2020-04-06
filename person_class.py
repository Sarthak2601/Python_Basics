class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi {self.name}! Let's talk. ")


person1 = Person("Sarthak")
print(person1.name)
person1.talk()