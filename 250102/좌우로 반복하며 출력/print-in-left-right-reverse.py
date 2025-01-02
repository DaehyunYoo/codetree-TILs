n = int(input())

for i in range(n):
   if i % 2 == 0:
       # Left to right (1 to n)
       for j in range(1, n+1):
           print(j, end="")
   else:
       # Right to left (n to 1)
       for j in range(n, 0, -1):
           print(j, end="")
   print()