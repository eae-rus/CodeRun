import numpy as np

def main():
    
    sample_size = int(input())
    x = np.empty(sample_size)
    y = np.empty(sample_size)
        
    for i in range(sample_size):
        sample = list(map(int, input().split()))
        x[i] = sample[0]
        y[i] = sample[1]

    coeffs = find_coeffs(x, y, sample_size)
    print(" ".join(map(str, coeffs)))

def f(x, y, a, b, c, sample_size):
    y_low = y[x < c]
    y_uper = y[x >= c]
    sum = np.sum((y_low - a)**2) + np.sum((y_uper - b)**2)
    return (sum/sample_size)**0.5 

def find_coeffs(x, y, sample_size):
    sort_set_x = np.sort(np.unique(x))
    len_sort_set_x = len(sort_set_x)
    a_opt = y[0]
    b_opt = y[0]
    c_opt = x[0]
    
    low, upper = 0, len_sort_set_x
    while (upper - low > 0):
        mid_up = int((low + upper) // 2)
        c_up = sort_set_x[mid_up]
        a_up, b_up = find_ab(x, y, c_up, sample_size)
        f_i_up = f(x, y, a_up, b_up, c_up, sample_size)
        
        mid_low = mid_up-1
        c_low = sort_set_x[mid_low]
        a_low, b_low = find_ab(x, y, c_low, sample_size)
        f_i_low = f(x, y, a_low, b_low, c_low, sample_size)
        
        if f_i_up - f_i_low > 0:
            upper = mid_low
            a_opt = a_low
            b_opt = b_low
            c_opt = c_low
        else:
            low = mid_up
            a_opt = a_up
            b_opt = b_up
            c_opt = c_up

    return [a_opt, b_opt, c_opt]

def find_ab(x, y, c, sample_size):
    y_low = y[x < c]
    y_uper = y[x >= c]
    sum_low = np.sum(y_low)
    sum_uper = np.sum(y_uper)
    len_low = len(y_low)
    len_uper = len(y_uper)
    a = sum_low / len_low if len_low != 0 else 0
    b = sum_uper / len_uper if len_uper != 0 else 0
    return a, b

if __name__ == '__main__':
	main()