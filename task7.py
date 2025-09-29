age = int(input("Введіть ваш вік: "))

if age < 18:
    print("Здоровим.")
else:
    has_diseases = input("Чи є у вас супутні захворювання? (так/ні): ").lower() == "так"
    smokes = input("Чи палите ви? (так/ні): ").lower() == "так"
    drinks_alcohol = input("Чи вживаєте алкоголь? (так/ні): ").lower() == "так"
    
    if has_diseases or smokes or drinks_alcohol:
        print("Ви вважаєтеся в зоні ризику.")
    else:
        print("Ви вважаєтеся Здоровим.")