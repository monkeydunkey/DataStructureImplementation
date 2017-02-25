def bfsRecurs(adj):
    queue = [0]
    visited = []
    while len(queue) != 0:
        node = queue.pop(0)
        visited.append(node)
        for n in adj[node]:
            if n not in visited and n not in queue:
                queue.append(n)
    return visited

if __name__ == '__main__':
    adj = [[1,2,3], [0,4,5,6], [0,7], [0, 8,9,10], [1], [1], [1], [2], [3], [3], [3]]
    visited = bfsRecurs(adj)
    print visited
    
