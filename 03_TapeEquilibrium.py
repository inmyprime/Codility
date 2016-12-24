def solution(A):
    # write your code in Python 2.7
    N = len(A)
    totalSum = sum(A)
    minDiff = 1000000000;
    
    diff = 2 * A[0] - totalSum
    minDiff = min(minDiff, abs(diff))
    for P in range(1,N-1):
        diff += 2 * A[P]
        minDiff = min(minDiff, abs(diff))
    
    return minDiff