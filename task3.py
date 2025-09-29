score = int(input("Введіть вашу оцінку: "))

if score >= 90 and score <= 100:
    print("Ваша оцінка A")
elif score >= 82:
    print("Ваша оцінка B")
elif score >= 74:
    print("Ваша оцінка C")
elif score >= 64:
    print("Ваша оцінка D")
elif score >= 60:
    print("Ваша оцінка E")
elif score >= 35:
    print("Ваша оцінка FX")
elif score >= 0 and score <= 34:
    print("Ваша оцінка F")
else:
    print("Неправильна оцінка! Введіть число від 0 до 100")