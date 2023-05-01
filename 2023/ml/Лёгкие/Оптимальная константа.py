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
        selection_elements[i] = int(input())
    
    answer_mse = sum(selection_elements)/sample_size
    print(answer_mse)
    
    min_value = min(selection_elements)
    max_value = max(selection_elements)
    
    answer_mae = find_opimal_constant_mae(selection_elements, max_value, min_value)
    print(answer_mae)
    answer_mape = find_opimal_constant_mape(selection_elements, max_value, min_value)
    print(answer_mape)
    
# ------------------------------------------------------------------------

def calculate_mae(elements: list, shift: float) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    return sum(abs(element - shift) for element in elements)

def calculate_mape(elements: list, shift: float, len_arr: int) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    sum = 0
    for i in range(len_arr):
        sum += abs((elements[i] - shift)/elements[i])
    return sum

def calculate_mape(elements: list, shift: float) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    return sum(abs((element - shift) / element) for element in elements)

def find_opimal_constant_mae(selection_elements: list, max_value: int, min_value: int) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    
    if min_value == max_value:
        return min_value
    
    opimal_constant = (max_value + min_value) / 2
    while abs(max_value - min_value) > 1e-6:
        derivative = (calculate_mae(selection_elements, opimal_constant) - 
                      calculate_mae(selection_elements, opimal_constant - 1e-7))
        if derivative > 0:
            max_value = opimal_constant
        else:
            min_value = opimal_constant
        
        opimal_constant = (max_value + min_value) / 2
             
    return opimal_constant

def find_opimal_constant_mape(selection_elements: list, max_value: int, min_value: int) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    
    if min_value == max_value:
        return min_value
    
    opimal_constant = (max_value + min_value) / 2
    while abs(max_value - min_value) > 1e-6:
        derivative = (calculate_mape(selection_elements, opimal_constant) - 
                      calculate_mape(selection_elements, opimal_constant - 1e-7))
        if derivative > 0:
            max_value = opimal_constant
        else:
            min_value = opimal_constant
        
        opimal_constant = (max_value + min_value) / 2
             
    return opimal_constant

if __name__ == '__main__':
	main()