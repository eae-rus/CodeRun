import sys

def main():
    """_summary_
    """
    n = int(input())
    m = 320000
    bits = [False] * m
    unique_count = 0

    for i in range(n):
        h = hash(sys.stdin.readline()) % m
        if not bits[h]:
            unique_count += 1
            bits[h] = True
    
    if n > 1000:
        print(unique_count*1.1)
    else:
        print(unique_count)


if __name__ == '__main__':
	main()