class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("I am animal")

class Mammal(Animal):
    def __init__(self,name,feature):
        super().__init__(name)
        self.feature=feature
    def speak(self):
        print("I am mammal")

class Bird(Animal):
    def __init__(self,name,feature):
        super().__init__(name)
        self.feature=feature
    def speak(self):
        print("I am a bird")

class Fish(Animal):
    def __init__(self,name,feature):
        super().__init__(name)
        self.feature=feature
    def speak(self):
        print("I am a fish")

class Dog(Mammal):
    def __init__(self,name,feature):
        super().__init__(name,feature)
    def walk(self):
        print("woof!","I am",self.name,"I",self.feature,"I can walk")

class Cat(Mammal):
    def __init__(self,name,feature):
        super().__init__(name,feature)
    def walk(self):
        print("meow!","I am",self.name,"I",self.feature,"I can walk")
    
class Eagle(Bird):
    def __init__(self,name,feature):
        super().__init__(name,feature)
    def fly(self):
        print("I am",self.name,"I",self.feature,"I can fly")

class Penguin(Bird):
    def __init__(self,name,feature):
        super().__init__(name,feature)
    def swim(self):
        print("I am",self.name,"I",self.feature,"I swim")

class Shark(Fish):
    def __init__(self,name,feature):
        super().__init__(name,feature)
    def swim(self):
        print("I am",self.name,"I",self.feature,"I swim")

class Salmon(Fish):
    def __init__(self,name,feature):
        super().__init__(name,feature)
    def swim(self):
        print("I am",self.name,"I",self.feature,"I swim")

def main():
    #create instance of classes
    dog1= Dog("Sisimanu","have furs")        
    cat1= Cat("kiyo","have furs")
    penguin1= Penguin("Murphy","have little legs")
    eagle1= Eagle("Gummy","have big eyes")
    salmon= Salmon("Tanky","have good meat")
    shark1= Shark("Zig","have big horn")

    #see how the object of subclass overide the function of its superclass
    dog1.walk()
    cat1.walk()
    penguin1.swim()
    eagle1.fly()
    salmon.swim()
    shark1.swim()

if __name__== "__main__":
    main()