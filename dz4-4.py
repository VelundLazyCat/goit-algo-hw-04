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

def say_hello(contacts, *args):
    return "How can I help you?"


def good_bye(contacts, *args):
    return "Good bye!\nPress Enter please..."


def add_contact(contacts, *args):
    name, phone = args
    contacts[name] = phone
    return f'New contact: {name}, phone:{phone} added'


def do_change(contacts, *args):
    name, phone = args
    contacts[name] = phone
    return f'Contact {name} has been changed'


def show_phone(contacts, *args):
    name = args[0]
    return f' Phone of {name} is: {contacts[name]}'


def show_all(contacts, *args):
    result = ''
    for key, value in contacts.items():
        result += f"{key}:   {value}\n"
    return result


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

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)
        if COMMANDS.get(command):
            try:
                # обробка усіх помилок невідповідності данних
                result = get_handler(command)(contacts, *args)
            except ValueError:
                print('Invalid data. Please try else..')
            # обробляємо сторки які повертають методи, так дізнаємось що пора виходити
            print(result)
            if 'bye' in result:
                input()
                break
        else:
            print('Command unknown. Maybe try else?')



if __name__ == "__main__":
    main()
