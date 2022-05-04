from datetime import date
from webbrowser import get

START = date(2019, 1, 1)


def get_input_date():
    is_done = False
    while not is_done:
        year, month, day = tuple(int(s) for s in input(
            'Введите дату в формате yyyy.mm.dd : ').split('.'))
        input_date = date(year, month, day)
        if input_date > START:
            return input_date
        print('Прости, но я создан 01 января 2019 года и не знаю что было раньше\n'
              'Попробуй ввести дату после моего Дня Рождения!')
        is_done = user_survey()


def get_count_weeks_year(date: date):
    """
    Функция для получения номера недели в текущем году от начала года до даты полученной функцией в качестве аргумента.

    Args:
        date (object): Объект класса date модуля datetime

    Returns:
        int: номер недели
    """
    return int(date.strftime('%U')) + 1


def get_total_count_weeks_year(year: int):
    """
    Функция для получения количества недель в году

    Args:
        year (int): год в формате yyyy

    Returns:
        int: количество недель
    """
    return int(date(year, 12, 31).strftime('%U')) + 1


def get_total_count_weeks(date: date):
    """
    Функция для получения номера недели за период от START до date

    Args:
        date (object): Объект класса date модуля datetime

    Returns:
        int: номер недели
    """
    # определяем период за который нам необходимо получить номер недели
    period = date.year - START.year
    # формируем список в котором каждый элемент это количество недель в году. Количество элементов зависит от количества полных лет в периоде.
    total_weeks = [get_total_count_weeks_year(
        START.year + i) for i in range(period)]
    # добавляем в список номер недели от начала года до date
    total_weeks.append(get_count_weeks_year(date))
    return sum(total_weeks)


def user_survey():
    """
    user_survey Функция опроса пользователя о желании продолжать использовать программу

    Returns:
        bool: возвращает True если пользователь больше не хочет продолжать и соответственно False, если хочет.
    """
    while 1:
        user_input = input(
            "Хотите попробовать еще раз? Да(Yes)\Нет(No): ").lower()
        if user_input == 'да' or user_input == 'yes':
            return False
        elif user_input == 'нет' or user_input == 'no':
            return True
        else:
            print('Пожалуйста введите "Да(Yes)" или "Нет(No)"')


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
            # в виде объекта класса date
            user_date = get_input_date()
            if user_date is None:
                break
            print('Номер недели от начала времен до вашей даты: ',
                  get_total_count_weeks(user_date))
            is_done = user_survey()
        except ValueError:
            print("Введены некорректные значения")
            is_done = user_survey()
    print('Ну что же, доиграем в следующий раз...')
