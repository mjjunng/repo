from itertools import product

def solution(word):
    lst = []
    
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            lst.append(''.join(c))

    lst.sort()
        
                
    return lst.index(word) + 1
