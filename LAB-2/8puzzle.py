import math
def bfs(src,target):
    visited=[]
    visited.append(src)
    a=[src]
    count=0
    while a:
        count+=1
        print(a[0],'\n')
        if a[0]==target:
            print("Puzzle solved in "+(str)(count)+"moves.")
            return count
        a+=possibleMoves(a[0],visited)
        a.pop(0)
    return False

def possibleMoves(state,visited):
    index=state.index(-1)
    moves=[]
    if index+3 in range(9):
        moves.append('d')
    if index-3 in range(9):
        moves.append('u')
    if index not in [0,3,6]:
        moves.append('l')
    if index not in [2,5,8]:
        moves.append('r')
    
    possMoves=[]
    for move in moves:
        possMoves.append(generate(move,state,index))
    
    return [move for move in possMoves if tuple(move) not in visited]


def generate(move,state,b):
    temp=state.copy()
    if move == 'u':
        temp[b-3], temp[b] = temp[b], temp[b-3]
    if move == 'd':
        temp[b+3], temp[b] = temp[b], temp[b+3]
    if move == 'r':
        temp[b+1], temp[b] = temp[b], temp[b+1]
    if move == 'l':
        temp[b-1], temp[b] = temp[b], temp[b-1]
    return temp
    
    


src=[1,2,3,-1,4,5,6,7,8]
target=[1,2,3,4,5,-1,6,7,8]
bfs(src,target)
