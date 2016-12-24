# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    max_ending = A[0]
    max_slice = A[0]
 
    for ele in A[1:]:
        max_ending = max(ele, max_ending + ele)
        max_slice = max(max_slice, max_ending)
 
    return max_slice