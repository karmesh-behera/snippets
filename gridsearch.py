
def searchArr(arr, k):
    m, n = 0, len(arr[0])-1
    while m < len(arr) and n >= 0: 
        if arr[m][n] == k:
            return True
        elif arr[m][n] < k:
            m += 1
        else:
            n -= 1
    return False 


def main():
    arr = [[-1, 2, 4, 4, 6], [1, 5, 5, 9, 21], [3, 6, 6, 9, 22], [3, 6, 8, 10, 24], [6, 8, 9, 12, 25], [8, 10, 12, 13, 40]]
    print(searchArr(arr, 7))
    print(searchArr(arr, 8))
    print(searchArr(arr, -1))

if __name__ == "__main__":
    main()