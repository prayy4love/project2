import datetime
from functools import reduce

# Данные пользователей, цветов, букетов и дополнительных товаров
users = [
    {'username': 'john_doe', 'password': 'password', 'role': 'user', 'purchase_history': [], 'created_at': '2024-09-01'},
    {'username': 'admin_user', 'password': 'password', 'role': 'admin'}
]

flowers = [
    {'id': 1, 'name': 'Роза', 'price': 50, 'quantity': 100, 'added_at': '2024-09-01'},
    {'id': 2, 'name': 'Тюльпан', 'price': 30, 'quantity': 150, 'added_at': '2024-09-02'},
    {'id': 3, 'name': 'Лилия', 'price': 40, 'quantity': 120, 'added_at': '2024-09-03'},
    {'id': 4, 'name': 'Гвоздика', 'price': 25, 'quantity': 200, 'added_at': '2024-09-04'},
    {'id': 5, 'name': 'Орхидея', 'price': 60, 'quantity': 80, 'added_at': '2024-09-05'}
]

bouquets = [
    {
        'id': 1,
        'name': 'Романтический букет',
        'price': 200,
        'quantity': 50,
        'added_at': '2024-09-06',
        'flowers': [
            {'flower_id': 1, 'quantity': 5},
            {'flower_id': 3, 'quantity': 3}
        ],
        'additional_items': [
            {'item_id': 1, 'quantity': 1},  # Плюшевый медведь
            {'item_id': 2, 'quantity': 1}   # Открытка
        ]
    },
    {
        'id': 2,
        'name': 'Весенний букет',
        'price': 150,
        'quantity': 70,
        'added_at': '2024-09-07',
        'flowers': [
            {'flower_id': 2, 'quantity': 7},
            {'flower_id': 4, 'quantity': 5}
        ],
        'additional_items': [
            {'item_id': 2, 'quantity': 1}   # Открытка
        ]
    },
    {
        'id': 3,
        'name': 'Свадебный букет',
        'price': 300,
        'quantity': 30,
        'added_at': '2024-09-08',
        'flowers': [
            {'flower_id': 1, 'quantity': 10},
            {'flower_id': 5, 'quantity': 5}
        ],
        'additional_items': [
            {'item_id': 3, 'quantity': 1}   # Ваза
        ]
    },
    {
        'id': 4,
        'name': 'Детский букет',
        'price': 100,
        'quantity': 100,
        'added_at': '2024-09-09',
        'flowers': [
            {'flower_id': 2, 'quantity': 10},
            {'flower_id': 3, 'quantity': 5}
        ],
        'additional_items': [
            {'item_id': 4, 'quantity': 1}   # Игрушка
        ]
    },
    {
        'id': 5,
        'name': 'Похоронный букет',
        'price': 250,
        'quantity': 20,
        'added_at': '2024-09-10',
        'flowers': [
            {'flower_id': 4, 'quantity': 15},
            {'flower_id': 5, 'quantity': 10}
        ],
        'additional_items': [
            {'item_id': 5, 'quantity': 1}   # Лента
        ]
    }
]

additional_items = [
    {'id': 1, 'name': 'Плюшевый медведь', 'price': 20, 'quantity': 50},
    {'id': 2, 'name': 'Открытка', 'price': 5, 'quantity': 100},
    {'id': 3, 'name': 'Ваза', 'price': 30, 'quantity': 30},
    {'id': 4, 'name': 'Игрушка', 'price': 15, 'quantity': 50},
    {'id': 5, 'name': 'Лента', 'price': 10, 'quantity': 100}
]

# Функции для пользователя
def view_flowers():
    print("Цветы:")
    for flower in flowers:
        print(f"ID: {flower['id']}, Название: {flower['name']}, Цена: {flower['price']}, Количество: {flower['quantity']}, Дата добавления: {flower['added_at']}")

def view_bouquets():
    print("Букеты:")
    for bouquet in bouquets:
        print(f"ID: {bouquet['id']}, Название: {bouquet['name']}, Цена: {bouquet['price']}, Количество: {bouquet['quantity']}, Дата добавления: {bouquet['added_at']}")

