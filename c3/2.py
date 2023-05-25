#Создать класс Square.
# Добавить в конструктор класса Square собственное исключение NonPositiveDigitException,
# унаследованное от ValueError, которое будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0.
class NonPositiveDigitException(ValueError):
    pass

class Square:
    def __init__(self, side):
        if side <= 0:
            raise NonPositiveDigitException('<0')

s = Square(-6)