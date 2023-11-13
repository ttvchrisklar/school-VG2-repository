# lerning how to use classes.

class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

print("waht is youre name and age?")
name = input("name: " )
age = input("age: " )
a = int(age)

p1 = myclass(name,a)
print(p1.name)
print(p1.age)
