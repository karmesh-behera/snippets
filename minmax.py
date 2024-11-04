def minmax(arr):
    pairs = [arr[i:i+2] for i in range(0, len(arr), 2)]
    mins, maxes = [], []
    for i in pairs:
        if i[0] <= i[1]:
            mins.append(i[0])
            maxes.append(i[1])
        else:
            mins.append(i[1])
            maxes.append(i[0])
    
    min, max = mins[0], maxes[0]
    for i in range(1, len(mins)):
        if mins[i] < min:
            min = mins[i]
    for i in range(1, len(maxes)):
        if maxes[i] > max:
            max = maxes[i]
    
    return [min, max]


def main():
    arr = [3, 2, 5, 1, 2, 4]
    print(minmax(arr))

if __name__ == "__main__":
    main()