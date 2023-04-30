import sys

def main():
    '''
    Ищется расстояние канатной дороги
    - в воздухе (rope_length)
    - "пешной" канатной дороги (walking_length)
    Выводится их сумма
    Задача решённая
    '''
    sample_size = int(input())
    selection_elements = [[None] * 2 for i in range(sample_size)]
        
    for i in range(sample_size):
        sample = input().split()
        selection_elements[i][0]=int(sample[0])
        selection_elements[i][1]=int(sample[1])
        
    rope_length = 0
    walking_length = 0 # сделал отдельной переменной, так как не согласуется с условием
    
    additional_rope_distance_stack = Stack()
    additional_rope_high_stack = Stack()
    
    # обработка первой точки
    if selection_elements[0][1] < 0:
            additional_rope_distance_stack.push(0)
            additional_rope_high_stack.push(0)
    walking_length += ((selection_elements[0][0])**2 +
                       (selection_elements[0][1])**2) **0.5
    
    # обработка последующих точек
    for i in range(1, sample_size):
        if selection_elements[i][1] < selection_elements[i-1][1]:
            additional_rope_distance_stack.push(selection_elements[i-1][0])
            additional_rope_high_stack.push(selection_elements[i-1][1])
        else:
            while (not additional_rope_high_stack.is_empty() and
                   selection_elements[i][1] >= additional_rope_high_stack.peek()):
                additional_rope_distance = additional_rope_distance_stack.pop()
                additional_rope_high = additional_rope_high_stack.pop()
                rope_length += ((selection_elements[i][0] - additional_rope_distance)**2 + 
                                (selection_elements[i][1] - additional_rope_high)**2) **0.5 
        
        walking_length += ((selection_elements[i][0] - selection_elements[i-1][0])**2 +
                           (selection_elements[i][1] - selection_elements[i-1][1])**2) **0.5
        
    print(rope_length + walking_length)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
	main()