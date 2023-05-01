import sys


def main():
    '''
    Реализованно за счёт рекурентной функции
    '''
    cube_faces = list(map(int, input().split()))
    number_throws = int(input())

    cube_faces_dict = {face: cube_faces.count(face)/6 for face in set(cube_faces)}
    
    mathematical_expectation = sum_faces_tree(cube_faces_dict, number_throws)
    
    print(mathematical_expectation)

def sum_faces_tree(cube_faces_dict, throws_left: int, before_sum: float = 0, before_probability: float = 1, before_face: int = -1):
    if throws_left > 0:
        sum = 0
        for face, probability in cube_faces_dict.items():
            if face != before_face:
                sum += sum_faces_tree(cube_faces_dict, throws_left - 1, before_sum+face, before_probability*probability, face)
            else:
                sum += sum_faces_tree(cube_faces_dict, throws_left - 1, before_sum, before_probability*probability, face)
        return sum
    else:
        return before_sum * before_probability

if __name__ == '__main__':
	main()