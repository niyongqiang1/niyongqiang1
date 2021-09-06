#封装：父类Animal封装了变量和方法
class Animal():
    def run(self):
        print("主类动物在跑")
    def cs(self):
        print("主类第二个方法")
#继承：Dog子类继承父类Animal
class Dog(Animal):
    def run(self):
        #重写父类的方法        
        print("dog is runing")
    def cs(self):
        print("dog第二个方法")
#继承：Cat子类继承父类Animal
class Cat(Animal):
    #继承父类的方法
    def run(self):
        return super().run()
#继承 Tortoise子类继承父类Animal
class Tortoise(Animal):
    def run(self):
        print("Tortoise is running slowly")
    def cs(self):
        print("乌龟的第二个方法")
    def yy(self):
        return("乌龟的第三个方法")
dog = Dog()
# dog.run()

cat = Cat()
# cat.run()
tortoise = Tortoise()
print(isinstance(cat,Animal))
#定义一个函数，传入类并内部调用类函数
def print_animal(cs):
    cs.run()
    cs.run()
    cs.cs()
# print_animal(Animal())
# print_animal(cat)
print_animal(dog)
print(print_animal(tortoise))
print(tortoise.yy())
print(isinstance(cat,Animal))
print(type(tortoise.run()))
