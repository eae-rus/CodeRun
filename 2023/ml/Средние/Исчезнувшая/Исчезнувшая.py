import numpy as np

def main() -> None:
    '''
    Main function that takes in user input to create two photos and
    checks if one photo can be found in all planes of the other.

    Args:
        None

    Returns:
        None
    '''
    n1, m1 = map(int, input()[:-1].split())
    photo_1: np.ndarray = np.empty((n1, m1), dtype=np.uint8)
    for n in range(n1):
        line: str = input()
        for m in range(m1):
            photo_1[n,m] = ord(line[m])

    n2, m2 = map(int, input()[:-1].split())
    photo_2: np.ndarray = np.empty((n2, m2), dtype=np.uint8)
    for n in range(n2):
        line: str = input()
        for m in range(m2):
            photo_2[n,m] = ord(line[m])

    answer: bool = find_foto__in_all_planes(photo_1, photo_2)  

    if answer:
        print("Yes")
    else:
        print("No")

def find_foto__in_all_planes(photo_1: np.ndarray, photo_2: np.ndarray) -> bool:
    '''
    Function that checks if one photo can be found in all planes of the 
    other by rotating the second photo 90 degrees four times and checking 
    if the photo is found in each rotation.

    Args:
        photo_1 (numpy.ndarray): The first photo.
        photo_2 (numpy.ndarray): The second photo.

    Returns:
        bool: True if the photo is found in all planes, False otherwise.
    '''
    for _ in range(4):
        if find_foto(photo_1, photo_2):
            return True
        else:
            photo_2 = np.rot90(photo_2)
    return False

def find_foto(photo_1: np.ndarray, photo_2: np.ndarray) -> bool:
    '''
    Function that checks if one photo can be found in the other by comparing
    all possible subarrays of the second photo of the same size as the first 
    photo to the first photo.

    Args:
        photo_1 (numpy.ndarray): The first photo.
        photo_2 (numpy.ndarray): The second photo.

    Returns:
        bool: True if the photo is found in the other, False otherwise.
    '''
    n1, m1 = photo_1.shape
    n2, m2 = photo_2.shape

    if (n2 < n1 or m2 < m1):
        return False

    elif (n2 == n1 and m2 == m1):
        if np.array_equal(photo_1, photo_2):
            return True
        else:
            return False

    else:
        for i in range(n2 - n1+1):
            for k in range(m2 - m1+1):
                if np.array_equal(photo_1, photo_2[i:i+n1, k:k+m1]):
                    return True
        return False


if __name__ == '__main__':
    main()