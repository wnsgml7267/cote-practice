from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split()) # 학생들 수, 비교 횟수
students = [[] for _ in range(N+1)] # 학생 번호
inde = [0 for _ in range(N+1)] # 인접 차수
answer = []
q = deque()

for i in range(M):
    x, y = map(int,input().split())
    students[x].append(y)
    inde[y] += 1 # 인접 차수 증가

# 인접 차수 0 인 것들 큐에 삽입
for i in range(1, N+1):
    if inde[i] == 0:
        q.append(i)

while q:
    tmp = q.popleft()
    answer.append(tmp)
    for i in students[tmp]:
        inde[i] -= 1
        if inde[i] == 0:
            q.append(i)
print(*answer)

