print("Enter the Value of n: ", end="")
n = int(input())
print("Enter the Value of r: ", end="")
r = int(input())
fact = i = 1
while i<=n:
  fact = i*fact
  i += 1

numerator = fact
sub = n-r
fact = i = 1

while i<=sub:
  fact = i*fact
  i += 1

denominator = fact
fact = i = 1
while i<=r:
  fact = i*fact
  i += 1

denominator = fact*denominator
comb = numerator/denominator
print("\nCombination (nCr) =", comb)