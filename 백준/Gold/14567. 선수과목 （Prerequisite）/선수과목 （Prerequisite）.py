import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
level = [0 for _ in range(n+1)] # 진입 차수 : 1 ~ n번의 진입차수 결정
grade = [0 for _ in range(n+1)] # 학기
graph = [[] for _ in range(n+1)]
q = deque()

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b) # a과목이 b의 선수 과목이다.
    level[b] += 1 # 선수 과목 a부터 수강해야하므로 b 진입 차수 증가

for i in range(1, n+1):
    if level[i] == 0: # 진입 차수 0은 큐에 삽입
        q.append((i, 1)) 
        grade[i] = 1 # 1학기에 수강

# 진입 차수 0부터 시작
while q:
    x, cnt = q.popleft()
    for i in graph[x]:
        level[i] -= 1
        if level[i] == 0: # 연결 끊기
            q.append((i, cnt + 1))
            grade[i] = cnt + 1 # 다음 학기
print(*grade[1:])