def main():
    """
    """
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    counts = {}
    l, r = 0, 0
    cost = float('inf')
    while l < n:
        while len(counts) < k and r < n:
            if a[r] <= k:
                if a[r] not in counts:
                    counts[a[r]] = 1
                else:
                    counts[a[r]] += 1
            r += 1
        if len(counts) == k:
            cost = min(cost, sum(a[l:r]))
        
        if a[l] <= k:
            counts[a[l]] -= 1
            if counts[a[l]] == 0:
                del counts[a[l]]
        l += 1
    
    print(cost)


if __name__ == '__main__':
	main()