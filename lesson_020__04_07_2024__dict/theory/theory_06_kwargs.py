def my_function(**kwargs):

    print('kwargs = ', kwargs)

    for key, value in kwargs.items():
        print(key, value)  # Выводит имена аргументов и их значения


my_function(name="John", age=25)

