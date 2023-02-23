def value(x):
    v = 0
    y = x.split(".")
    l = len(y) - 1
    while l >= 0:
        if l == 2:
            v += int(y[l])*10
        elif l == 1:
            v += int(y[l])*1000
        else:
            v += int(y[l])*100000
        l -= 1
    v += len(y)
    return v
	
def solution(l):
	l.sort(key=value)
	return l
	

	

    
print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
#print(solution(["f", "b", "d", "a"]))