text_pass = "hhh lll hhh ddd sss qwerty 12345 password admin"
input_password = input("Введіть пароль: ")

if input_password in text_pass.split():
    print("Пароль знайдено в списку")
else:
    print("Пароль не знайдено в списку")