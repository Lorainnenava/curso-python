menu = ["expresso", "moca", "latte", "capuccino", "cortado", "americano"]

example = [{"identificador": 1, "name": "ab", "status": 1},
           {"identificador": 2, "name": "cd", "status": 1}, {"identificador": 3, "name": "cd", "status": 2}]

status_1 = [item for item in example if item["status"] == 1]
print(status_1)


def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee


map_coffee = map(find_coffee, menu)

for x in map_coffee:
    print(x)


def filter_coffee(coffee):
    if coffee == "c":
        return coffee


filter_coffee = filter(filter_coffee, menu)
for x in filter_coffee:
    print(x)
