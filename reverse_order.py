N=int(input())
lis=[]
for i in range(N):
    name=input()
    lis+=[name]
for i in range(N):
    print(lis[N-i-1])
"""
input:8
Anjali
Ravi
Akbar
Suresh
Gopal
Latha
Mohan
Ashok
output:
Ashok
Mohan
Latha
Gopal
Suresh
Akbar
Ravi
Anjali
"""
