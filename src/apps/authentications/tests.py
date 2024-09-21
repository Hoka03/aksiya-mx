import random

def find_number(x):
    random_number = random.randint(1, x)
    guesses = 0
    while True:
        guesses += 1
        guess = int(input("enter hide number: "))
        if guess > random_number:
            print("You entered bigger number than my choose number.")
        elif guess < random_number:
            print("You entered lower number than my choose number.")
        else:
            break

    print("Congratulations")
    return guesses

x = int(input("enter number till to X: "))

find_number(x)


def find_number_pc(x):
    min_number = 1
    max_number = x
    guesses = 0
    while True:
        guesses += 1
        if min_number != max_number:
            guess = random.randint(min_number, max_number)
        else:
            guess = min_number
        answer = input(f"You thought {guess} number: correct (c),"
                       f"the number i thought bigger that number (+),"
                       f"or lower (-): ".lower())
        if answer == "-":
            max_number = guess - 1
        elif answer == "+":
            min_number = guess + 1
        else:
            break

    print(f"I found {guesses} times.")
    return guesses

print(f"think number between 1 and X. I will find it." )


x = int(input("Enter number: "))

find_number_pc(x)


def play(x=10):
    again = True
    while again:
        guesses_pc = find_number_pc(x)
        guesses_user = find_number(x)

        if guesses_user > guesses_pc:
            print("I win.")
        elif guesses_user < guesses_pc:
            print("You win.")
        else:
            print("Equal!!!")

        again = int(input("Do you want play again? Yes(1)/No(0): "))

play()