import numpy as np

class MeanCalculator:
    def __init__(self):
        self.Count = 0.
        self.Mean = 0.

    def Add(self, value, weight = 1.):
        self.Count += weight
        self.Mean += weight * (value - self.Mean) / self.Count

    def Remove(self, value, weight = 1.):
        self.Add(value, -weight)

class SumSquaredErrorsCalculator:
    def __init__(self):
        self.MeanCalculator = MeanCalculator()
        self.SSE = 0.

    def Add(self, value, weight = 1.):
        curDiff = value - self.MeanCalculator.Mean
        self.MeanCalculator.Add(value, weight)
        self.SSE += weight * curDiff * (value - self.MeanCalculator.Mean)

    def Remove(self, value, weight = 1.):
        self.Add(value, -weight)


def main():
    OverAllSSE = SumSquaredErrorsCalculator()
    
    sample_size = int(input())
    all_items = np.zeros((sample_size, 2))
    for i in range(sample_size):
        x, y = map(int, input().split())
        all_items[i] = [x, y]
        OverAllSSE.Add(y)
    all_items = all_items[np.argsort(all_items[:, 0])]

    left = SumSquaredErrorsCalculator()
    right = OverAllSSE

    bestA = 0
    bestB = right.MeanCalculator.Mean
    bestC = all_items[0][0]

    bestQ = right.SSE
    
    for i in range(sample_size - 1):
        item = all_items[i]
        nextItem = all_items[i + 1]

        left.Add(item[1])
        right.Remove(item[1])

        if item[0] == nextItem[0]:
            continue

        a = left.MeanCalculator.Mean
        b = right.MeanCalculator.Mean
        c = (item[0] + nextItem[0]) / 2

        q = left.SSE + right.SSE

        if q < bestQ:
            bestA = a
            bestB = b
            bestC = c
            bestQ = q
    
    coeffs = [bestA, bestB, bestC]
    print(" ".join(map(str, coeffs)))

       
if __name__ == '__main__':
	main()