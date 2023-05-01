class Animal:
    def __init__(self, name, age):
        self.name = name
        self. age = age
    
    def speak(self):
        print("울음소리")

class dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = "품종"

    def speak(self):
        print("멍멍")

class cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        print("야옹")
        
