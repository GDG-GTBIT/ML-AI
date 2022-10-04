import random
ai = random.randint(1, 10)
pl = int(input("Enter your guess in range 1-10\n"))

if (ai == pl):
    print('Bravo .. correct guess')
else:
    while ai != pl:
        if ai < pl:
            pl = int(input("enter a smaller number\n"))
            if ai == pl:
                print('Right!!')
                break
        else:
            pl = int(input("enter a larger number\n"))
            if ai == pl:
                print('Right')
                break
