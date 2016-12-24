# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(K, M, A):
    # write your code in Python 2.7
    blocksNeeded = 0
    lower = max(A)
    upper = sum(A)
    result = 0
    
    if K == 1:
        return upper
    if K >= len(A):
        return lower
    
    while lower <= upper:
        mid = (lower + upper) / 2
        blocksNeeded = blocksNo(A, mid)
        if blocksNeeded <= K:
            upper = mid - 1
            result = mid
        else:
            lower = mid + 1
            
    return result

def blocksNo(A, maxSum):
    blocks = 1
    preSum = A[0]
    for ele in A[1:]:
        if preSum + ele > maxSum:
            preSum = ele
            blocks += 1
        else:
            preSum += ele
    return blocks