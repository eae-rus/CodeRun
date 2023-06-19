import random
import math

def main():
    '''
    Врать не буду, использовал источник:
    https://habr.com/ru/companies/yandex/articles/461273/
    '''
    EPS = 1e-9

    # генерация пустой строки, тут всё просто.
    def empty_row(size):
        return [0] * size

    # генерация пустой матрицы, тут всё просто.
    def empty_matrix(rows, cols):
        return [empty_row(cols) for _ in range(rows)]

    # Нормализация строки, тут всё просто.
    def normalized_row(row):
        row_sum = sum(row) + EPS
        return [x / row_sum for x in row]

    # Нормализация матрицы по строкам, тут всё просто, я так же делал когда составлял кластеры.
    def normalized_matrix(mtx):
        return [normalized_row(r) for r in mtx]

    def restore_params(alphabet, string_samples):
        '''
        Непосредственная функция для восстановления параметров.
        '''

        # "лишние параметры"
        n_tokens = len(alphabet) # вычисляем количество элементов
        n_samples = len(string_samples) # вычисляем количество строк

        # Преобразуем строки в набор элементов. Кстати, подобное делал и я.
        # разве что входные данные пытался представить через эти вероятности и уже их кластеризовать...
        # + добавлля последний элемент, вероятност перехода в который тоже старался учитывать
        # Вот только зачем здесь 2 последних элемента, всегда равные последнему?
        samples = [tuple([alphabet.index(token) for token in s] + [n_tokens - 1, n_tokens - 1]) for s in string_samples]
        # Генерация рандомной вероятности для старта.
        # По сути это вероятость того, что выборка пренадлежит какой-то из группы
        probs = [random.random() for _ in range(n_samples)]

        # Циклы обучения
        for _ in range(200):
            # сохранение старых вероятностей
            old_probs = [x for x in probs]

            # составление вероятностей первого символа и вероятностей перехода
            p0, A = empty_row(n_tokens), empty_matrix(n_tokens, n_tokens)
            q0, B = empty_row(n_tokens), empty_matrix(n_tokens, n_tokens)
            # заполеняем эти матрицы на основе всех выборок
            for prob, sample in zip(probs, samples):
                p0[sample[0]] += prob
                q0[sample[0]] += 1 - prob
                for t1, t2 in zip(sample[:-1], sample[1:]):
                    A[t1][t2] += prob
                    B[t1][t2] += 1 - prob
            # Нормализуем их. Сиё я тоже делал, но для "входных данных", которые хотел кластеризовать.
            A, p0 = normalized_matrix(A), normalized_row(p0)
            B, q0 = normalized_matrix(B), normalized_row(q0)

            # Считаем логорифмическую разность, надо будет ещё разобраться, зачем и почему это нужно
            # именно в логарифме...
            trans_log_diff = [
                [math.log(b + EPS) - math.log(a + EPS) for b, a in zip(B_r, A_r)]
                for B_r, A_r in zip(B, A)
            ]

            # Пересчитываем новые вероятности того, что выборка относится к созданному кластеру
            probs = empty_row(n_samples)
            for i, sample in enumerate(samples):
                # Оцениваем вероятности по первым выборкам
                value = math.log(q0[sample[0]] + EPS) - math.log(p0[sample[0]] + EPS)
                # И затем вероятности всех остальных переходов
                for t1, t2 in zip(sample[:-1], sample[1:]):
                    value += trans_log_diff[t1][t2]
                # В завершением, перводим в вероятность
                probs[i] = 1.0 / (1.0 + math.exp(value))

            # Проверка условия на завершение, если максимальное изменение становится ниже заданного порога
            # то прекращаем
            if max(abs(x - y) for x, y in zip(probs, old_probs)) < 1e-9:
                break
            
        # В завершении разделяем выборку на кластеры.
        # Я у себя это делал через выделение по принципу:
        # 1) Сортируем максимальные, отбираем до порога "50%"
        # 2) Если получилось больше 80% от n, то прекращаем
        # 3) если получилось меньше 20% от n, то добираем
        # 4) оставшееся - другой кластер
        # *само собой, сохраняем нумерацию
        return [int(x > 0.5) for x in probs]

    # ------------------------------------------------
    n, k = map(int, input().split())
    alphabet = list(input().strip()) + ['']

    # считывание строк
    string_samples = []
    for _ in range(n):
        string_samples.append(input().rstrip())


    # запуск "волшебной модели", и как оказалось, в задаче надо не кластеризировать данные,
    # а просто найти восстановить последовательности, о чём я общем-то тоже размышлял.
    result = restore_params(alphabet, string_samples)
    #вывод данных
    for r in result:
        print(r)

if __name__ == '__main__':
    main()