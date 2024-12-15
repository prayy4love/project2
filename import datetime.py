import datetime
from functools import reduce

# Данные пользователей, цветов и букетов
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
        ]
    }
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

def buy_flower(user, flower_id, quantity):
    flower = next((f for f in flowers if f['id'] == flower_id), None)
    if flower and flower['quantity'] >= quantity:
        flower['quantity'] -= quantity
        user['purchase_history'].append({'flower_id': flower_id, 'quantity': quantity, 'purchase_date': datetime.datetime.now().strftime('%Y-%m-%d')})
        print(f"Успешно куплено {quantity} шт. {flower['name']}.")
    else:
        print("Недостаточно товара на складе или товар не найден.")

def buy_bouquet(user, bouquet_id, quantity):
    bouquet = next((b for b in bouquets if b['id'] == bouquet_id), None)
    if bouquet and bouquet['quantity'] >= quantity:
        bouquet['quantity'] -= quantity
        user['purchase_history'].append({'bouquet_id': bouquet_id, 'quantity': quantity, 'purchase_date': datetime.datetime.now().strftime('%Y-%m-%d')})
        print(f"Успешно куплено {quantity} шт. {bouquet['name']}.")
    else:
        print("Недостаточно товара на складе или товар не найден.")

def view_purchase_history(user):
    print("История покупок:")
    for purchase in user['purchase_history']:
        if 'flower_id' in purchase:
            flower = next((f for f in flowers if f['id'] == purchase['flower_id']), None)
            if flower:
                print(f"Цветок: {flower['name']}, Количество: {purchase['quantity']}, Дата покупки: {purchase['purchase_date']}")
        elif 'bouquet_id' in purchase:
            bouquet = next((b for b in bouquets if b['id'] == purchase['bouquet_id']), None)
            if bouquet:
                print(f"Букет: {bouquet['name']}, Количество: {purchase['quantity']}, Дата покупки: {purchase['purchase_date']}")

def sort_flowers(criteria):
    if criteria == 'price':
        sorted_flowers = sorted(flowers, key=lambda x: x['price'])
    elif criteria == 'added_at':
        sorted_flowers = sorted(flowers, key=lambda x: x['added_at'])
    else:
        print("Неверный критерий.")
        return
    print("Отсортированные цветы:")
    for flower in sorted_flowers:
        print(f"ID: {flower['id']}, Название: {flower['name']}, Цена: {flower['price']}, Количество: {flower['quantity']}, Дата добавления: {flower['added_at']}")

def sort_bouquets(criteria):
    if criteria == 'price':
        sorted_bouquets = sorted(bouquets, key=lambda x: x['price'])
    elif criteria == 'added_at':
        sorted_bouquets = sorted(bouquets, key=lambda x: x['added_at'])
    else:
        print("Неверный критерий.")
        return
    print("Отсортированные букеты:")
    for bouquet in sorted_bouquets:
        print(f"ID: {bouquet['id']}, Название: {bouquet['name']}, Цена: {bouquet['price']}, Количество: {bouquet['quantity']}, Дата добавления: {bouquet['added_at']}")

def filter_flowers(keyword):
    filtered_flowers = list(filter(lambda x: keyword.lower() in x['name'].lower(), flowers))
    print("Отфильтрованные цветы:")
    for flower in filtered_flowers:
        print(f"ID: {flower['id']}, Название: {flower['name']}, Цена: {flower['price']}, Количество: {flower['quantity']}, Дата добавления: {flower['added_at']}")

def filter_bouquets(keyword):
    filtered_bouquets = list(filter(lambda x: keyword.lower() in x['name'].lower(), bouquets))
    print("Отфильтрованные букеты:")
    for bouquet in filtered_bouquets:
        print(f"ID: {bouquet['id']}, Название: {bouquet['name']}, Цена: {bouquet['price']}, Количество: {bouquet['quantity']}, Дата добавления: {bouquet['added_at']}")

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

def add_bouquet(name, price, quantity, flower_ids_quantities):
    new_bouquet = {
        'id': len(bouquets) + 1,
        'name': name,
        'price': price,
        'quantity': quantity,
        'added_at': datetime.datetime.now().strftime('%Y-%m-%d'),
        'flowers': flower_ids_quantities
    }
    bouquets.append(new_bouquet)
    print(f"Букет {name} успешно добавлен.")

