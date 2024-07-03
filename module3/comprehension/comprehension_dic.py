# dict = { key:value for key, value in <sequence> if <condition> } sintaxis
# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)

#Nótese como en el caso de utilizar dos listas, el formato que sigue es: 
# new_dict ={key:value for (key, value) in zip(list1, list2)}

#Aquí he utilizado la función zip que combina las dos listas. Cuando las dos listas son de longitud diferente,
#la longitud de la lista más corta es la longitud del diccionario.