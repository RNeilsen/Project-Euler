# prob54 of Project Euler
# by Richard Neilsen

# note: card values are internally represented as follows
# 2 = 2, 3 = 3, ..., 9 = 9,  T = 10, J = 11, Q = 12, K = 13, A = 14

def main():
    f = open('poker.txt', 'r')
    p1wins = 0
    for line in f:
        if determine_winner(line) == 1: 
            p1wins += 1
    print(p1wins)
        
def determine_winner(s):
    """determine the winner (1 or 2) of a pair of hands
    
    Input format:
    s -- 10 cards as a spaced string, e.g. '6S 8C 5S QH TH 9H AS AC 2C JD'
    Output format:
    1, 2 (player 1 or 2 wins) or 0 (draw)
    """
    rawcards = [(x[0],x[1]) for x in s.split()]
    cards = []
    for c in rawcards:
        (a,b) = c
        if a == 'T': a = '10'
        if a == 'J': a = '11'
        if a == 'Q': a = '12'
        if a == 'K': a = '13'
        if a == 'A': a = '14'
        cards.append((int(a),b))
    (h1,h2) = (cards[:5], cards[5:])
    
    (hand1, rankedcards1) = handify(h1)
    (hand2, rankedcards2) = handify(h2)
    
    if hand1 > hand2: return 1
    elif hand2 > hand1: return 2
    else:
        i = 0
        while rankedcards1[i][1] > 0:
            if rankedcards1[i][0] > rankedcards2[i][0]: return 1
            elif rankedcards2[i][0] > rankedcards1[i][0]: return 2
            i += 1
        return 0 # draw
    
    
def handify(h):
    """Determine the hand type and rank cards in order of importance
    
    Input format: h (list)
    a hand of cards as a list of pairs (val, suit)
    where val is an int (2-14)
    and suit is a string ('C', 'D', 'H' or 'S')
        
    Output format: (type (int), rankedcards (list))
    where type is the hand (high card = 0, ... straight flush = 8)
    and rankedcards is a collated list of types in the hand
    e.g. [(5,3), (11,2), (14,0), (13,0), (12,0), (10,0), ...]
    represents a full house, fives full of Jacks
    """
    hist = [0 for i in range(15)]
    
    for c in h:
        hist[c[0]] += 1
    
    sortedhist = sorted(hist, reverse=True)
    
    rankedcards = [(i, hist[i]) for i in range(len(hist))]
    rankedcards.sort(key = lambda x : x[0] + x[1] * (len(hist) + 1), reverse = True)
    
    if sortedhist[:2] == [4,1]: # four of a kind
        return (7, rankedcards) 
    elif sortedhist[:2] == [3,2]: # full house
        return (6, rankedcards) 
    elif sortedhist[:3] == [3,1,1]: # three of a kind
        return (3, rankedcards)
    elif sortedhist[:3] == [2,2,1]: # two pair
        return (2, rankedcards) 
    elif sortedhist[:4] == [2,1,1,1]: # pair
        return (1, rankedcards)
    
    suits = sorted([x[1] for x in h])
    flush = (suits[0] == suits[-1])
    vals = sorted([x[0] for x in h])
    straight = (vals[0] == vals[4]-4 or (vals[4]==14 and vals[3]==5))
    
    if flush and straight: # straight flush
        return (8, rankedcards) 
    elif flush:  # flush
        return (5, rankedcards)
    elif straight:  # straight
        return (4, rankedcards)
    else: # high card
        return (0, rankedcards)

if __name__ == '__main__':
    main()