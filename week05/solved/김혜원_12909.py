def solution(s):
    stack = []
    
    # ( 일 때 넣고 )일 때 pop 하기
    for char in s:
        if(char == '('):
            stack.append('(')
        else :
            if(len(stack) == 0):
                return False
            else:
                stack.pop()
    
    if(len(stack) == 0):
        return True
    else:
        return False