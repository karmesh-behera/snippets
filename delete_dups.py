
#delete duplicates form a sorted array


def deleteDups(arr):


    index = 1
    for i in range(1, len(arr)):
        if arr[index-1] != arr[i]:
            arr[index] = arr[i]
            index += 1



def delete_duplicates(A):
    if not A:
        return 0
    
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index-1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index
            

def main():
    test = [2, 3, 5, 5, 7, 11, 11, 11, 13]
    delete_duplicates(test)
    print(test)
    #expected [2,3,5,7,11,13,x,y,z]


if __name__ == "__main__":
    main()