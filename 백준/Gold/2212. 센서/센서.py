from heapq import heappop, heappush
sensor = int(input()) # 센서
center = int(input()) # 집중국
s_distance = sorted(list(map(int,input().split()))) # 센서 길이   
answer = 0
if center < sensor: # 집중국이 센서보다 작을 경우
  heap = []
  for i in range(1, sensor):
    heappush(heap, -(s_distance[i] - s_distance[i-1])) # 센서 수신 길이 차이
  # 집중국 - 1 만큼 가장 긴 수신 길이 제거
  for i in range(center-1):
    heappop(heap)
  # 남은 수신 영역 길이의 합
  while heap:
    answer += heappop(heap)
print(-answer)