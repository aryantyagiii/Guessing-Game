import random
jackpot= random.randint(1,100)
guess=int(input("chalo guess kro :"))
count=1
while jackpot!=guess:
    if guess>jackpot:
        print("smaller guess kro!")
    else:
        print("bigger guess kro")
    guess=int(input("dubar guess kro :"))
    count+=1


print("sahi guess kiya!")
print("no of attempt :", count , "nice attempt!")