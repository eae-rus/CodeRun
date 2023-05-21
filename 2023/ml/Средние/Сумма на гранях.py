def main():
    '''
    Реализованно за счёт предполагаемой формулы
    '''
    cube_faces = list(map(int, input().split()))
    number_throws = int(input())
    
    b1_sum = sum(cube_faces)/6
    
    bx = 0
    
    for x_previous in cube_faces:
        for x in cube_faces:
            if x != x_previous:
                bx += x
    
    bx_sum = bx/36
    
    sum_k = b1_sum + (number_throws - 1) * bx_sum
    
    print(sum_k)

if __name__ == '__main__':
	main()