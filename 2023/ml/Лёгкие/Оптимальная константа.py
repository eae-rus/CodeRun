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
    elements = [None] * sample_size
        
    for i in range(sample_size):
        elements[i] = int(input())
    
    answer_mse = sum(elements)/sample_size
    print(answer_mse)
    
    min_value = min(elements)
    max_value = max(elements)
    
    answer_mae = find_opimal_constant_mae(elements, max_value, min_value)
    print(answer_mae)
    answer_mape = find_opimal_constant_mape(elements, max_value, min_value)
    print(answer_mape)
    
# ------------------------------------------------------------------------

# используются формулы "знаков", так как при расчёте разности, остаётся лишь дельта, которая мала и мы точно знаем, что
# значения не переходят через "0". При этом, была более красивая реализация, но максимально сократили, поэтому сейчас чуть хуже читается
# и очень широкая строка. А суть следующая: 
# вычисляем сумму знаков

def __sign_derivative__(elements: list, opimal_constant: float) -> int:
    return -sum(1 for element in elements if element > opimal_constant) + sum(1 for element in elements if element < opimal_constant)

# Во второй функции ещё учитывается "вес" каждого знака
def __sign_relative_derivative__(elements: list, opimal_constant: float) -> int:
    return -sum(1/element for element in elements if element > opimal_constant) + sum(1/element for element in elements if element < opimal_constant)

def find_opimal_constant_mae(elements: list, max_value: int, min_value: int) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    
    if min_value == max_value:
        return min_value
    
    opimal_constant = (max_value + min_value) / 2
    while abs(max_value - min_value) > 2e-6:
        if __sign_derivative__(elements, opimal_constant) > 0:
            max_value = opimal_constant
        else:
            min_value = opimal_constant
        
        opimal_constant = (max_value + min_value) / 2
             
    return opimal_constant

def find_opimal_constant_mape(elements: list, max_value: int, min_value: int) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    
    if min_value == max_value:
        return min_value
    
    opimal_constant = (max_value + min_value) / 2
    while abs(max_value - min_value) > 2e-6:
        if __sign_relative_derivative__(elements, opimal_constant) > 0:
            max_value = opimal_constant
        else:
            min_value = opimal_constant
        
        opimal_constant = (max_value + min_value) / 2
             
    return opimal_constant

if __name__ == '__main__':
	main()