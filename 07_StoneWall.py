# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(H):
    # write your code in Python 2.7
    blocks = 0
    stack = []
    for height in H:
        while len(stack) != 0 and height < stack[-1]:
            stack.pop()
            blocks += 1
        if len(stack) == 0 or height > stack[-1]:
            stack.append(height)
            
    blocks += len(stack)
    return blocks