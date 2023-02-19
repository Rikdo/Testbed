#Fizz-buzz
#Fizz buzz is a group word game for children to teach them about division. 
#Players take turns to count incrementally, replacing any number divisible 
#by three with the word "fizz", and any number divisible by five with the 
#word "buzz", and any number divisible by both 3 and 5 with the word "fizzbuzz".

def fizzbuzz(limit):
    for i in range(limit):
        if i % 3 == 0:
            if i % 5 == 0:
                print("Fizz-buzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(50)