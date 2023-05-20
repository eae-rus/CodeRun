import numpy as np

def main():
    """
    """
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    counts = np.zeros(k)
    l, r = 0, 0
    cost = float('inf')
    while l < n:
        while counts.sum() < k and r < n:
            if a[r] <= k:
                if counts[a[r]-1] == 0:
                    counts[a[r]-1] += 1
            r += 1
        if counts.sum() == k:
            cost = min(cost, sum(a[l:r]))
        
        if a[l] <= k:    
            counts[a[l]-1] -= 1
        l += 1
    
    print(cost)


if __name__ == '__main__':
	main()