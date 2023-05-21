import sys

def main():
    """_summary_
    """
    n = int(input())
    m = 199900
    bits = [False] * m
    unique_count = 0

    for _ in range(n):
        h = hash(sys.stdin.readline()) % m
        if not bits[h]:
            unique_count += 1
            bits[h] = True

    print(unique_count)


if __name__ == '__main__':
	main()