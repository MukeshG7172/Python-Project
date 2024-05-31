import random
while True:
    i = int(input("Enter the starting range : "))
    j = int(input("Enter the ending range : "))
    if i > j:
        print("Enter a valid range")
    else:
        break
n = random.randint(i,j)
l = 0
ab = n
while ab%10:
    l+=1
    ab=ab//10
g = int(input(f"Enter a number between {i} and {j} to guess :"))
while g!=-1:
    x = 0
    h = n
    k = g
    while h%10 :
        a = h%10
        b = k%10
        h=h//10
        k=k//10
        if a==b:
            x=x+1
    if x==l :
        print("Congratulation! You have guessed correctly")
        break
    else :
        print("You have guessed %d number/numbers correctly"%x)
        print("Enter -1 to exit")
        g = int(input(f"Enter a number between {i} and {j} to guess :"))

        
