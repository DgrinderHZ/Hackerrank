vowels = "AEIOU"
def minion_game(string):
    # your code goes here
    kevin = set()
    stuart = set()
    scoreKev = 0
    scoreStu = 0
    for i in range(len(string)):
        if string[i] in vowels:
            sub = string[i]
            if sub not in kevin:
                    scoreKev += string.count(sub)
            kevin.add(sub)
            for j in range(i+1, len(string)):
                sub += string[j]
                if sub not in kevin:
                    scoreKev += string.count(sub)
                    kevin.add(sub)
        else:
            sub = string[i]
            if sub not in stuart:
                    scoreStu += string.count(sub)
            stuart.add(sub)
            for j in range(i+1, len(string)):
                sub += string[j]
                if sub not in stuart:
                    scoreStu += string.count(sub)
                    stuart.add(sub)
    print(kevin)
    print(stuart)
    if scoreKev == scoreStu:
        print("Draw")
    elif scoreKev > scoreStu:
        print("Kevin", scoreKev)
    else:
        print("Stuart", scoreStu)


if __name__ == '__main__':
