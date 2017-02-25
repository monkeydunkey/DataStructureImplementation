# solution to n-queens problem using backtracking
def backtrackQueen(qPositions, column, chessboard):
    if column >= chessboard[1]:
        return qPositions
    y = column
    for i in range(chessboard[0]):
        x = i 
        if x not in [z[0] for z in qPositions]:
            flag = True
            for queen in qPositions:
                if abs(queen[0] - x) == abs(queen[1] - y):
                    flag = False
                    break
            if flag:
                qPositions.append([x, y])
                qPositions = backtrackQueen(qPositions, column + 1, chessboard)
                if len(qPositions) == chessboard[1]:
                    return qPositions
                qPositions.pop()
    return qPositions

if __name__ == '__main__':
    chessboard = [3,3]
    qPositions = []
    qPositions = backtrackQueen(qPositions, 0, chessboard)
    if len(qPositions) == chessboard[1]:
        print 'Solution Found'
        print qPositions
    else:
        print 'No Solution was found'
