#  1.Три класса исключений
class ValueError(BaseException):
    pass
class TypeError(BaseException):
    pass
class NumberError(BaseException):
    pass
# 2.Класс имеющий три метода, который при ошибке выбрасывает исключение
class MyClass:

    def method_1(self, value):
        if not value:
            raise ValueError('Пустое значение')

    def method_2(self, value):
        if not value.isdigit():
            raise TypeError('Значение не цифровое')

    def method_3(self, value):
        if len(value) < 5:
            raise NumberError('Значене меньше 5')

# 3.Класс имеющий методы работайщие с обьектами и обрабатывающий исключения
class MyHandler:

    @staticmethod
    def handle(method):
        try:
            method()
        except ValueError as e:
            print('Первое исключение:', e)
        except TypeError as e:
            print('Второе исключение:', e)
        except NumberError as e:
            print('Третье исключение:', e)
        except Exception as e:
            print(' Найдено исключение:', e)


my_object = MyClass()

MyHandler.handle(lambda: my_object.method_1(''))
MyHandler.handle(lambda: my_object.method_2('string'))
MyHandler.handle(lambda: my_object.method_3('123'))

