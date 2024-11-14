




def cyclicsorted(arr):
    l, u = 0, len(arr)-1
    while l <= u:
        m = l +(u-l)//2
        if arr[m] > arr[m-1] and arr[m] < arr[u]:
            u = m-1
        elif arr[m] < arr[m-1]:
            return m
        else:
            l = m+1
    return -1







def main():
    arr = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
    print(cyclicsorted(arr))

if __name__ == "__main__":
    main()