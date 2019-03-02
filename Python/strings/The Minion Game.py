vowels = "AEIOU"


def minion_game(string):
    scoreKev = 0
    scoreStu = 0
    for i in range(len(string)):
        if s[i] in vowels:
            scoreKev += (len(string)-i)
        else:
            scoreStu += (len(string)-i)
    if scoreKev == scoreStu:
        print("Draw")
    elif scoreKev > scoreStu:
        print("Kevin", scoreKev)
    else:
        print("Stuart", scoreStu)


"""
Some WA and TLE!
After some thinking the appraoch above is more eligant
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
    
    if scoreKev == scoreStu:
        print("Draw")
    elif scoreKev > scoreStu:
        print("Kevin", scoreKev)
    else:
        print("Stuart", scoreStu)
"""

