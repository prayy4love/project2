def greet(name="Неизвестное имя", age=20):
    print(f"Привет, {name}. Тебе {age} лет.")
 
def add(a, b):
    return a + b

greet(name="Петя", age=30)
greet("Вася" 22)
greet("Соня") 
person = greet("Соня")
result = add(3, 4)
print(result)
print(person)


def multiply(*args):
    print(args)
    result=1
    for num in args