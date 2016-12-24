# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    count = 1
    current = max(abs(A[0]),abs(A[-1]))
    head = 0
    tail = len(A) - 1
    
    while head <= tail:
        headValue = abs(A[head])
        if headValue == current:
            head += 1
            continue
        
        tailValue = abs(A[tail])
        if tailValue == current:
            tail -= 1
            continue
        
        count += 1
        if headValue >= tailValue:
            current = headValue
            head += 1
        else:
            current = tailValue
            tail -= 1
    
    return count