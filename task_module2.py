menu = {
    1: {"name": "espresso", "price": 1.99},
    2: {"name": "coffee", "price": 2.50},
    3: {"name": "cake", "price": 2.79},
    4: {"name": "soup", "price": 4.50},
    5: {"name": "sandwich", "price": 4.99},
}

"""Calcula el subtotal de un pedido

    [IMPLÉMENTAME]
        1. Suma los precios de todos los artículos en el pedido y devuelve la suma.

    Argumentos:
        order: lista de diccionarios que contienen el nombre y precio de un artículo.

    Retorna:
        float = La suma de los precios de los artículos en el pedido.
    """


def calculate_subtotal(order):
    try:
        print("Calculating bill subtotal...")

        subtotal = sum(item['price'] for item in order)

        subtotal = round(subtotal, 2)

        return subtotal
    except:
        raise NotImplementedError()


"""Calcula el impuesto de un pedido

    [IMPLÉMENTAME]
        1. Multiplica el subtotal por el 15% y devuelve el producto redondeado a dos decimales.

    Argumentos:
        subtotal: el precio del cual se obtendrá el impuesto

    Retorna:
        float - El impuesto requerido de un subtotal dado, que es el 15% redondeado a dos decimales.
    """


def calculate_tax(subtotal):
    try:
        print("Calculating tax from subtotal...")

        tax = round(subtotal * 0.15, 2)

        return tax
    except:
        raise NotImplementedError()


"""Resume el pedido

    [IMPLÉMENTAME]
        1. Calcula el total (subtotal + impuesto) y guárdalo en una variable llamada total (redondeado a dos decimales).
        2. Guarda solo los nombres de todos los artículos en el pedido en una lista llamada names.
        3. Devuelve names y total.

    Argumentos:
        order: lista de diccionarios que contienen el nombre y precio de un artículo.

    Retorna:
        tupla de names y total. La instrucción de retorno debería verse así:

        return names, total

    """


def summarize_order(order):
    try:
        print(order)

        subtotal = calculate_subtotal(order)

        tax = calculate_tax(subtotal)

        total = round(subtotal + tax, 2)

        names = [item["name"] for item in order]

        return names, total
    except:
        raise NotImplementedError()


# This function is provided for you, and will print out the items in an order
def print_order(order):
    print("You have ordered " + str(len(order)) + " items")
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(
            f"{selection}. {menu[selection]['name']: <9} | {
                menu[selection]['price']: >5}"
        )
    print()


# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input("Select menu item number " +
                     str(count) + " (from 1 to 5): ")
        count += 1
        order.append(menu[int(item)])
    return order


"""
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
"""


def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    summarize = summarize_order(order)
    print("Summarize order is: " + str(summarize))


if __name__ == "__main__":
    main()
