num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# Write your code here
N=int(input())
l=[]
for i in num_list:
    if N<i:
        l+=[i]
print(l)

"""
input:50
output:[93, 71]
"""
