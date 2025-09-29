a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))

if a >= b and a >= c:
    print(f"Найбільше число: {a}")
elif b >= a and b >= c:
    print(f"Найбільше число: {b}")
else:
    print(f"Найбільше число: {c}")