def view_additional_items():
    print("Дополнительные товары:")
    for item in additional_items:
        print(f"ID: {item['id']}, Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")

def buy_flower(user, flower_id, quantity):
    flower = next((f for f in flowers if f['id'] == flower_id), None)
    if flower and flower['quantity'] >= quantity:
        flower['quantity'] -= quantity
        user.setdefault('purchase_history', []).append({'item_id': flower_id, 'item_type': 'flower', 'quantity': quantity, 'purchase_date': datetime.datetime.now().strftime('%Y-%m-%d')})
        print(f"Успешно куплено {quantity} шт. {flower['name']}.")
    else:
        print("Недостаточно товара на складе или товар не найден.")

def buy_bouquet(user, bouquet_id, quantity):
    bouquet = next((b for b in bouquets if b['id'] == bouquet_id), None)
    if bouquet and bouquet['quantity'] >= quantity:
        bouquet['quantity'] -= quantity
        user.setdefault('purchase_history', []).append({'item_id': bouquet_id, 'item_type': 'bouquet', 'quantity': quantity, 'purchase_date': datetime.datetime.now().strftime('%Y-%m-%d')})
        print(f"Успешно куплено {quantity} шт. {bouquet['name']}.")
    else:
        print("Недостаточно товара на складе или товар не найден.")

def buy_additional_item(user, item_id, quantity):
    item = next((i for i in additional_items if i['id'] == item_id), None)
    if item and item['quantity'] >= quantity:
        item['quantity'] -= quantity
        user.setdefault('purchase_history', []).append({'item_id': item_id, 'item_type': 'additional_item', 'quantity': quantity, 'purchase_date': datetime.datetime.now().strftime('%Y-%m-%d')})
        print(f"Успешно куплено {quantity} шт. {item['name']}.")
    else:
        print("Недостаточно товара на складе или товар не найден.")

def view_purchase_history(user):
    print("История покупок:")
    for purchase in user.get('purchase_history', []):
        if purchase['item_type'] == 'flower':
            flower = next((f for f in flowers if f['id'] == purchase['item_id']), None)
            if flower:
                print(f"Цветок: {flower['name']}, Количество: {purchase['quantity']}, Дата покупки: {purchase['purchase_date']}")
        elif purchase['item_type'] == 'bouquet':
            bouquet = next((b for b in bouquets if b['id'] == purchase['item_id']), None)
            if bouquet:
                print(f"Букет: {bouquet['name']}, Количество: {purchase['quantity']}, Дата покупки: {purchase['purchase_date']}")
        elif purchase['item_type'] == 'additional_item':
            item = next((i for i in additional_items if i['id'] == purchase['item_id']), None)
            if item:
                print(f"Дополнительный товар: {item['name']}, Количество: {purchase['quantity']}, Дата покупки: {purchase['purchase_date']}")

def sort_items(item_type, criteria):
    if item_type == 'flower':
        items = flowers
    elif item_type == 'bouquet':
        items = bouquets
    elif item_type == 'additional_item':
        items = additional_items
    else:
        print("Неверный тип товара.")
        return

    if criteria == 'цена':
        sorted_items = sorted(items, key=lambda x: x['price'])
    elif criteria == 'дата добавления':
        sorted_items = sorted(items, key=lambda x: x['added_at'])
    else:
        print("Неверный критерий.")
        return

    print(f"Отсортированные {item_type}ы:")
    for item in sorted_items:
        print(f"ID: {item['id']}, Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}, Дата добавления: {item.get('added_at', 'N/A')}")

def filter_items(item_type, keyword):
    if item_type == 'flower':
        items = flowers
    elif item_type == 'bouquet':
        items = bouquets
    elif item_type == 'additional_item':
        items = additional_items
    else:
        print("Неверный тип товара.")
        return

    filtered_items = list(filter(lambda x: keyword.lower() in x['name'].lower(), items))
    print(f"Отфильтрованные {item_type}ы:")
    for item in filtered_items:
        print(f"ID: {item['id']}, Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}, Дата добавления: {item.get('added_at', 'N/A')}")

