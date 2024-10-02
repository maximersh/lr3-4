correct_password = "1234"
user_password = input("Введите пароль: ")
if user_password == correct_password:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")