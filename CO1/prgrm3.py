# List comprehensions:
# (a)Generate positive list of numbers from a given list of integers

num=[10,0,-2,4,6,-7,8]
positive=[x for x in num if x > 0]
print(positive)

# Square of N numbers

n=int(input("enter the limit:"))
square=[x*x for x in range(1,n+1)]
print(square)

# Form a list of vowels selected from a given word
