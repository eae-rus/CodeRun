
def main():
    
    sample_size = int(input())
    x = [None] * sample_size
    y = [None] * sample_size
        
    for i in range(sample_size):
        sample = list(map(int, input().split()))
        x[i]=sample[0]
        y[i]=sample[1]

    coeffs = find_coeffs(x, y)
    print(" ".join(map(str, coeffs)))

def f(x, y, a, b, c):
    len_x = len(x)
    sum = 0
    for i in range(len_x):
        if x[i] < c:
            sum += (y[i] - a)**2
        else:
            sum += (y[i] - b)**2
    return (sum/len_x)**0.5 

def find_coeffs(x, y):
    set_y = set(x)
    len_x = len(x)
    a_opt = y[0]
    b_opt = y[0]
    c_opt = x[0]
    f_min = f(x, y, a_opt, b_opt, c_opt)
    
    for c_i in set_y:
        y_sum_low = 0
        y_len_low = 0
        y_sum_uper = 0
        y_len_uper = 0
        for i in range(len_x):
            if x[i] < c_i:
                y_sum_low += y[i]
                y_len_low += 1
            else:
                y_sum_uper += y[i]
                y_len_uper += 1
        a_i = y_sum_low / y_len_low if y_len_low != 0 else 0
        b_i = y_sum_uper / y_len_uper if y_len_uper != 0 else 0
        f_i = f(x, y, a_i, b_i, c_i)
        
        if f_i < f_min:
            a_opt = a_i
            b_opt = b_i
            c_opt = c_i
            f_min = f_i
    
    return [a_opt, b_opt, c_opt]


if __name__ == '__main__':
	main()