def main():

    class MeanCalculator:
        def __init__(self):
            self.count = 0.
            self.mean = 0.

        def add(self, value, weight=1.):
            cur_diff = value - self.mean
            self.count += weight
            self.mean += weight * cur_diff / self.count

        def remove(self, value, weight=1.):
            self.add(value, -weight)

    class SumSquaredErrorsCalculator:
        def __init__(self):
            self.mean_calculator = MeanCalculator()
            self.sse = 0.

        def add(self, value, weight=1.):
            cur_diff = value - self.mean_calculator.mean
            self.mean_calculator.add(value, weight)
            self.sse += weight * cur_diff * (value - self.mean_calculator.mean)

        def remove(self, value, weight=1.):
            self.add(value, -weight)

    overall_sse = SumSquaredErrorsCalculator()

    sample_size = int(input())
    all_items = []
    for i in range(sample_size):
        x, y = map(int, input().split())
        all_items.append([x, y])
        overall_sse.add(y)
    all_items.sort(key=lambda x: x[0])

    left = SumSquaredErrorsCalculator()
    right = overall_sse

    best_a = 0
    best_b = right.mean_calculator.mean
    best_c = all_items[0][0]

    best_q = right.sse

    for i in range(sample_size - 1):
        item = all_items[i]
        next_item = all_items[i + 1]

        left.add(item[1])
        right.remove(item[1])

        if item[0] == next_item[0]:
            continue

        a = left.mean_calculator.mean
        b = right.mean_calculator.mean
        c = (item[0] + next_item[0]) / 2

        q = left.sse + right.sse

        if q < best_q:
            best_a = a
            best_b = b
            best_c = c
            best_q = q

    coeffs = [best_a, best_b, best_c]
    print(" ".join(map(str, coeffs)))
    
if __name__ == '__main__':
	main()