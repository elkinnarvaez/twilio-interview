from collections import deque
from heapq import heappop, heappush

def dfsRecursive(graph, visited, u):
    visited.add(u)
    print(u)
    for v in graph[u]:
        if v not in visited:
            dfsRecursive(graph, visited, v)

def dfs(graph, visited, s):
    stack = deque()
    stack.append(s)
    visited.add(s)
    while(len(stack) != 0):
        u = stack.pop()
        print(u)
        for v in graph[u]:
            if v not in visited:
                stack.append(v)
                visited.add(v)

def bfs(graph, visited, s):
    queue = deque()
    queue.append(s)
    visited.add(s)
    while(len(queue) != 0):
        u = queue.popleft()
        print(u)
        for v in graph[u]:
            if v not in visited:
                queue.append(v)
                visited.add(v)

def dijkstra(graph, s):
    ans = [float('INF') for _ in range(len(graph))]
    prev = [None for _ in len(graph)]
    visited = set()
    heap = [(0, s)]
    while len(heap) != 0:
        d, u = heappop(heap)
        if u not in visited:
            for v, dv in graph[u]:
                if d + dv < ans[v]:
                    ans[v] = d + dv
                    heappush(heap, (ans[v], v))
                    prev[v] = u
            visited.add(u)
    return ans, prev
    
def main():
    n1 = 5
    graph1 = [
        [1, 2, 3],
        [0],
        [0, 3, 4],
        [0, 2],
        [2]
    ]

    graph2 = [
        [1, 2, 3],
        [],
        [4, 5],
        [5],
        [],
        []
    ]
    dfs(graph1, set(), 0)

main()