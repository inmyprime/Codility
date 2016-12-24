# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B):
    # write your code in Python 2.7
    alive_count = 0
    downstream = []
    down_count = 0
    
    for index in range(0,len(A)):
        if B[index] == 1:
            downstream.append(A[index])
            down_count += 1
        else:
            while down_count != 0:
                if downstream[-1] < A[index]:
                    downstream.pop()
                    down_count -= 1
                else:
                    break
            if down_count == 0:
                alive_count += 1
    
    alive_count += down_count
    return alive_count