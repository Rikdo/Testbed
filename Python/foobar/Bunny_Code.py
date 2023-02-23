def solution(l, t):
    si = 0
    ei = 0
    while si <= len(l):
        ck = sum(l[si:ei])
        if ck == t:
            return [si, ei-1]
        elif ei >= len(l):
            si += 1
            ei = si
        elif ck >> t:
            si += 1
            ei = si
        else:
            ei += 1
    return [-1, -1]
			
			
print(solution([1, 2, 3, 4], 15))
print(solution([4, 3, 10, 2, 8], 12))