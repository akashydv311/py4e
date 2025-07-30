# find the largest number
largest_so_far = -1
print("Before", largest_so_far)

for i in [9, 41, 12, 3, 74, 15]:
    if largest_so_far < i:
        largest_so_far = i
    print(largest_so_far, i)

print("After", largest_so_far)



print()
# find the sum of all numbers
s = 0
print("Before", s)

for i in [9, 41, 12, 3, 74, 15]:
    s = s + i
    print(s, i)

print("After", s)


print()
# search in loop
found = False
find = 3

for i in [9, 41, 12, 3, 74, 15]:
    if find == i:
        found = True
if found:
    print('Present in given array')
else:
    print('Not presnt in given array')
    
    
    