import sys

def main():
    '''
    '''
    results = []
    for z in range(3):
        points = list(map(float, input().split()))
        
        inner_circle = 0
        outer_circle = 0
        for i in range(0,len(points)-1,2):
            x = points[i]
            y = points[i+1]
            r = (x*x+y*y)**0.5
            if r < 0.5:
                inner_circle += 1
            else:
                outer_circle += 1

        if abs(inner_circle-outer_circle) < 50:
            results.append(1)
        else:
            results.append(2)

    for result in results:
        print(result)


if __name__ == '__main__':
	main()