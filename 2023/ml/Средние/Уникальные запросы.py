import sys
import hashlib

def main():
    """_summary_
    """
    n = int(input())
    m = 131072 # 2**17
    bits = [False] * m
    unique_count = 0

    for _ in range(n):
        s = sys.stdin.readline()
        h = hashlib.sha512(s.encode()).hexdigest()
        hv = int(h, 16) % m
        if not bits[hv]:
            unique_count += 1
            bits[hv] = True

    print(unique_count)


if __name__ == '__main__':
	main()