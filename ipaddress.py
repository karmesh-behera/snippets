MAX_IP = [255, 255, 255, 255]
MAX_SIZE = 2**16


def missing_ip(file_input):
    bucket = [0]*MAX_SIZE
    for i in file_input:
        conversion = int("{0:b}".format(i[0]) + "{0:b}".format(i[1]) + "{0:b}".format(i[2]) + "{0:b}".format(i[3]), 2)
        bucket[conversion] = 1
    
    for i in bucket:
        if i == 1:
            return i
    return False

def main():
    print()

if __name__ == "__main__":
    main()