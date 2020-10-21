"""This file simulates long-run monopoly games with dice of the type specified, and finds
the six-digit modal string of the most common three squares"""

dicenum = 2     # number of dice to roll
dicetype = 4    # type of dice to roll

gamenumber = 100   # number of games to simulate
gamelength = 10000   # number of turns per simulated game

import random
random.seed()

def roll():
    return random.randint(1,dicetype)

board = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
         "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
         "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
         "GTJ", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]
boardlength = len(board)

cchestcards = ["GO", "JAIL"] + ["" for n in range(14)]
chancecards = ["GO", "JAIL", "C1", "E3", "H2", "R1", "NextR", "NextR", "NextU", "Back3"] + ["" for n in range(6)]

def main():
    totalvisitcount = [0 for n in board]

    for game in range(gamenumber):
        pos = 0
        chdeck = chancecards.copy()
        random.shuffle(chdeck)
        ccdeck = cchestcards.copy()
        random.shuffle(ccdeck)
        visitcount = [0 for n in board]
        doublescount = 0

        for turn in range(gamelength):
            (d1,d2) = (roll(), roll())
            if d1 == d2:
                doublescount += 1
            else:
                doublescount = 0
            pos = (pos + d1 + d2) % boardlength

            # check for third doubles
            if doublescount >= 3:
                pos = board.index("JAIL")
                doublescount = 0
            elif pos == board.index("GTJ"):
                pos = board.index("JAIL")
            else:
                if board[pos] in {"CH1", "CH2", "CH3"}:
                    card = chdeck.pop(0)
                    if card in {"GO", "JAIL", "C1", "E3", "H2", "R1"}:
                        pos = board.index(card)
                    elif card == "NextR":
                        while board[pos] not in {"R1", "R2", "R3", "R4"}:
                            pos = (pos + 1) % boardlength
                    elif card == "NextU":
                        while board[pos] not in {"U1", "U2"}:
                            pos = (pos + 1) % boardlength
                    elif card == "Back3":
                        pos = (pos - 3) % boardlength
                    chdeck.append(card)

                # CC must be evaluated separately because CH3 with a Back3 card can land on CC3
                if board[pos] in {"CC1", "CC2", "CC3"}:
                    card = ccdeck.pop(0)
                    if card != "":
                        pos = board.index(card)
                    ccdeck.append(card)

            visitcount[pos] += 1
        totalvisitcount = [totalvisitcount[n] + visitcount[n] for n in range(len(totalvisitcount))]

    visits = [(str(n).zfill(2), board[n], totalvisitcount[n]) for n in range(len(totalvisitcount))]
    visits.sort(key = lambda x: x[2], reverse = True)
    print(visits)

from time import time

if __name__ == '__main__':
    starttime = time()
    main()
    print("Completed in", time() - starttime, "seconds")