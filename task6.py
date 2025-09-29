purchase_amount = float(input("Введіть суму покупки: "))

if purchase_amount <= 1000:
    discount = 0
    final_amount = purchase_amount
elif purchase_amount <= 5000:
    discount = 10
    final_amount = purchase_amount * 0.9
elif purchase_amount <= 10000:
    discount = 20
    final_amount = purchase_amount * 0.8
else:
    discount = 30
    final_amount = purchase_amount * 0.7

print(f"Сума покупки: {purchase_amount:.2f} грн")
print(f"Знижка: {discount}%")
print(f"Сума до сплати: {final_amount:.2f} грн")