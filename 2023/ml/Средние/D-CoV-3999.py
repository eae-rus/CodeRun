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
                dict_visited[j] = [i]
            else:
                dict_visited[j].append(i)
    
    visited = np.array([k for k in dict_visited.keys()])
    # Получение индексов, отсортированных по первому столбцу
    visited = np.sort(visited, axis=0)
    
    for number_visite in visited:
        for employee in dict_visited[number_visite]:
            if status[employee] == 1:
                for employee_sick in dict_visited[number_visite]:
                    status[employee_sick] = 1
                continue

    # Вывод статусов сотрудников
    print(' '.join(map(str, status)))
    

if __name__ == '__main__':
	main()