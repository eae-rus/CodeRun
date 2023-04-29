import sys


def main():
    '''
    MSE можно найти за счёт математических преобразований (производной) как:
    - среднее арифметическое входных чисел делённое на число элементов
    MAE и MAPE будем искать за счёт:
    - минимального отклонения MAE и MAPE по массиву уникальных чисел от меньшего
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
    set_elements = list(set(selection_elements))
    # используем его для поиска MAE и MAPE
    min_elements = min(set_elements)
    set_elements.remove(min_elements)
    
    mae = calculate_mae(selection_elements, min_elements)  
    answer_mae = min_elements
    is_finded_answer_mae = False
    mape = calculate_mape(selection_elements, min_elements)
    answer_mape = min_elements
    is_finded_answer_mape = False
    
    while (len(set_elements) > 0) and ((not is_finded_answer_mae) or (not is_finded_answer_mape)):
        min_elements = min(set_elements)
        if not is_finded_answer_mae:
            new_mae = calculate_mae(selection_elements, min_elements)
            if new_mae < mae:
                mae = new_mae
                answer_mae = min_elements
            else:
                is_finded_answer_mae = True
        if not is_finded_answer_mape:
            new_mape = calculate_mape(selection_elements, min_elements)
            if new_mape < mape:
                mape = new_mape
                answer_mape = min_elements
            else:
                is_finded_answer_mape = True
        set_elements.remove(min_elements)
    print(answer_mae)
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


if __name__ == '__main__':
	main()