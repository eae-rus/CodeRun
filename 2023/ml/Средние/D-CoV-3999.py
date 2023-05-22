import numpy as np

def main():
    '''
    '''
                
    # Чтение входных данных
    n = int(input())
    status = np.full(n, 0, dtype=np.uint8)
    dict_visited = {}
    # Чтение заражённых сотрудников
    status = np.array(list(map(int, input().split()))).astype(np.uint8)
    
    for i in range(0,n):
        k, *meetings = map(int, input().split())
        for j in meetings:
            if dict_visited.get(j) is None:
                dict_visited[j] = [i, -1]
            else:
                dict_visited[j][1] = i
    
    visited = np.array([(k, *v) for k, v in dict_visited.items()])
    # Получение индексов, отсортированных по первому столбцу
    sorted_indices = np.argsort(visited[:, 0])
    
    for i in sorted_indices:
        employee_1 = visited[i][1]
        employee_2 = visited[i][2]
        if employee_1 != -1 and employee_2 != -1:
            if status[employee_1] or status[employee_2]:
                status[employee_1] = 1
                status[employee_2] = 1   

    # Вывод статусов сотрудников
    print(' '.join(map(str, status)))
    

if __name__ == '__main__':
	main()