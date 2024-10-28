import random

locations = {
    "Лесная поляна": {
        "Описание": "Солнечная поляна, полная сочной травы. Воздух наполнен ароматом цветов. В центре поляны стоит огромный дуб с дуплом.",
        "Предметы": ["Морковка", "Трава"],
        "Задача": "Найдите морковку, чтобы подкормить крольчонка, который прячется в дупле дуба.",
        "Крольчонок": True,
        "Лиса": False,
        "Дупло": True
    },
    "Густой лес": {
        "Описание": "Темный и густой лес, где сложно найти дорогу. В ветвях деревьев прячутся птицы, а на земле валяются опавшие листья.",
        "Предметы": ["Ягода", "Лист", "Камень"],
        "Задача": "Найдите ягоду, чтобы отвлечь лису, которая бродит по лесу.",
        "Крольчонок": False,
        "Лиса": True,
        "Дупло": False
    },
    "Речка": {
        "Описание": "Прозрачная речка с быстрым течением. На берегу растут высокие ивы, а в воде плещутся рыбки.",
        "Предметы": ["Камень", "Палочка"],
        "Задача": "Перейдите через речку, используя палку как мостик.",
        "Крольчонок": False,
        "Лиса": False,
        "Дупло": False,
        "Мостик": False
    },
    "Нора": {
        "Описание": "Теплая и уютная нора, где можно спрятаться от опасности. Внутри норы стоит уютный гнездышко из мягкой травы.",
        "Предметы": [],
        "Задача": "Дойдите до норы, чтобы спастись от хитрой лисы.",
        "Крольчонок": False,
        "Лиса": False,
        "Дупло": False,
        "Мостик": False
    }
}


inventory = []

current_location = "Лесная поляна"

def show_location(location_name):
    location = locations[location_name]
    print(location["Описание"])
    print("В этой локации вы можете найти:", ", ".join(location["Предметы"]))
    print()

def process_command(command):
    global current_location, inventory

    if command == "взять":
        item_name = input("Какой предмет вы хотите взять? ")
        location = locations[current_location]
        if item_name in location["Предметы"]:
            inventory.append(item_name)
            location["Предметы"].remove(item_name)
            print(f"Вы взяли {item_name}.")
        else:
            print("Такого предмета нет в локации.")
    elif command == "использовать":
        item_name = input("Какой предмет вы хотите использовать? ")
        if item_name == "Морковка" and locations[current_location]["Крольчонок"] == True and locations[current_location]["Дупло"] == True:
            locations[current_location]["Крольчонок"] = False
            print("Вы подкормили крольчонка морковкой!")
        elif item_name == "Ягода" and locations[current_location]["Лиса"] == True:
            locations[current_location]["Лиса"] = False
            print("Вы отвлекли лису ягодой!")
        elif item_name == "Палочка" and locations[current_location]["Речка"] == True and locations[current_location]["Мостик"] == False:
            locations[current_location]["Мостик"] = True
            print("Вы построили мостик из палки!")
        else:
            print("Этот предмет нельзя использовать здесь.")
    elif command == "перейти":
        if current_location == "Лесная поляна" and locations[current_location]["Крольчонок"] == False:
            current_location = "Густой лес"
            print("Вы перешли в Густой лес.")
        elif current_location == "Густой лес" and locations[current_location]["Лиса"] == False:
            current_location = "Речка"
            print("Вы вышли к речке.")
        elif current_location == "Речка" and locations[current_location]["Мостик"] == True:
            current_location = "Нора"
            print("Вы перешли через речку и добрались до норы!")
        else:
            print("В этом направлении нет пути.")
    else:
        print("Неизвестная команда.")

while True:
    show_location(current_location)

    if locations[current_location]["Задача"]:
        print(locations[current_location]["Задача"])

    if locations[current_location]["Лиса"]:
        print("Осторожно! В этой локации вас поджидает хитрая лиса!")
    elif locations[current_location]["Крольчонок"]:
        print("В этой локации вы видите маленького крольчонка, который прячется в дупле!")

    command = input("Введите команду (взять, использовать, перейти, выйти): ").lower()

    if command == "выйти":
        print("До свидания!")
        break

    process_command(command)

    if current_location == "Нора":
        print("Вы добрались до норы и в безопасности! Вы победили!")
        break