def delete_flower(flower_id):
    global flowers
    flowers = [flower for flower in flowers if flower['id'] != flower_id]
    print(f"Цветок с ID {flower_id} успешно удален.")

def delete_bouquet(bouquet_id):
    global bouquets
    bouquets = [bouquet for bouquet in bouquets if bouquet['id'] != bouquet_id]
    print(f"Букет с ID {bouquet_id} успешно удален.")

def edit_flower(flower_id, name, price, quantity):
    flower = next((f for f in flowers if f['id'] == flower_id), None)
    if flower:
        flower['name'] = name
        flower['price'] = price
        flower['quantity'] = quantity
        print(f"Цветок с ID {flower_id} успешно обновлен.")
    else:
        print("Цветок не найден.")

def edit_bouquet(bouquet_id, name, price, quantity, flower_ids_quantities):
    bouquet = next((b for b in bouquets if b['id'] == bouquet_id), None)
    if bouquet:
        bouquet['name'] = name
        bouquet['price'] = price
        bouquet['quantity'] = quantity
        bouquet['flowers'] = flower_ids_quantities
        print(f"Букет с ID {bouquet_id} успешно обновлен.")
    else:
        print("Букет не найден.")

def manage_users():
    print("Управление пользователями:")
    for user in users:
        print(f"Имя пользователя: {user['username']}, Роль: {user['role']}, Дата создания: {user.get('created_at', 'N/A')}")

def view_statistics():
    total_purchases = reduce(lambda acc, user: acc + len(user['purchase_history']), users, 0)
    average_purchase_price = reduce(lambda acc, user: acc + sum(p['price'] for p in user['purchase_history']), users, 0) / total_purchases if total_purchases > 0 else 0
    print(f"Общее количество покупок: {total_purchases}")
    print(f"Средняя стоимость покупок: {average_purchase_price:.2f}")

# Интерфейс командной строки
def user_interface(user):
    while True:
        print("\n1. Просмотреть доступные цветы")
        print("2. Просмотреть доступные букеты")
        print("3. Купить цветок")
        print("4. Купить букет")
        print("5. Просмотреть историю покупок")
        print("6. Сортировать цветы")
        print("7. Сортировать букеты")
        print("8. Фильтровать цветы")
        print("9. Фильтровать букеты")
        print("10. Обновить профиль")
        print("11. Выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            view_flowers()
        elif choice == '2':
            view_bouquets()
        elif choice == '3':
            flower_id = int(input("Введите ID цветка: "))
            quantity = int(input("Введите количество: "))
            buy_flower(user, flower_id, quantity)
        elif choice == '4':
            bouquet_id = int(input("Введите ID букета: "))
            quantity = int(input("Введите количество: "))
            buy_bouquet(user, bouquet_id, quantity)
        elif choice == '5':
            view_purchase_history(user)
        elif choice == '6':
            criteria = input("Введите критерий сортировки (price/added_at): ")
            sort_flowers(criteria)
        elif choice == '7':
            criteria = input("Введите критерий сортировки (price/added_at): ")
            sort_bouquets(criteria)
        elif choice == '8':
            keyword = input("Введите ключевое слово для фильтрации: ")
            filter_flowers(keyword)
        elif choice == '9':
            keyword = input("Введите ключевое слово для фильтрации: ")
            filter_bouquets(keyword)
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
        print("3. Удалить цветок")
        print("4. Удалить букет")
        print("5. Редактировать данные о цветке")
        print("6. Редактировать данные о букете")
        print("7. Управление пользователями")
        print("8. Просмотреть статистику")
        print("9. Выйти")
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
            add_bouquet(name, price, quantity, flower_ids_quantities)
        elif choice == '3':
            flower_id = int(input("Введите ID цветка: "))
            delete_flower(flower_id)
        elif choice == '4':
            bouquet_id = int(input("Введите ID букета: "))
            delete_bouquet(bouquet_id)
        elif choice == '5':
            flower_id = int(input("Введите ID цветка: "))
            name = input("Введите новое название цветка: ")
            price = float(input("Введите новую цену цветка: "))
            quantity = int(input("Введите новое количество: "))
            edit_flower(flower_id, name, price, quantity)
        elif choice == '6':
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
            edit_bouquet(bouquet_id, name, price, quantity, flower_ids_quantities)
        elif choice == '7':
            manage_users()
        elif choice == '8':
            view_statistics()
        elif choice == '9':
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
