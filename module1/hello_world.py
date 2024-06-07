print("hello world")

name= "Lorainne"

if name == "Lorainne":
    print(name) #Lorainne

# --- ESPACIADOS ---
y = 1  +  2
print(y) #3

# incorrecto
x = 1 
+ 2
print(x) #1

f= 1 \
+ 2
print(f) #3

# SANGRIA
def say_hello():
    print("Hello there!")

print(say_hello())

myName= "Lorainne"
print(type(myName))

del myName # Elimina la variable
print(myName)

a= "hola"
b= "como estas"
print(a + b)

print(6**2)
a=True
print(not a)

print(3 * "hola")

array=[1, 2, 3]
for xd, i in enumerate(array):
    print(xd,i)