# [self.invest_volume, self.t, self.koefficient, self.pv, self.npv, self.pdp, self.pi, self.irr, self.roi]
# ["№п/п", "Инвестиции", "Срок", "Коэффициент", "PV.", "NPV.", "PBP.", "PI.", "IRR.", "ROI."]

# Константы для зелёного текста на чёрном фоне и стандартного стиля
G = "\033[0;32;40m"
N = "\033[0m"


# Получаем максимальный или минимальный результат по столбцу из results
def get_best_param(results, row, find):
    param = []

    for i in range(0, len(results)):
        param.append(float(results[i][row]))

    best_idx = None
    best_value = None

    if find == "max":
        for i in range(0, len(param)):
            if best_value is None or param[i] > best_value:
                best_idx = i
                best_value = param[i]
    else:
        for i in range(0, len(param)):
            if best_value is None or param[i] < best_value:
                best_idx = i
                best_value = param[i]
    return [row, best_idx, best_value]


# Сравниваем результаты
def compare(results):

    # invest_volume, time
    # pv, npv
    # pdp, pi
    # irr, roi

    # Просто массив строк для генерации текста
    comparators = ["Объем инвестиций", "Срок", "PV", "NPV", "PBP", "PI", "IRR", "ROI"]


    # Можно было и циклом, но тогда модульность кода не имеет никакого смысла
    best_params = [get_best_param(results, 0, "min"), get_best_param(results, 1, "min"),
                   get_best_param(results, 3, "max"), get_best_param(results, 4, "max"),
                   get_best_param(results, 5, "min"), get_best_param(results, 6, "max"),
                   get_best_param(results, 7, "max"), get_best_param(results, 8, "max")]

    str_result = []
    comment = []
    recommend_index = []

    # Добавляем номера проектов по порядку, округляем все значения до 3 знаков после запятой, кастуем их в str
    for i in range(0, len(results)):
        string = [f"{i+1}"]
        for j in range(0, len(results[i])):
            string.append(str(round(results[i][j], 3)))
        str_result.append(string)

    # Из массива best_params получаем номера столбцов, лучшие проекты по ним и значения соответствующих параметров
    for i in range(0, len(best_params)):
        # get leading project number
        leading_project = best_params[i][1]
        # res is best project
        res = str_result[leading_project]
        comment.append(f"Проект {leading_project+1} лидирует по показателю {comparators[i]} со значением "
                       f"{best_params[i][2]}")

        # индекс лучшего проекта по PV
        if i == 2:
            recommend_index.append(leading_project)

        # индекс лучшего проекта по ROI (ОДЗ >1.0) или -1
        if i == 7 and (float(best_params[i][2]) > 1.0):
            recommend_index.append(leading_project)
        elif i == 7 and (float(best_params[i][2]) <= 1.0):
            recommend_index.append(-1)

        # getting value, applying green color beforehand, resetting afterhand
        text = res[best_params[i][0] + 1]
        text = G + text + N
        res[best_params[i][0] + 1] = text

    # Генерируем текст рекомендации на индексах из recommend_index. Костыльненько, но работает
    if recommend_index[0] == recommend_index[1]:
        recommend_text = f"Рекомендуется выбрать проект {recommend_index[0]}, поскольку он имеет наивысший PV и " \
                         f"максимальный ROI (при ROI > 1.0)"
    elif recommend_index[0] != recommend_index[1] and recommend_index[1] != -1:
        recommend_text = f"Рекомендуется выбрать проект {recommend_index[1]}, поскольку он имеет максимальный ROI" \
                         f" (при ROI > 1.0)"
    else:
        recommend_text = f"Между n зол выбирай ни одного (С) я. \nВо всех проектах ROI < 1.0"

    return [str_result, comment, recommend_text]
