
def num_combinations(target, plays):
    combos = [[1] + [0]*target for _ in plays]
    for i in range(len(plays)):
        for j in range(1, target + 1):
            if i > 0:
                combos_without_play = combos[i-1][j]
            else:
                combos_without_play = 0
            if j >= plays[i]:
                combos_with_play = combos[i][j-plays[i]]
            else:
                combos_with_play = 0
            combos[i][j] = combos_with_play + combos_without_play
    print(combos)
    return combos[-1][-1]





def main():
    target = 12
    plays = [2, 3, 7]
    print(num_combinations(target, plays))


if __name__ == "__main__":
    main()