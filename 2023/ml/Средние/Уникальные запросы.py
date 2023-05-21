import sys

def main():
    """_summary_
    """
    n = int(input())
    m = 131072 # 2**17
    bits = [False] * m
    unique_count = 0
    degree_divisor = 140737488355328 # 2**47
    degree_add = 65536 # 2**16

    for _ in range(n):
        h = hash(sys.stdin.readline())
        h = int(h / degree_divisor) + degree_add
        if not bits[h]:
            unique_count += 1
            bits[h] = True

    print(unique_count)


if __name__ == '__main__':
	main()