# Проект FitLife - MVP версия 1.0

# Получаем данные пользователя с проверкой try/except
def get_user_data():
    """Получаем имя и возраст пользователя с проверкой ввода."""
    user_name = input('Привет! Как тебя зовут?: ')
    while True:
        try:
            user_age = int(input('Сколько тебе лет?: '))
            if user_age <= 0:
                print('Возраст должен быть положительным числом!')
                continue
            if user_age > 110:
                print('Возраст выглядит неправдоподобно!')
                continue
            break
        except ValueError:
            print('Ошибка! Введите целое число (например, 20)!')
    return user_name, user_age


# Получаем параметры пользователя с проверкой try/except
def get_user_parameters():
    """Получаем вес и рост пользователя с проверкой ввода."""
    while True:
        try:
            user_weight = float(
                input('Введите ваш вес в кг (используйте точку): '))
            if user_weight <= 0:
                print("Вес должен быть положительным числом!")
                continue
            break
        except ValueError:
            print("Ошибка! Используйте число с точкой (например, 70.5).")

    while True:
        try:
            user_height = float(
                input('Введите ваш рост в метрах (используйте точку): '))
            if user_height <= 0:
                print
                ("Рост должен быть положительным числом. Попробуйте ещё раз.")
                continue
            if user_height > 2.5:
                print("Проверьте значение роста. Введите ещё раз.")
                continue
            break
        except ValueError:
            print("Ошибка! Используйте число с точкой (например, 1.75).")

    return user_weight, user_height


# Получаем переменные из функций
user_name, user_age = get_user_data()
user_weight, user_height = get_user_parameters()

# Константы
WATER_PER_KG = 30
MILLILITERS_PER_LITER = 1000

# Расчёт индекса массы тела с округлением
bmi = round(user_weight / (user_height ** 2), 1)
# Расчёт потребления воды в литрах без округления
water_l = user_weight * WATER_PER_KG / MILLILITERS_PER_LITER

# Выводим результат
print()
print()
print(f'--- Отчёт для пользователя {user_name}, {user_age} лет ---')
print(f'Индекс массы тела (BMI): {bmi}')
print(f'Рекомендуемое потребление воды: {water_l:.1f} л в день')
print('--- Расчёт окончен. Будьте здоровы! ---')
print('--- Спасибо, что используете Fit Life Bot!!! ---')
