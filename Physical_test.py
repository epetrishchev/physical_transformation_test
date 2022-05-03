from datetime import date

START = date(2019, 1, 1)


def get_week_number():
    is_done = False
    while not is_done:
        try:
            year, month, day = tuple(int(s) for s in input(
                'Введите дату в формате yyyy.mm.dd : ').split('.'))
            user_date = date(year, month, day)
            return get_total_count_weeks(user_date)
        except ValueError:
            while True:
                user_input = input(
                    "Некорректная дата. Хотите попробовать еще раз? (Да\Нет): ")
                if user_input == 'Да':
                    break
                elif user_input == 'Нет':
                    is_done = True
                    break
                else:
                    print('Пожалуйста введите "Да" или "Нет"')


def get_count_weeks(date):
    return int(date.strftime('%U'))


def get_count_weeks_year(year):
    return int(date(year, 12, 31).strftime('%U')) + 1


def get_total_count_weeks(date):
    period = date.year - START.year
    total_weeks = [get_count_weeks_year(START.year + i) for i in range(period)]
    total_weeks.append(int(date.strftime('%U')) + 1)
    return sum(total_weeks)


week_number = get_week_number()
if week_number:
    print('Номер текущей недели', week_number)
