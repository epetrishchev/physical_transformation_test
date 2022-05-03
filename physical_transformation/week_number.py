from datetime import date

START = date(2019, 1, 1)


def get_count_weeks(date: date):
    """
    get_count_weeks Функция для получения номера недели в текущем году от начала года до даты полученной функцией в качестве аргумента.

    Args:
        date (object): Объект класса date модуля datetime

    Returns:
        int: номер недели
    """
    return int(date.strftime('%U'))


def get_count_weeks_year(year: int):
    """
    get_count_weeks_year Функция для получения количества недель в году

    Args:
        year (int): год в формате yyyy

    Returns:
        int: количество недель
    """
    return int(date(year, 12, 31).strftime('%U')) + 1


def get_total_count_weeks(date: date):
    """
    get_total_count_weeks Функция для получения номера недели за период от START до date

    Args:
        date (object): Объект класса date модуля datetime

    Returns:
        int: номер недели
    """
    # определяем период за который нам необходимо получить номер недели
    period = date.year - START.year
    # формируем список в котором каждый элемент это количество недель в году. Количество элементов зависит от количества полных лет в периоде.
    total_weeks = [get_count_weeks_year(START.year + i) for i in range(period)]
    # добавляем в список номер недели от начала года до date
    total_weeks.append(int(date.strftime('%U')) + 1)
    return sum(total_weeks)


def get_week_number():
    """
    get_week_number Функция для вывода номера недели в консоль. Точка отсчета это дата константы START и до даты, которую вводит пользователь.

    Returns:
        int: номер недели
    """
    # флаг отслеживающий завершение программы
    is_done = False
    while not is_done:
        try:
            # получаем дату, до которой нужно посчитать номер недели от пользователя
            year, month, day = tuple(int(s) for s in input(
                'Введите дату в формате yyyy.mm.dd : ').split('.'))
            # создаем объект класса date
            user_date = date(year, month, day)
            print('Номер недели от начала времен до вашей даты: ',
                  get_total_count_weeks(user_date))
            user_input = input(
                "Хотите попробовать еще раз? Да(Yes)\Нет(No): ").lower()
            if user_input == 'да' or user_input == 'yes':
                break
            elif user_input == 'нет' or user_input == 'no':
                is_done = True
                break
            else:
                print('Пожалуйста введите "Да/Yes" или "Нет/No"')
        except ValueError:
            while True:
                user_input = input(
                    "Некорректная дата. Хотите попробовать еще раз? Да(Yes)\Нет(No): ").lower()
                if user_input == 'да' or user_input == 'yes':
                    break
                elif user_input == 'нет' or user_input == 'no':
                    is_done = True
                    break
                else:
                    print('Пожалуйста введите "Да/Yes" или "Нет/No"')
