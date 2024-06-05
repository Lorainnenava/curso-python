def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate)) // 100.00


print(calculate_tax(25000, 15))