def update_profile(user, new_password):
    user['password'] = new_password
    print("Профиль успешно обновлен.")

# Функции для администратора
def add_flower(name, price, quantity):
    new_flower = {
        'id': len(flowers) + 1,
        'name': name,
        'price': price,
        'quantity': quantity,
        'added_at': datetime.datetime.now().strftime('%Y-%m-%d')
    }
    flowers.append(new_flower)
    print(f"Цветок {name} успешно добавлен.")

def add_bouquet(name, price, quantity, flower_ids_quantities, additional_item_ids_quantities):
    new_bouquet = {
        'id': len(bouquets) + 1,
        'name': name,
        'price': price,
        'quantity': quantity,
        'added_at': datetime.datetime.now().strftime('%Y-%m-%d'),
        'flowers': flower_ids_quantities,
        'additional_items': additional_item_ids_quantities
    }
    bouquets.append(new_bouquet)
    print(f"Букет {name} успешно добавлен.")

def add_additional_item(name, price, quantity):
    new_item = {
        'id': len(additional_items) + 1,
        'name': name,
        'price': price,
        'quantity': quantity
    }
    additional_items.append(new_item)
    print(f"Дополнительный товар {name} успешно добавлен.")

def delete_flower(flower_id):
    global flowers
    flowers = [flower for flower in flowers if flower['id'] != flower_id]
    print(f"Цветок с ID {flower_id} успешно удален.")

def delete_bouquet(bouquet_id):
    global bouquets
    bouquets = [bouquet for bouquet in bouquets if bouquet['id'] != bouquet_id]
    print(f"Букет с ID {bouquet_id} успешно удален.")

def delete_additional_item(item_id):
    global additional_items
    additional_items = [item for item in additional_items if item['id'] != item_id]
    print(f"Дополнительный товар с ID {item_id} успешно удален.")

def edit_flower(flower_id, name, price, quantity):
    flower = next((f for f in flowers if f['id'] == flower_id), None)
    if flower:
        flower['name'] = name
        flower['price'] = price
        flower['quantity'] = quantity
        print(f"Цветок с ID {flower_id} успешно обновлен.")
    else:
        print("Цветок не найден.")

def edit_bouquet(bouquet_id, name, price, quantity, flower_ids_quantities, additional_item_ids_quantities):
    bouquet = next((b for b in bouquets if b['id'] == bouquet_id), None)
    if bouquet:
        bouquet['name'] = name
        bouquet['price'] = price
        bouquet['quantity'] = quantity
        bouquet['flowers'] = flower_ids_quantities
        bouquet['additional_items'] = additional_item_ids_quantities
        print(f"Букет с ID {bouquet_id} успешно обновлен.")
    else:
        print("Букет не найден.")

def edit_additional_item(item_id, name, price, quantity):
    item = next((i for i in additional_items if i['id'] == item_id), None)
    if item:
        item['name'] = name
        item['price'] = price
        item['quantity'] = quantity
        print(f"Дополнительный товар с ID {item_id} успешно обновлен.")
    else:
        print("Дополнительный товар не найден.")

def manage_users():
    print("Управление пользователями:")
    for user in users:
        print(f"Имя пользователя: {user['username']}, Роль: {user['role']}, Дата создания: {user.get('created_at', 'N/A')}")

def add_user(username, password, role):
    if role not in ['user', 'admin']:
        print("Неверная роль.")
        return
    new_user = {
        'username': username,
        'password': password,
        'role': role,
        'purchase_history': [],
        'created_at': datetime.datetime.now().strftime('%Y-%m-%d')
    }
    users.append(new_user)
    print(f"Пользователь {username} успешно добавлен.")

def delete_user(username):
    global users
    users = [user for user in users if user['username'] != username]
    print(f"Пользователь {username} успешно удален.")

def edit_user(username, new_password, new_role):
    user = next((u for u in users if u['username'] == username), None)
    if user:
        user['password'] = new_password
        user['role'] = new_role
        print(f"Пользователь {username} успешно обновлен.")
    else:
        print("Пользователь не найден.")

