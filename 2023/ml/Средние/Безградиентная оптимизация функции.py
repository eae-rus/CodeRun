import sys
import random
import math

def main():
    '''
    Реализиую метод симуляции отжига
    '''
    x, y, h = map(float, input().split())
    
    T = 1 # Температура отжига
    alpha = 0.975 # коэффициент трения отжига (0.975^200 примерно 0.01)
    
    while True:
        # Выбор случайного направления
        dx = random.uniform(-1, 1)
        dy = random.uniform(-1, 1)
        
        # Нормировка направления
        norm = math.sqrt(dx*dx + dy*dy)
        dx /= norm
        dy /= norm
        
        # Вычисление новых координат
        x_new = x + dx*T
        y_new = y + dy*T
        
        # Проверка на границы допустимых значений
        if x_new < -50 or x_new > 100 or y_new < -50 or y_new > 100:
            continue
        
        print(x_new, y_new)
        sys.stdout.flush()
        sign, h_new = input().split()
        
        if sign == "+":
            exit(0)
        
        h_new = float(h_new)
        if h_new > h:
            h = h_new
            x = x_new
            y = y_new
        
        # Обновление температуры
        T *= alpha
        

if __name__ == '__main__':
    main()