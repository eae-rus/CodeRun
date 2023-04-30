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
    # выбор оптимального алгоритма
    # дальше создаём сортированный массив уникальных значений
    set_elements = list(set(selection_elements))
    log_2_for_grad = math.log2(max_value*10**6)
    computational_load_enumeration = 1 + len(set_elements) # примерная оценка
    computational_load_grad = 6 + 4*log_2_for_grad # примерная оценка

    if computational_load_enumeration - computational_load_grad > 0:
        answer_mae = find_opimal_constant_mae_grad(selection_elements, max_value, min_value)
        print(answer_mae)

        answer_mape = find_opimal_constant_mape_grad(selection_elements, max_value, min_value)
        print(answer_mape)
    else:
        # используем его для поиска MAE и MAPE
        min_elements = min_value
        set_elements.remove(min_elements)
        len_selection_elements = len(selection_elements)

        difference = __difference_list__(selection_elements, [min_elements]*len_selection_elements)
        mae = calculate_mae_enumeration(difference, min_elements)  
        answer_mae = min_elements
        is_finded_answer_mae = False
        mape = calculate_mape_enumeration(selection_elements, difference, min_elements)
        answer_mape = min_elements
        is_finded_answer_mape = False

        while (len(set_elements) > 0) and ((not is_finded_answer_mae) or (not is_finded_answer_mape)):
            min_elements = min(set_elements)
            difference = __difference_list__(selection_elements, [min_elements]*len_selection_elements)
            if not is_finded_answer_mae:
                new_mae = calculate_mae_enumeration(difference)  
                if new_mae < mae:
                    mae = new_mae
                    answer_mae = min_elements
                else:
                    is_finded_answer_mae = True
            if not is_finded_answer_mape:
                new_mape = calculate_mape_enumeration(selection_elements, difference)
                if new_mape < mape:
                    mape = new_mape
                    answer_mape = min_elements
                else:
                    is_finded_answer_mape = True
            set_elements.remove(min_elements)
        print(answer_mae)
        print(answer_mape)
    
# ------------------------------------------------------------------------

def calculate_mae(elements: list, shift: float) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    difference = __difference_list__(elements, [shift]*len(elements))
    abs_difference = [abs(x) for x in difference]
    mae = sum(abs_difference)
    return mae

def calculate_mae_enumeration(difference: list) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    abs_difference = [abs(x) for x in difference]
    mae = sum(abs_difference)
    return mae

def calculate_mape(elements: list, shift: float) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    relative_difference = __relative_difference_list__(elements, [shift]*len(elements))
    abs_difference = [abs(x) for x in relative_difference]
    mape = sum(abs_difference)
    return mape

def calculate_mape_enumeration(elements: list, difference: list) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    relative_difference = [None]*len(elements)
    for i in range(len(elements)):
        relative_difference[i] = (difference[i])/elements[i]
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

def find_opimal_constant_mae_grad(selection_elements: list, max_value, min_value) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    
    if min_value == max_value:
        return min_value
    
    derivative = (calculate_mae(selection_elements, min_value + 1e-7)- 
                  calculate_mae(selection_elements, min_value))/1e-7
    if derivative >= 0:
        return min_value
    
    derivative = (calculate_mae(selection_elements, max_value) - 
                  calculate_mae(selection_elements, max_value - 1e-7))/1e-7
    if derivative < 0:
        return max_value
    
    opimal_constant = (max_value + min_value)/2
    step = 1
    derivative = (calculate_mae(selection_elements, opimal_constant) - 
                  calculate_mae(selection_elements, opimal_constant - 1e-7))/1e-7
    if derivative > 0:
        previous_opimal_constant = opimal_constant
        opimal_constant = opimal_constant - step * derivative
    elif derivative < 0:
        previous_opimal_constant = opimal_constant
        opimal_constant = opimal_constant - step * derivative
    else:
        return opimal_constant
    previous_derivative = derivative
    
    while abs(opimal_constant - previous_opimal_constant) > 1e-6/2:
        derivative = (calculate_mae(selection_elements, opimal_constant) - 
                      calculate_mae(selection_elements, opimal_constant - 1e-7))/1e-7
        if derivative > 0:
            previous_opimal_constant = opimal_constant
            opimal_constant = opimal_constant - step * derivative
        elif derivative < 0:
            previous_opimal_constant = opimal_constant
            opimal_constant = opimal_constant - step * derivative
        else:
            return opimal_constant
        
        # уменьшение шага
        if sign(derivative) != sign(previous_derivative):
            step = step/2
            revious_derivative = derivative
        else:
            previous_derivative = derivative
             
    return opimal_constant

def find_opimal_constant_mape_grad(selection_elements: list, max_value, min_value) -> float:
    # FIXME: отутствует какая-либо "защита" от невалидных значений
    
    if min_value == max_value:
        return min_value
    
    derivative = (calculate_mape(selection_elements, min_value + 1e-7)- 
                  calculate_mape(selection_elements, min_value))/1e-7
    if derivative >= 0:
        return min_value
    
    derivative = (calculate_mape(selection_elements, max_value) - 
                  calculate_mape(selection_elements, max_value - 1e-7))/1e-7
    if derivative < 0:
        return max_value
    
    opimal_constant = min_value
    step = 1
    derivative = (calculate_mape(selection_elements, opimal_constant) - 
                  calculate_mape(selection_elements, opimal_constant - 1e-7))/1e-7
    if derivative > 0:
        previous_opimal_constant = opimal_constant
        opimal_constant = opimal_constant - step * derivative
    elif derivative < 0:
        previous_opimal_constant = opimal_constant
        opimal_constant = opimal_constant - step * derivative
    else:
        return opimal_constant
    previous_derivative = derivative
    
    while abs(opimal_constant - previous_opimal_constant) > 1e-6/2:
        derivative = (calculate_mape(selection_elements, opimal_constant) - 
                      calculate_mape(selection_elements, opimal_constant - 1e-7))/1e-7
        if derivative > 0:
            previous_opimal_constant = opimal_constant
            opimal_constant = opimal_constant - step * derivative
        elif derivative < 0:
            previous_opimal_constant = opimal_constant
            opimal_constant = opimal_constant - step * derivative
        else:
            return opimal_constant
        
        # уменьшение шага
        if sign(derivative) != sign(previous_derivative):
            step = step/2
            previous_derivative = derivative
        else:
            previous_derivative = derivative
             
    return opimal_constant

def sign(x: float) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

if __name__ == '__main__':
	main()