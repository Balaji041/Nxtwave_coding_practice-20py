num_list =  [10, 20, 40, 100]
n = int(input())
first_list =[n]+num_list # Add the number in the beginning
second_list =  num_list+[n]# Add the number at the end

print(first_list)
print(second_list)
"""
input:20
output:
[20, 10, 20, 40, 100]
[10, 20, 40, 100, 20]
"""
