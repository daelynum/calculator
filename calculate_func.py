def calculate_from_string(expression: str):

    """для каждого оператора сформировал анонимную функцию"""
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    """разбил список на элементы"""
    lst = expression.split(' ')
    result = []
    """если в первоначальном списке только один жлемент, возвращаю его в качестве ответа"""
    if len(lst) == 1:
        return lst[0]

    """Прохожу по списку элементов"""
    for _ in lst:
        while len(lst) > 1:
            """если список result пуст (то есть это первый проход по циклу), то первый элемент из исходного цикла
             удаляется и вставляется в список result"""
            if not result:
                try:
                    e1 = lst.pop(0)
                    result.append(float(e1))
                except ValueError:
                    raise Exception(f'ожидалось число, найдено: {e1}')
                """если список result уже не пуст (то есть один раз по циклу мы прошлись)"""
            else:
                e1 = result[0]

            """Далее удаляю сл элемент из списка, который должен быть оператором и за одно проверяю, 
            является ли он оператором, щаявленным в словаре вначале функции """
            try:
                operator = lst.pop(0)
                func = operators[operator]
            except KeyError:
                raise ValueError(f'ожидался оператор, найдено: {operator}')
            """Далее удаляю сл элемент из списка, который должен быть числом и  за одно проверяю, 
            является ли он числом"""
            try:
                e2 = lst.pop(0)
                float(e2)
            except ValueError:
                raise Exception(f'ожидалось число, найдено: {e2}')
            """в первом цикле e1 это самое первое число (вставленное в список result), в посл цилах
            заменяю первый элемент на результат функции"""
            result[0] = func(float(e1), float(e2))

        return round(result[0], 3)
