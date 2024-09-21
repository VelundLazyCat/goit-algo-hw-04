'''
Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, 
та буде відповідати відповідно до введеної команди.
У цій домашній роботі зосередимося на інтерфейсі самого бота. Найпростіший і найзручніший на початковому етапі розробки інтерфейс - це консольний застосунок CLI (Command Line Interface). CLI достатньо просто реалізувати. Будь-який CLI складається з трьох основних елементів:

Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів
та модифікаторів команд.
Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання
команд.
Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних
та повернення користувачеві відповіді від функції - handler-а.

На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону
за ім'ям, змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг.
Щоб реалізувати таку нескладну логіку, скористаємося словником. У словнику будемо зберігати ім'я користувача,
як ключ, і номер телефону як значення.
Вимоги до завдання:

Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. Команди та аргументи мають бути розпізнані незалежно від регістру введення.
Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. В разі введення команди "exit" або "close", програма повинна завершувати виконання.
Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.
'''


# щоб зробити масштабування більш постим хендлер буде передвати у набір функцій однаковий комплект змінних.
# то вже на розсуд логіки конкретного метода, буде він їх оброблювать та перевірять чи ні
def say_hello(contacts, *args):
    print("How can I help you?")
    return 'hello'


# метод прощання
def good_bye(contacts, *args):
    print("Good bye!")
    input('Press Enter please...')
    return 'exit'


# додаєвання нового контакту
def add_contact(contacts, *args):
    name, phone = args
    contacts[name] = phone
    print(f'New contact: {name}, phone:{phone} added')
    return 'Contact added'


# Зміна існуючого контакту
def do_change(contacts, *args):
    name, phone = args
    contacts[name] = phone
    print(f'Contact {name} has been changed')
    return 'Contact changed'


# виведення в консоль питомого контакту
def show_phone(contacts, *args):
    name = args
    print(f' Phone of {name} is: {contacts[name]}')
    return 'contact showed'


# виведення в консоль всіх контактів
def show_all(contacts, *args):
    for keys, value in contacts.items():
        print(keys, ':   ', value)
    return 'all showed'


# парсер команд
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# гендлер обробки команд
def get_handler(command):
    return COMMANDS[command]


# словник відаовідності команд і викликаємих ними методів
COMMANDS = {'hello': say_hello,  'add': add_contact,
            'change': do_change, 'phone': show_phone,
            'all': show_all,     'close': good_bye,
            'exit': good_bye,
            }

# головна логіка роботи бота


def main():
    # словник зберігання контактів
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        # приймання команди від користувача
        user_input = input("Enter a command: ").strip().lower()
        # розділення команди від данних
        command, *args = parse_input(user_input)
        # якшо команда валідна викликаємо метод, інакше пишемо користувачу що він не правий
        if COMMANDS.get(command):
            try:
                # обробка усіх помилок невідповідності данних
                result = get_handler(command)(contacts, *args)
            except ValueError:
                print('Invalid data. Please try else..')
            # обробляємо сторки які повертають методи, так дізнаємось що пора виходити
            if result == 'exit':
                break
        else:
            print('Command unknown. Maybe try else?')


if __name__ == "__main__":
    main()
