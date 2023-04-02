def Solution(N):
    answer = ['' for _ in range(N * 5)]
    
    for idx in range(N*5):
        if idx < N or (2 * N - 1 < idx < 2 * N + N):
            answer[idx] = "@" * (N * 5)
        else:
            answer[idx] = "@" * N
        
    return "\n".join(answer)


N = int(input())
    
print(Solution(N))