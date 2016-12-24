# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, P, Q):
    # write your code in Python 2.7
    F = arrayF(N)
    prefix_sum = [0] * (N+2)
    for k in xrange(1, N + 2):
        prefix_sum[k] = prefix_sum[k-1]
        if F[k-1] != 0 and F[(k-1)//F[k-1]] == 0:
            prefix_sum[k] += 1
    
    M = len(P)
    count = [0] * M
    for i in xrange(M):
        count[i] = prefix_sum[Q[i]+1] - prefix_sum[P[i]]
        
    return count

def arrayF(n):
    F = [0] * (n + 1)
    i=2
    while (i * i <= n):
        if (F[i] == 0):
            k= i * i
            while (k <= n):
                if (F[k] == 0):
                    F[k] = i;
                k += i
        i += 1
    return F