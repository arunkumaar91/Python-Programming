class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor is called")
        self.lastName = last_name
        self.eyeColor = eye_color

    def show_info(self):
        print("Last Name: " +self.lastName)
        print("Eye Color: " +self.eyeColor)
    
class Child(Parent):
    def __init__(self, last_name, eye_color, no_of_toys):
        print("Child Constructor is called")
        Parent.__init__(self, last_name, eye_color)
        self.noOfToys = no_of_toys

    def show_info(self):
        print("Last Name: " +self.lastName)
        print("Eye Color: " +self.eyeColor)
        print("No of Toys: " +str(self.noOfToys))

#sarav_ramachandran = Parent("Saravanen", "brown")

#sarav_ramachandran.show_info()
#print(sarav_ramachandran.lastName)

arunkumaar_sarav = Child("Saravanen", "brown", 5)
arunkumaar_sarav.show_info()

#print(arunkumaar_sarav.lastName)
#print(arunkumaar_sarav.noOfToys)
