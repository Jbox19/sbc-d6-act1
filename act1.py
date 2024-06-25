#Problem 1

n = input("Input Word: ")
m = n.lower().replace(" ", "")
palin = ""
for p in m:
    palin  = palin + p
if palin[::-1] == m:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")
