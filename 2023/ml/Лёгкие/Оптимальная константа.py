import sys
import math


def main():
    '''
    MSE можно найти за счёт математических преобразований (производной) как:
    - среднее арифметическое входных чисел делённое на число элементов
    MAE и MAPE будем искать за счёт:
    - постепенного сужения к оптимальной точке.
    *примечание: в реальности, данный алгоритм оптимален только после определённого
    отношения количества выборок к максимальному значению, пока что это не учитывается.
    '''
    sample_size = int(input())
    selection_elements = [None] * sample_size
        
    for i in range(sample_size):
        sample = int(input())
        selection_elements[i]=sample
    
    answer_mse = sum(selection_elements)/sample_size
    print(answer_mse)
    
    min_value = min(selection_elements)
    max_value = max(selection_elements)

    answer_mae = find_opimal_constant_mae_grad(selection_elements, max_value, min_value)
    print(answer_mae)
    answer_mape = find_opimal_constant_mape_grad(selection_elements, max_value, min_value)
    print(answer_mape)
    
# ------------------------------------------------------------------------

def calculate_mae(elements: list, shift: float) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    difference = __difference_list__(elements, shift)
    abs_difference = [abs(x) for x in difference]
    mae = sum(abs_difference)
    return mae

def calculate_mape(elements: list, shift: float) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    relative_difference = __relative_difference_list__(elements, shift)
    abs_difference = [abs(x) for x in relative_difference]
    mape = sum(abs_difference)
    return mape

def __difference_list__(list1: list, min_elements: int) -> list: 
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    difference = [None]*len(list1)
    # Используем цикл for для вычисления разности между соответствующими элементами двух списков
    for i in range(len(list1)):
        difference[i] = list1[i] - min_elements
    return difference

def __relative_difference_list__(list1: list, min_elements: int) -> list: 
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    relative_difference = [None]*len(list1)
    # Используем цикл for для вычисления разности между соответствующими элементами двух списков
    for i in range(len(list1)):
        relative_difference[i] = (list1[i] - min_elements)/list1[i]
    return relative_difference

def find_opimal_constant_mae_grad(selection_elements: list, max_value: int, min_value: int) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    
    if min_value == max_value:
        return min_value
    
    derivative = (calculate_mae(selection_elements, min_value + 1e-7)- 
                  calculate_mae(selection_elements, min_value))
    if derivative >= 0:
        return min_value
    
    derivative = (calculate_mae(selection_elements, max_value) - 
                  calculate_mae(selection_elements, max_value - 1e-7))
    if derivative <= 0:
        return max_value
    
    opimal_constant = (max_value + min_value) / 2
    while abs(max_value - min_value) > 1e-6:
        derivative = (calculate_mae(selection_elements, opimal_constant) - 
                      calculate_mae(selection_elements, opimal_constant - 1e-7))
        if derivative > 0:
            max_value = opimal_constant
        elif derivative < 0:
            min_value = opimal_constant
        else:
            return opimal_constant
        
        opimal_constant = (max_value + min_value) / 2
             
    return opimal_constant

def find_opimal_constant_mape_grad(selection_elements: list, max_value: int, min_value: int) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    
    if min_value == max_value:
        return min_value
    
    derivative = (calculate_mape(selection_elements, min_value + 1e-7)- 
                  calculate_mape(selection_elements, min_value))
    if derivative >= 0:
        return min_value
    
    derivative = (calculate_mape(selection_elements, max_value) - 
                  calculate_mape(selection_elements, max_value - 1e-7))
    if derivative < 0:
        return max_value
    
    opimal_constant = (max_value + min_value) / 2
    while abs(max_value - min_value) > 1e-6:
        derivative = (calculate_mape(selection_elements, opimal_constant) - 
                      calculate_mape(selection_elements, opimal_constant - 1e-7))
        if derivative > 0:
            max_value = opimal_constant
        elif derivative < 0:
            min_value = opimal_constant
        else:
            return opimal_constant
        
        opimal_constant = (max_value + min_value) / 2
             
    return opimal_constant

if __name__ == '__main__':
	main()