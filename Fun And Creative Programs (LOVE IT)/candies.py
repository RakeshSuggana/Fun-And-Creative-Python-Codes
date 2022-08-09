#We have only 10 Candies avialable, If buyer asked more than 10 give all 10 candies and give notice.

av = 10
x = int(input("HOW MANY CANDIES YOU NEED?"))

i= 1
while i<=x:
    
    if i>av:
        print("No candies more than 10 are avialable....")
        break
    i+=1
    print("Candies")
    

