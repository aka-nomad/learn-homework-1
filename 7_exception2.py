"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    try:
      price, discount, max_discount = float(price), float(discount), int(max_discount)
      if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
      return price - (price * discount / 100)
    except ValueError:
        print('Переданы некорректные аргументы')
    except TypeError:
        print('Не сработало приведение типов данных!')
    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять","five"))
    print(discounted(100.0, 100, "10"))
