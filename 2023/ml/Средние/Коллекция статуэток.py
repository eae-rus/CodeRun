from collections import defaultdict

def main():
    """
    """
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    counts = defaultdict(int)
    l, r = 0, 0
    cost = float('inf')
    while r < n:
        if a[r] <= k:
            counts[a[r]] += 1
        r += 1
        
        while len(counts) == k:
            cost = min(cost, sum(a[l:r]))
            if a[l] <= k:
                counts[a[l]] -= 1
                if counts[a[l]] == 0:
                    del counts[a[l]]
            l += 1
    
    print(cost)


if __name__ == '__main__':
	main()