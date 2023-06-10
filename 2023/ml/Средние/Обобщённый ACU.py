def main():
    # Читаем входные данные
    n = int(input())
    data = []
    for i in range(n):
        t, y = map(float, input().split())
        data.append((t, y))

    # Сортируем массив предсказаний модели по возрастанию
    data = sorted(data, key=lambda x: x[1])

    # Считаем количество пар объектов (i, j), где i < j и y_i > y_j
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if data[i][0] > data[j][0]:
                count += 1
            elif data[i][0] == data[j][0]:
                count += 0.5

    # Вычисляем AUC
    if count == 0:
        auc = 0.0
    else:
        auc = count / (n * (n - 1) / 2)

    # Выводим результат
    print('{:.6f}'.format(auc))

if __name__ == '__main__':
    main()