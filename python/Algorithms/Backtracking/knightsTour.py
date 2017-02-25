# This is a backtracking based Kinghts tour solution
def backtrackKnight(steps, point, chessboard):
    x, y = point
    cands = []
    # calculating candidate points
    for i in range(1, 3):
        cands.append([x + (3 - i), y + i])
        cands.append([x - (3 - i), y + i])
        cands.append([x + (3 - i), y - i])
        cands.append([x + (3 - i), y - i])
    for can in cands:
        x1 , y1 = can
        if x1 >=0 and y1 >= 0 and x1 < chessboard[0] and y1 < chessboard[1] and (x1, y1) not in steps:
            steps.add((x1, y1))
            steps = backtrackKnight(steps, [x1, y1], chessboard)
            if len(steps) > 20:
                print len(steps)
            if len(steps) == chessboard[0] * chessboard[1]:
                return steps
            steps.remove((x1, y1))
    return steps

# alternate solution
def move(x,y,m):

    result=False
    if x<0 or x>=N or y<0 or y>=N or visited[x][y]==True: # You may merge these two ifs.
        return False
    visited[x][y]=True
    if m==(N * N - 1):
        print "a solution has been found"
        visited[x][y]=True # Set visited here tot true.
        return True
    else:
        print x,",",y
        if (move(x+2,y+1,m+1) or move(x+2,y-1,m+1)
            or move(x-2,y+1,m+1) or move(x-2,y-1,m+1)
            or move(x+1,y+1,m+1) or move(x+1,y-1,m+1)
            or move(x-1,y+1,m+1) or move(x-1,y-1,m+1)): # Place them in one if.
            print x,",",y

            return True
    return False # If the algorithm comes here it may return false


if __name__ == '__main__':
    N = 1 # This way you can test it with 5 or 6 and even 100 if you want to.
    visited = [[False for x in range(N)] for y in range(N)]
    print move(0,0,0)
    x, y = 5, 5
    steps = set()
    chessboard = [x, y]
    flag = False
    for i in xrange(x):
        flag = False
        for j in xrange(y):
            steps.add((i, j))
            steps = backtrackKnight(steps, [i, j], chessboard)
            if len(steps) == x * y:
                print 'Solution Found'
                print steps
                flag = True
                break
            steps.remove((i, j))
        if flag:
            break

    if not flag:
        print 'No Solution was found'
    
