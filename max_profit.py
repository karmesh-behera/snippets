



def max_profit(arr):
    profit = 0
    current_min = arr[0]
    for i in arr:
        if i - current_min > profit:
            profit = i - current_min
        if i < current_min:
            current_min = i 
    return profit 



def main():
    arr = (310, 315, 275, 295, 260, 270, 290, 230, 255, 250)
    print(max_profit(arr)) #expected output is 30




if __name__ == "__main__":
    main()