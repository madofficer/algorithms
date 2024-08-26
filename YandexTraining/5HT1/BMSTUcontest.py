game1 = list(map(int, input().split(':')))

game2 = list(map(int, input().split(':')))

home_away = int(input())

if (game1[0] + game2[0]) == (game1[1] + game2[1]):
    if home_away == 1:  # home
        if game1[1] >= game2[0]:
            print(1)
        else:
            print(0)
    elif home_away == 2:  # away
        if game2[1] >= game1[0]:
            print(1)
        else:
            print(0)
elif (game1[0] + game2[0]) < (game1[1] + game2[1]):

    team1 = game1[0] + game2[0]
    team2 = game1[1] + game2[1]
    if home_away == 1:  # home
        d = 0
        while team1 < team2:
            team1 += 1
            d += 1
        if d + game2[0] <= game1[1]:
            print(d + 1)
        else:
            print(d)
    elif home_away == 2:  # away
        d = 0
        while team1 < team2:
            team1 += 1
            d += 1
        if game1[0] <= game2[1]:
            print(d + 1)
        else:
            print(d)
elif (game1[0] + game2[0]) > (game1[1] + game2[1]):
    print(0)
