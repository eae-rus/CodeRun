import sys

def main():
    '''
    '''
    sample_size = int(input())
    selection_elements = [[None] * 2 for i in range(sample_size)]
        
    for i in range(sample_size):
        sample = input().split()
        selection_elements[i][0]=int(sample[0])
        selection_elements[i][1]=int(sample[1])
        
    rope_length = 0
    walking_length = 0
    previous_rope_distance = 0
    previous_rope_high = 0
    previous_distance = 0
    previous_high = 0
    is_need_rope = False
    
    for distance, high in selection_elements:
        if high < previous_rope_high:
            is_need_rope = True
        else:
            if is_need_rope:
                is_need_rope = False
                rope_qrt = (high - previous_rope_high)**2 + (distance - previous_rope_distance)**2
                rope_length += rope_qrt**0.5 
            previous_rope_high = high
            previous_rope_distance = distance
        
        walking_qrt = (high - previous_high)**2 + (distance - previous_distance)**2
        walking_length += walking_qrt**0.5     
        previous_distance = distance
        previous_high = high
        
    print(rope_length + walking_length)


if __name__ == '__main__':
	main()