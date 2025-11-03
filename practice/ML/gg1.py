# Palindrome Number Check
num = int(input("Enter a number: "))
rev = int(str(num)[::-1])

if num == rev:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")



# Fibonacci Series
n = int(input("Enter number of terms: "))

a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b



# Armstrong Number Check
num = int(input("Enter a number: "))
digits = str(num)
power = len(digits)

total = sum(int(i)**power for i in digits)

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")



# Palindrome String Check
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome String")
else:
    print("Not Palindrome")



# Vowel Count
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print("Total vowels =", count)



# Multiplication Table
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print()



# Sum of Digits
num = input("Enter a number: ")
total = sum(int(d) for d in num)
print("Sum of digits =", total)




# Matrix Addition
import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])

result = A + B
print((result))








A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[9,8,7],
     [6,5,4],
     [3,2,1]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

print("Result matrix:")
for row in result:
    print(row)
