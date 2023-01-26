import TerminalIO
import Calculator
import Comparator


# Главная функция
def main():
    # Получаем ввод от пользователя, готовим два массива (под калькуляторы и результаты вычислений)
    user_inputs = TerminalIO.user_inputs()
    calculators = []
    results = []

    # Перебираем все объекты класса Input в массиве, аппендим к массиву калькуляторов объекты класса Calculator,
    # инициализируемые соответствующими полями из Input, выполняем вычисления, закидываем их в results
    for i in range(0, len(user_inputs)):
        calculators.append(Calculator.Calculator(*user_inputs[i].get_data()))
        calculators[i].calc_all()
        results.append(calculators[i].get_results())

    # Сравниваем результаты
    compared_results = Comparator.compare(results)

    # Выводим результаты
    TerminalIO.print_results(compared_results)


# Если имя файла main, то вызываем main()
if __name__ == '__main__':
    main()
