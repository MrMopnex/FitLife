# Проект FitLife - MVP версия 1.0

# Получаем данные пользователя с проверкой try/except
def get_user_data():
    """Получаем имя и возраст пользователя с проверкой ввода."""
    while True:
        user_name = input('Здравствуйте! Укажите своё имя: ').strip()
        if not user_name:
            print('Имя не может быть пустым')
            continue
        if not (2 <= len(user_name) <= 30):
            print('Имя должно содержать от 2 до 30 символов')
            continue
        break

    while True:
        try:
            user_age = int(input('Укажите свой возраст: '))
            if not (1 <= user_age <= 110):
                print('Возраст должен быть числом от 1 до 110!')
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
                input('Укажите свой вес в кг: '))
            if not (5 <= user_weight <= 300):
                print('Введите число от 5 до 300')
                continue
            break
        except ValueError:
            print("Используйте точку для дробного числа (например, 70.5).")

    while True:
        try:
            user_height = float(
                input('Укажите свой рост в метрах: '))
            if not (.5 <= user_height <= 2.5):
                print("Введи значение от 0.5 до 2.5 метра")
                continue
            break
        except ValueError:
            print("Используйте точку для дробного числа (например, 1.75).")

    return user_weight, user_height


user_name, user_age = get_user_data()
user_weight, user_height = get_user_parameters()

# Константы
WATER_PER_KG = 30
MILLILITERS_PER_LITER = 1000

# Расчёт индекса массы тела с округлением
bmi = round(user_weight / (user_height ** 2), 1)
# Расчёт потребления воды в литрах без округления
water_l = user_weight * WATER_PER_KG / MILLILITERS_PER_LITER

# Интерпретация показателей ИМТ
if bmi <= 16:
    weight_status = "Выраженный дефицит массы тела"
elif 16 < bmi <= 18.5:
    weight_status = "Недостаточная масса тела"
elif 18.5 < bmi <= 25:
    weight_status = "Норма! Так держать!!!"
elif 25 < bmi <= 30:
    weight_status = "Избыточная масса тела"
elif 30 < bmi <= 35:
    weight_status = "Ожирение 1 степени"
elif 35 < bmi <= 40:
    weight_status = "Ожирение 2 степени"
else:
    weight_status = "Ожирение 3 степени"

# Формирование правильного слова для возраста (год, года, лет)
last_digit = user_age % 10
last_two_digits = user_age % 100

if 11 <= last_two_digits <= 14:
    age_word = "лет"
elif last_digit == 1:
    age_word = "год"
elif 2 <= last_digit <= 4:
    age_word = "года"
else:  # 0, 5–9
    age_word = "лет"

# Выводим результат
print()
print()
print(f'--- Отчёт для пользователя {user_name}, {user_age} {age_word} ---')
print(f'Индекс массы тела (BMI): {bmi}.')
print(f'В соответствии с рекомендациями ВОЗ у вас: {weight_status}. ')
print(f'Рекомендуемое потребление воды: {water_l:.1f} л в день')
print('--- Расчёт окончен. Будьте здоровы! ---')
print('--- Спасибо, что используете Fit Life Bot!!! ---')
