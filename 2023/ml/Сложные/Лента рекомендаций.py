import sys

def main():
    '''
    '''
    n, m = list(map(int, sys.stdin.readline().strip().split()))

    # Считывание данных
    array_a = []
    for i in range(n):
        array_a.append(int(sys.stdin.readline().strip()))

    # регистрация массива изменений
    # FIXME: исправить "первый" элемент
    # массив изменений. 
    # Структура:
    # - тип переменной
    # - индекс изменения (первого вхождения)
    # - колличество переменных
    changes_a = [[array_a[-1], []]] 
    len_changes = 1
    for i in range(1,n):
        if array_a[-i] != array_a[-i-1]:
            changes_a[len_changes-1][1].append(n-i)

            changes_structure = [array_a[-i-1], []]
            changes_a.append(changes_structure)
            len_changes += 1
        else:
            changes_a[len_changes-1][1].append(n-i)
    # внесение последнего, 0-го, элемента (вероятно косяк алгоритма выше)
    changes_a[len_changes-1][1].append(0)

    # рекомендательный алгоритм
    recomendation = []
    previous_key = -1
    i = 1
    while i <= len_changes and len_changes > 0:
        if len_changes >= 2:
            if changes_a[-2][0] == changes_a[-1][0]:
                change = changes_a.pop()
                len_changes -= 1
                for x in change[1]:
                    changes_a[-1][1].append(x)

        if changes_a[-i][0] != previous_key:
            recomendation.append(changes_a[-i][1].pop())
            previous_key = changes_a[-i][0]
            if i == 1:
                if changes_a[-1][1] == []:
                    changes_a.pop()
                    len_changes -= 1 
            elif i == 2:
                if changes_a[-2][1] == []:
                    change = changes_a.pop()
                    changes_a.pop()
                    changes_a.append(change)
                    len_changes -= 1
            i = 1
            # FIXME: добавить "склеивание" для защиты от более дальних обнулений
        else:
            i += 1
        

    print(*recomendation) # вывод в обратном порядке


if __name__ == '__main__':
    main()