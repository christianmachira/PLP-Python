class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        print(f"My name is {self.name}, I am {self.age}, and I am a {self.gender}")
    
person1=person("Christian", 23, "Male")
person1.info()

