class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hello, my name is", self.name, ", I am", self.age, "years of age and definitely", self.gender, "=).")

# an instance of the Person class
person1 = Person("Felly", 20, "female")

# Call the introduce method to display the person's information
person1.introduce()
