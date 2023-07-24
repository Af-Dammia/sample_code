import math
class MyFirstClass:
    def reset(self):
        self.x=0
        self.y=0
a=MyFirstClass()
a.x=2
a.y=4
#a.reset()
MyFirstClass.reset(a)
print(a.x,a.y)
#print(a.reset())
class Point:
    def move(self,x,y):
        self.x=x
        self.y=y
    def reset(self):
        self.move(0,0)
    def calculate_distance(self,other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

p1=Point()
p2=Point()
p1.move(2,6)
p2.move(5,9)
print(p2.calculate_distance(p1))
assert(p2.calculate_distance(p1))==(p1.calculate_distance(p2))
p1.move(3,40)
print(p1.calculate_distance(p2))
print(p2.calculate_distance(p1))
