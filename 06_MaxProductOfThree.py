def solution(A):
    # write your code in Python 2.7
    A.sort()
    N = len(A)
    if A[0] < 0 and A[1] < 0:
        return max(A[0]*A[1]*A[N-1], A[N-1]*A[N-2]*A[N-3])
    else:
        return A[N-1]*A[N-2]*A[N-3]