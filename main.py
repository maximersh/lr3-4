correct_password = "1234"
user_password = input("Введите пароль: ") #ввод переменной
if user_password == correct_password:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
