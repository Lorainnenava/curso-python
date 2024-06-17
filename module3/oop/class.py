class student:
    def into(self, name, lastName):
        return "My name is {} {}".format(name, lastName) # ejemplo con format
        return "My name is " + name + " " + lastName # ejemplo con +

instanceStudent= student()
value= instanceStudent.into("Lorainne", "Navarro")
print(value)