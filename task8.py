balance = 1000.0  # Початковий баланс

print("Ласкаво просимо до банкомату!")

while True:
    print("\nМеню:")
    print("1. Перевірка балансу")
    print("2. Внесення грошей")
    print("3. Зняття грошей")
    print("4. Вихід")
    
    choice = input("Оберіть опцію (1-4): ")
    
    if choice == "1":
        print(f"Ваш поточний баланс: {balance:.2f} грн")
    
    elif choice == "2":
        amount = float(input("Введіть суму для внесення: "))
        if amount > 0:
            balance += amount
            print(f"Гроші успішно внесено. Новий баланс: {balance:.2f} грн")
        else:
            print("Помилка! Сума повинна бути більше 0")
    
    elif choice == "3":
        amount = float(input("Введіть суму для зняття: "))
        if amount <= 0:
            print("Помилка! Сума повинна бути більше 0")
        elif amount > balance:
            print("Помилка! Недостатньо коштів на рахунку")
        else:
            balance -= amount
            print(f"Гроші успішно знято. Новий баланс: {balance:.2f} грн")
    
    elif choice == "4":
        print("Дякуємо за використання банкомату! До побачення!")
        break
    
    else:
        print("Неправильний вибір! Спробуйте ще раз.")