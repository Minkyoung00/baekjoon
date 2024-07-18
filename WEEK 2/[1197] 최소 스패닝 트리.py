import sys
input = sys.stdin.readline

class edge():
    def __init__(self,u,v,w) -> None:
        self.u = u
        self.v = v
        self.w = w

def cru(graph,V):
    result = 0
    parents = [ i for i in range(0,V+1)]

    while graph:
        e = graph[0]
        del graph[0]
        u, v, w = e
        winner = max(parents[u],parents[v])
        loser = min(parents[u],parents[v])

        if winner != loser:
            for i in range(V+1):
                if parents[i] == winner:
                    parents[i] = loser
            result += w

    return result

V, E = (int(i) for i in input().split())

graph = []
for i in range(E):
    A, B, C = (int(i) for i in input().split())
    graph.append([A,B,C])
graph.sort(key=lambda x: x[2])

print(cru(graph,V))
