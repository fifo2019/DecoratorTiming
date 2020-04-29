from decorator import Stopwatch, StopwatchTwo


def main():
    print('Вычисление n-го числа ряда Фибоначчи.')
    try:
        num_repet = int(input('Введите количество повторений программы : '))
        element = int(input('Введите номер искомого элемента : '))
    except ValueError:
        print("Вы ввели не число..")
    else:
        print("\t*****   Через декоратор   *****")
        @Stopwatch(num_repet)
        def fibonacci(element):
            a = 0
            b = 1
            for _ in range(int(element)):
                a, b = b, a + b
            return f"{element} элемент последовательности равен {a}"

        print(fibonacci(element))

        print("\t*****   Через контекстный менеджер   *****")
        with StopwatchTwo(num_repet) as st:
            print(fibonacci(element))


if __name__ == '__main__':
    main()