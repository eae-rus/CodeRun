import sys


def main():
    '''
    MSE можно найти за счёт математических преобразований (производной) как:
    - среднее арифметическое входных чисел делённое на число элементов
    MAE и MAPE будем искать за счёт:
    - минимального отклонения MAE и MAPE по массиву уникальных числе начиная с меньшего значения
    *Примечание: последнее утверждение является не проверенной гипотизой
    '''
    sample_size = int(input())
    selection_elements = [None] * sample_size
        
    for i in range(sample_size):
        sample = int(input())
        selection_elements[i]=sample
    
    answer_mse = sum(selection_elements)/sample_size
    print(answer_mse)

    # дальше создаём сортированный массив уникальных значений
    sorted_set_elements = __quicksort__(list(set(selection_elements)))
    # используем его для поиска минимального абсолютного отклонения
    mae = calculate_mae(selection_elements, sorted_set_elements[0])
    answer_mae = sorted_set_elements[0]
    for elemet in sorted_set_elements[1:]:
        new_mae = calculate_mae(selection_elements, elemet)
        if new_mae < mae:
            mae = new_mae
            answer_mae = elemet
        else:
            break
    print(answer_mae)
    # используем его для поиска минимального абсолютного отклонения
    mape = calculate_mape(selection_elements, sorted_set_elements[0])
    answer_mape = sorted_set_elements[0]
    for elemet in sorted_set_elements[1:]:
        new_mape = calculate_mape(selection_elements, elemet)
        if new_mape < mape:
            mape = new_mape
            answer_mape = elemet
        else:
            break
    print(answer_mape)

def calculate_mae(list1: list, shift: float) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    difference = __difference_list__(list1, [shift]*len(list1))
    abs_difference = [abs(x) for x in difference]
    mae = sum(abs_difference)
    return mae

def calculate_mape(list1: list, shift: float) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    relative_difference = __relative_difference_list__(list1, [shift]*len(list1))
    abs_difference = [abs(x) for x in relative_difference]
    mape = sum(abs_difference)
    return mape

def __difference_list__(list1: list, list2: list) -> list: 
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    difference = [None]*len(list1)
    # Используем цикл for для вычисления разности между соответствующими элементами двух списков
    for i in range(len(list1)):
        difference[i] = list1[i] - list2[i]
    return difference

def __relative_difference_list__(list1: list, list2: list) -> list: 
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    relative_difference = [None]*len(list1)
    # Используем цикл for для вычисления разности между соответствующими элементами двух списков
    for i in range(len(list1)):
        relative_difference[i] = (list1[i] - list2[i])/list1[i]
    return relative_difference

def __quicksort__(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return __quicksort__(less) + [pivot] + __quicksort__(greater)

if __name__ == '__main__':
	main()