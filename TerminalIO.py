import prettytable
import SafeTypes


# Класс для пользовательского ввода
class Input:

    # Конструктор
    def __init__(self):
        self.koefficient = None
        self.invest_volume = None
        self.cash_threads_count = 0
        self.cash_threads_values = []

    # Ввод данных
    def set_data(self):
        self.koefficient = SafeTypes.safe_input("Введите ставку дисконтирования: ", "float", True)
        self.invest_volume = SafeTypes.safe_input("Введите объём инвестиции: ", "float", True)
        while self.cash_threads_count < 4 or self.cash_threads_count > 8:
            self.cash_threads_count = SafeTypes.safe_input("Введите число денежных потоков [4-8]: ", "int", True)
        for j in range(0, self.cash_threads_count):
            self.cash_threads_values.append(SafeTypes.safe_input("> ", "float", True))

    def get_data(self):
        return [self.koefficient, self.invest_volume, self.cash_threads_count, self.cash_threads_values]


# Пользователь вводит число проектов, на каждый создаётся объект класса Input, заполняется методом set_data, аппендится
# к массиву inputs
def user_inputs():

    inputs = []
    inputs_count = 0

    while inputs_count < 2 or inputs_count > 3:
        inputs_count = SafeTypes.safe_input("Введите число проектов [2-3]: ", "int", True)

    for i in range(0, inputs_count):
        print(f"Ввод данных проекта №{i + 1}")
        user_input = Input()
        user_input.set_data()
        inputs.append(user_input)

    return inputs


# Выводим пользователю таблицу с результатами вычислений + лучший проект
def print_results(compared_results):
    results = compared_results[0]
    comment = compared_results[1]
    recommend = compared_results[2]
    output_table = prettytable.PrettyTable()
    output_table.field_names = ["№п/п", "Инвестиции", "Срок", "Коэффициент", "PV.", "NPV.", "PBP.", "PI.",
                                "IRR.", "ROI."]
    for i in range(0, len(results)):
        output_table.add_row([*results[i]])

    print("\n")
    print(output_table)

    for i in comment:
        print(i)

    print("\n")
    print(recommend)
