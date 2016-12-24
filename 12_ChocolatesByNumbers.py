# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, M):
    # write your code in Python 2.7
    g = gcd(N,M)
    return N // g
    
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)