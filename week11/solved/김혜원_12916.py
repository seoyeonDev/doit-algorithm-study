def solution(s):

    pCount = s.lower().count('p')
    yCount = s.lower().count('y')

    if(pCount == yCount):
        return True
    else :
        return False