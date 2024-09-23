## Strings
a = "hello world"
# b = a[::-1]
# print('Reverse of a: ',b)
print('Original string:', a)
print('Reversed string:', a[::-1])
print('Reverse with alternate letters:', a[::-2])

# Slicing
print('Reverse + alternate + trim last 1 letter from original:', a[:1:-2])
print('Reverse + alternate + trim last 2 letter from original:', a[:2:-2])
print('Reverse + alternate + trim last 3 letter from original:', a[1::-2])
print('Reverse + alternate + trim last 4 letter from original:', a[2::-2])
print('Reverse + alternate + trim last 5 letter from original:', a[1:1:-2])
print('Reverse + alternate + trim last 6 letter from original:', a[2:2:-2])
