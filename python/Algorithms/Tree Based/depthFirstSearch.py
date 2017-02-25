def depthFirst(adj, node, nodeInfo, time):
    if nodeInfo[node].get('StartTime', -1) != -1:
        return [nodeInfo,time]
    nodeInfo[node]['StartTime'] = time
    for nodes in adj[node]:
        time += 1
        nodeInfo, time = depthFirst(adj, nodes, nodeInfo, time)
    nodeInfo[node]['StopTime'] = time
    return [nodeInfo, time]

if __name__ == '__main__':
    adj = [[1,2,3], [0,4,5,6,7], [0,7], [0, 8,9,10], [1], [1], [1], [2], [3], [3], [3]]
    nodeInfo = [{'node': x} for x in xrange(11)]
    nodeInfo, time = depthFirst(adj, 0, nodeInfo, 0)
    print nodeInfo
