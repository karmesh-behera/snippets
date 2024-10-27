
def reach_end(arr):
    end = len(arr)
    furthest = arr[0]
    for i in range(len(arr)):
        if furthest <= i:
            return False
        furthest = max(furthest, arr[i] + i)
    return True 



def main():
    arr = [3,3,1,0,2,0,1]
    print(reach_end(arr))
    negarr = [3,2,0,0,2,0,1]
    print(reach_end(negarr))

if __name__ == "__main__":
    main()