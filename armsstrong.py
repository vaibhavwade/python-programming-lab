x=input('enter the number ')
L=len(x)
sum=0
for j in range (0,L):
 sum+=int(x[j])**L
if int(x)==sum:
 print('angstrong number')
else:
 print('not')
