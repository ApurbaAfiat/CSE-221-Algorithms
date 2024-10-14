# -*- coding: utf-8 -*-
"""Task1_Lab06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HfirdbQLV10TIrFp2E7qVvT5UoTyckyC
"""

import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances
with open("/content/Input1.txt", "r") as f:
    N, M = map(int, f.readline().split())
    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v, w = map(int, f.readline().split())
        graph[u - 1].append((v - 1, w))

    source = int(f.readline()) - 1

# Finding shortest distances
distances = dijkstra(graph, source)
with open("/content/Output1.txt", "w") as f:
    for distance in distances:
        if distance == float('inf'):
            f.write("-1 ")
        else:
            f.write(f"{distance} ")