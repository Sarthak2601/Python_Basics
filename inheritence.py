class Mammal :
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f'{self.name} is walking')


class Dog(Mammal):
    def __init__(self,name):
        self.name = name


class Cat(Mammal):
    def __init__(self, name):
        self.name = name


dog1 = Dog("Judo")
dog1.walk()

cat1 = Cat("Kitty")
cat1.walk()