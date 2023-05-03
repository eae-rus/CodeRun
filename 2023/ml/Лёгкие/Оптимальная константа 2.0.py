import math

def main():
    '''
    Всё решается формульно, требуется записать расчёт этих формул.
    '''
    sample_size, extra_elements = map(int, input().split())
    a = [None] * sample_size
    b = [None] * sample_size

    for i in range(sample_size):
        line_text = input()
        last_space_index = line_text.rfind(' ')
        b[i] = float(line_text[last_space_index+1:])
        a[i] = float(line_text[line_text.rfind(' ', 0, last_space_index)+1:last_space_index])

    sum_a = sum(a)
    sum_b = sum(b)
    
    answer_mse = sum_a/sum_b
    print(answer_mse)
    
    # получаем уравнение типа
    # p = (  e^(sum(b*ln(1+a/b)) / sum(b))    )- 1
    # считаем по частям
    numerator = 0
    for i in range(sample_size):
        ab_1 = 1 + a[i] / b[i]
        ln_ab_1 = math.log(ab_1)
        numerator += b[i] * ln_ab_1
    answer_msle = math.exp(numerator/sum_b)-1
    print(answer_msle)
    
    answer_LogLoss = answer_mse # по результатам вычислений, производные сходятся к одним значениям
    print(answer_LogLoss)

if __name__ == '__main__':
	main()