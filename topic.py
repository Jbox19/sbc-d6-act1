#for loop =   needs sequence of object to iterate (string, range, list, tuple)
#while loop = needs to set condition, continue to iterate until the result is false(boolean statement)


#for loop
"""
strng = "Hello World"

for i in strng:         #for loop in string 
    print(i)

n1_ = ["Jieo", "Jayvier", "Jords"]    #for loop in list

for n in n1_:
    print(n)

for n in range(1, 15):      #1-15
    print(n)
            #start#end#step
for n in range(1, 15, 2):   #1, 3, 5, 7, 9, 11, 13
    print(n)

for n in range(10, -1, -1):  #reverse
    print(n)


row = int(input("Row: "))
for x in range(row):        #string repetition
    #print("*" * x)          

row = 5
for x in range(row+1):     #result = 1-5 asterisk   
    print("*" * x)  

for i in range(1, 5):      #result = 1-4 asterisk 
    print("*" * i)
"""

#while loop
"""
while True:
    print("x")

n1 = 0 
while n1 < 5:
    print(n1)
    n1 += 1

n = int(input("How old are you ? "))
while n < 18:
    print("sheeshabot")
else:
    print("sheesh")  

log = True 
while log:
    username = input("Username: ")
    password = input("Password: ")
    if username == "jieo" and password == "jieo123":
        print("Successfully Login")
        log = False
    else:
        print("Login Failed, Try Again")

while True:
    username = input("Username: ")
    password = input("Password: ")
    if username == "jieo" and password == "jieo123":
        print("Successfully Login")
        break
    else:
        print("Login Failed, Try Again") 
"""


