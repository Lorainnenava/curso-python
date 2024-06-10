Food_bill = {
    1: 3.99,
    2: 4.55,
    3: 11.99
}


def bill_total(bill):
    total = 0.00
    for k, v in bill.items():
        total += v
    return total


def calculate_tax(percent, bill_total):
    return round((percent * bill_total) / 100.0, 2)


food_total = bill_total(Food_bill)
tax_total = calculate_tax(15, food_total)

print(food_total)
print(tax_total)