def view_statistics():
    total_purchases = reduce(lambda acc, user: acc + len(user.get('purchase_history', [])), users, 0)
    total_purchase_price = reduce(lambda acc, user: acc + sum(p['quantity'] * (flowers[p['item_id']-1]['price'] if p['item_type'] == 'flower' else bouquets[p['item_id']-1]['price'] if p['item_type'] == 'bouquet' else additional_items[p['item_id']-1]['price']) for p in user.get('purchase_history', [])), users, 0)
    average_purchase_price = total_purchase_price / total_purchases if total_purchases > 0 else 0
    print(f"Общее количество покупок: {total_purchases}")
    print(f"Средняя стоимость покупок: {average_purchase_price:.2f}")

# Интерфейс командной строки
def user_interface(user):
    while True:
        print("\n1. Просмотреть доступные цветы")
        print("2. Просмотреть доступные букеты")
        print("3. Просмотреть доступные дополнительные товары")
        print("4. Купить цветок")
        print("5. Купить букет")
        print("6. Купить дополнительный товар")
        print("7. Просмотреть историю покупок")
        print("8. Сортировать товары")
        print("9. Фильтровать товары")
        print("10. Обновить профиль")
        print("11. Выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            view_flowers()
        elif choice == '2':
            view_bouquets()
        elif choice == '3':
            view_additional_items()
        elif choice == '4':
            flower_id = int(input("Введите ID цветка: "))
            quantity = int(input("Введите количество: "))
            buy_flower(user, flower_id, quantity)
        elif choice == '5':
            bouquet_id = int(input("Введите ID букета: "))
            quantity = int(input("Введите количество: "))
            buy_bouquet(user, bouquet_id, quantity)
        elif choice == '6':
            item_id = int(input("Введите ID дополнительного товара: "))
            quantity = int(input("Введите количество: "))
            buy_additional_item(user, item_id, quantity)
        elif choice == '7':
            view_purchase_history(user)
        elif choice == '8':
            item_type = input("Введите тип товара (flower/bouquet/additional_item): ")
            criteria = input("Введите критерий сортировки (цена/дата добавления): ")
            sort_items(item_type, criteria)
        elif choice == '9':
            item_type = input("Введите тип товара (flower/bouquet/additional_item): ")
            keyword = input("Введите ключевое слово для фильтрации: ")
            filter_items(item_type, keyword)
        elif choice == '10':
            new_password = input("Введите новый пароль: ")
            update_profile(user, new_password)
        elif choice == '11':
            break
        else:
            print("Неверный выбор.")

def admin_interface(user):
    while True:
        print("\n1. Добавить цветок")
        print("2. Добавить букет")
        print("3. Добавить дополнительный товар")
        print("4. Удалить цветок")
        print("5. Удалить букет")
        print("6. Удалить дополнительный товар")
        print("7. Редактировать данные о цветке")
        print("8. Редактировать данные о букете")
        print("9. Редактировать данные о дополнительном товаре")
        print("10. Управление пользователями")
        print("11. Просмотреть статистику")
        print("12. Выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            name = input("Введите название цветка: ")
            price = float(input("Введите цену цветка: "))
            quantity = int(input("Введите количество: "))
            add_flower(name, price, quantity)
        elif choice == '2':
            name = input("Введите название букета: ")
            price = float(input("Введите цену букета: "))
            quantity = int(input("Введите количество: "))
            flower_ids_quantities = []
            while True:
                flower_id = int(input("Введите ID цветка (или 0 для завершения): "))
                if flower_id == 0:
                    break
                flower_quantity = int(input("Введите количество цветка: "))
                flower_ids_quantities.append({'flower_id': flower_id, 'quantity': flower_quantity})
            additional_item_ids_quantities = []
            while True:
                item_id = int(input("Введите ID дополнительного товара (или 0 для завершения): "))
                if item_id == 0:
                    break
                item_quantity = int(input("Введите количество дополнительного товара: "))
                additional_item_ids_quantities.append({'item_id': item_id, 'quantity': item_quantity})
            add_bouquet(name, price, quantity, flower_ids_quantities, additional_item_ids_quantities)
        elif choice == '3':
            name = input("Введите название дополнительного товара: ")
            price = float(input("Введите цену дополнительного товара: "))
            quantity = int(input("Введите количество: "))
            add_additional_item(name, price, quantity)
        elif choice == '4':
            flower_id = int(input("Введите ID цветка: "))
            delete_flower(flower_id)
        elif choice == '5':
            bouquet_id = int(input("Введите ID букета: "))
            delete_bouquet(bouquet_id)
        elif choice == '6':
            item_id = int(input("Введите ID дополнительного товара: "))
            delete_additional_item(item_id)
        elif choice == '7':
            flower_id = int(input("Введите ID цветка: "))
            name = input("Введите новое название цветка: ")
            price = float(input("Введите новую цену цветка: "))
            quantity = int(input("Введите новое количество: "))
            edit_flower(flower_id, name, price, quantity)
        elif choice == '8':
            bouquet_id = int(input("Введите ID букета: "))
            name = input("Введите новое название букета: ")
            price = float(input("Введите новую цену букета: "))
            quantity = int(input("Введите новое количество: "))
            flower_ids_quantities = []
            while True:
                flower_id = int(input("Введите ID цветка (или 0 для завершения): "))
                if flower_id == 0:
                    break
                flower_quantity = int(input("Введите количество цветка: "))
                flower_ids_quantities.append({'flower_id': flower_id, 'quantity': flower_quantity})
            additional_item_ids_quantities = []
            while True:
                item_id = int(input("Введите ID дополнительного товара (или 0 для завершения): "))
                if item_id == 0:
                    break
                item_quantity = int(input("Введите количество дополнительного товара: "))
                additional_item_ids_quantities.append({'item_id': item_id, 'quantity': item_quantity})
            edit_bouquet(bouquet_id, name, price, quantity, flower_ids_quantities, additional_item_ids_quantities)
        elif choice == '9':
            item_id = int(input("Введите ID дополнительного товара: "))
            name = input("Введите новое название дополнительного товара: ")
            price = float(input("Введите новую цену дополнительного товара: "))
            quantity = int(input("Введите новое количество: "))
            edit_additional_item(item_id, name, price, quantity)
        elif choice == '10':
            manage_users()
            action = input("Выберите действие (add/delete/edit): ")
            if action == 'add':
                username = input("Введите имя пользователя: ")
                password = input("Введите пароль: ")
                role = input("Выберите роль (user/admin): ")
                add_user(username, password, role)
            elif action == 'delete':
                username = input("Введите имя пользователя для удаления: ")
                delete_user(username)
            elif action == 'edit':
                username = input("Введите имя пользователя для редактирования: ")
                new_password = input("Введите новый пароль: ")
                new_role = input("Выберите новую роль (user/admin): ")
                edit_user(username, new_password, new_role)
            else:
                print("Неверный выбор.")
        elif choice == '11':
            view_statistics()
        elif choice == '12':
            break
        else:
            print("Неверный выбор.")

# Регистрация
def register():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    role = input("Выберите роль (user/admin): ")
    if role not in ['user', 'admin']:
        print("Неверная роль.")
        return
    new_user = {
        'username': username,
        'password': password,
        'role': role,
        'purchase_history': [],
        'created_at': datetime.datetime.now().strftime('%Y-%m-%d')
    }
    users.append(new_user)
    print("Регистрация успешна.")

# Авторизация
def authenticate():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    user = next((u for u in users if u['username'] == username and u['password'] == password), None)
    if user:
        print(f"Добро пожаловать, {user['username']}!")
        if user['role'] == 'user':
            user_interface(user)
        elif user['role'] == 'admin':
            admin_interface(user)
    else:
        print("Неверное имя пользователя или пароль.")

# Запуск приложения
if __name__ == "__main__":
    while True:
        print("\n1. Регистрация")
        print("2. Вход")
        print("3. Выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            register()
        elif choice == '2':
            authenticate()
        elif choice == '3':
            break
        else:
            print("Неверный выбор.")
