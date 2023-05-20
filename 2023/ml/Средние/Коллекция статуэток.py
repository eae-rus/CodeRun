import numpy as np

def main():
    """
    """
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    signal_avail = np.full(k, False, dtype=np.bool_)
    counts_cont = np.zeros(k, dtype=np.int32)
    l, r = 0, 0
    cost = float('inf')
    while l < n:
        while (not signal_avail.all()) and r < n:
            if a[r] <= k:
                counts_cont[a[r]-1] += 1
                if (not signal_avail[a[r]-1]):
                    signal_avail[a[r]-1] = True
            r += 1
        if signal_avail.all():
            cost = min(cost, sum(a[l:r]))
        
        if a[l] <= k:
            counts_cont[a[l]-1] -= 1
            if counts_cont[a[l]-1] == 0:
                signal_avail[a[l]-1] = False
        l += 1
    
    print(cost)


if __name__ == '__main__':
	main()