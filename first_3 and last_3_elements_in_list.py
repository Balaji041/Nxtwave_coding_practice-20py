N=int(input())
li=[]
for i in range(N):
    Name=input()
    if i<3 or i>(N-4):
        li+=[Name]
print(li)

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
output:['Anjali', 'Ravi', 'Akbar', 'Latha', 'Mohan', 'Ashok']

"""
