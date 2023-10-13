import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input())
m,n,k = map(int, input().split())

graph = []
for i in range(m):
    graph.append(list(map(int,input())))