import sys

def main():
    '''
    '''
    X, Y, Z = map(float, input().split())
    number_turns = 0
    step = 1
    itteration = 0
    X_previous_sign = 1
    Y_previous_sign = 1    
    
    while True:
        itteration += 1
        if number_turns == 0:
            print(X + step*X_previous_sign, Y, itteration)
        elif number_turns == 1:
            print(X, Y + step*Y_previous_sign, itteration)
        elif number_turns == 2:
            print(X - step*X_previous_sign, Y, itteration)
        elif number_turns == 3:
            print(X, Y - step*Y_previous_sign, itteration)
        else:
            step /= 2
            number_turns = 0
            continue
        
        sys.stdout.flush()
        sign, Z_new = input().split()
        
        if sign == "+" or itteration > 205:
            break
        
        Z_new = float(Z_new)
        if Z_new > Z:
            Z = Z_new
            number_turns = 0
            if number_turns == 0:
                X += step
                X_previous_sign = 1
            elif number_turns == 1:
                Y += step
                Y_previous_sign = 1
            elif number_turns == 2:
                X -= step
                X_previous_sign = -1
            else:
                Y -= step
                Y_previous_sign = -1
        else:
            number_turns += 1

if __name__ == '__main__':
    main()