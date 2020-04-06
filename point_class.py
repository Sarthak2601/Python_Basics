class Point:
    def __init__(self,x,y):    # Constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10,20)
print(point1.x)

