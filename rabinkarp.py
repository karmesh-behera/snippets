


def searchString(s, t):
    lenS, lenT = len(s), len(t)
    if lenS > lenT:
        return -1 
    searchHash, testHash = 0, 0

    for x in s:
        searchHash += ord(x)

    for i in range(0, lenS-1):
        testHash += ord(t[i]) 
    
    
    if searchHash == testHash + ord(t[lenT-1]):
        if s == t:
            return 0 
        else:
            return -1
    
    for i in range(0, lenT-lenS):
        testHash += ord(t[i+lenS-1])
        if searchHash == testHash:
            if s == t[i:i+lenS]:
                return i
        testHash -= ord(t[i])


    return -1


    

def main():
    t = "GACGCCA"
    s = "GACGCCA"
    print(searchString(s, t))

if __name__ == "__main__":
    main()