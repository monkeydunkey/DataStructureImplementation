# Enter your code here. Read input from STDIN. Print output to STDOUT
def calc_distance(adj, distArr, root):
    distArr[root] = 0
    visited = set()
    cand = [[i, x] for i, x in enumerate(distArr) if x is not None and x not in visited]
    while len(cand) != 0:
        cand = sorted(cand, key = lambda x : x[1])
        vertex, dist = cand.pop(0)
        visited.add(vertex)
        for i in xrange(len(distArr)):
            if adj[vertex][i] is not None and i not in visited:
                if distArr[i] is None:
                    distArr[i] = dist + adj[vertex][i]
                else:
                    distArr[i] = min(dist + adj[vertex][i], distArr[i])
        cand = [[i, x] for i, x in enumerate(distArr) if x is not None and x not in visited]
        print cand
    return distArr

queries = int(raw_input())
for q in xrange(queries):
    N, m = map(int, raw_input().split(' '))
    distArr = [None for x in xrange(N)]
    adj = [[None for x in xrange(N)] for y in xrange(N)]
    for i in xrange(m):
        a, b, w = map(int, raw_input().split(' '))
        if adj[a-1][b-1] is None:
            adj[a-1][b-1], adj[b-1][a-1] = w, w
        else:
            minEdge = min(adj[a-1][b-1], w)
            adj[a-1][b-1], adj[b-1][a-1] = minEdge, minEdge
    root = int(raw_input()) - 1
    distArr = calc_distance(adj, distArr, root)
    distArr.pop(root)

    distArr = map(lambda x: "-1" if x is None else str(x), distArr)
    print " ".join(distArr)
