g1=input()
n2=len(g1)
if n2%2!=0:
    g1=g1[:int(n2/2)]+'*'+g1[int(n2/2)+1:n2]
else:
    g1=g1[:int(n2/2)-1]+'**'+g1[int(n2/2)+1:n2]
print(g1)
