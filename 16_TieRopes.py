# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(K, A):
    # write your code in Python 2.7
    current = 0
    count = 0
    for rope in A:
        current += rope
        if current >= K:
            count += 1
            current = 0
    return count