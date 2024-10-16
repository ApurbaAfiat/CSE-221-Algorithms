# -*- coding: utf-8 -*-
"""Task_04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S3gIS5FGU18ph5z158Y9wGXpIrNP7a4q
"""

def has_cycle(graph):
    def dfs(node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False
        return False

    N = len(graph)
    visited = [False] * N
    rec_stack = [False] * N

    for node in range(N):
        if not visited[node]:
            if dfs(node, visited, rec_stack):
                return True

    return False
with open("/content/Input4.txt", "r") as file:
    N, M = map(int, file.readline().split())
    adjacency_list = [[] for _ in range(N)]

    for _ in range(M):
        edge = file.readline().split()
        ui = int(edge[0]) - 1
        vi = int(edge[1]) - 1
        adjacency_list[ui].append(vi)
has_cycle_result = has_cycle(adjacency_list)
with open("/content/Output4.txt", "r") as output_file:
    expected_output = output_file.readline().strip()
if has_cycle_result and expected_output == "YES":
    print(" YES")
elif not has_cycle_result and expected_output == "NO":
    print("NO")
else:
    print("Output does not match the expected result.")