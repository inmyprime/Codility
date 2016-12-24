# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, P, Q):
    # write your code in Python 2.7
    mapping = {"A":1, "C":2, "G":3, "T":4}
    N = len(S)
    M = len(P)
    minimum = [0] * M
    prefix_sum = [[0]*(N+1), [0]*(N+1), [0]*(N+1), [0]*(N+1)]
    for K in range(1, N+1):
        prefix_sum[0][K] = prefix_sum[0][K-1]
        prefix_sum[1][K] = prefix_sum[1][K-1]
        prefix_sum[2][K] = prefix_sum[2][K-1]
        prefix_sum[3][K] = prefix_sum[3][K-1]
        prefix_sum[mapping[S[K-1]]-1][K] += 1
    
    for K in range(M):
        for i in range(4):
            if prefix_sum[i][Q[K]+1] - prefix_sum[i][P[K]] != 0:
                minimum[K] = i+1
                break
        
    
    return minimum