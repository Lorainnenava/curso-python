file = open("test.txt", "r")

data = file.readline()

print(data)

file.close()


# Ejemplo
with open("test.txt", "r") as file:
    data = file.readline()

    print(data)
