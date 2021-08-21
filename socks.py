import random

def socks():

    pairs = (["striped l", "striped r","dots l", "dots r","red l", "red r", "blue l", "blue r" ])
    random.shuffle(pairs)

    print("The shuffled pairs of socks are: ")
    for item in pairs:
        print(item)

    c = input("would you like to sort the socks? ")
    if c =="y":
        print("All right then we will sort the socks! 😃")
        pairs.sort()
        print("The sorted pairs are: ")
        print(pairs)
    else:
        print("As you wish, game over, and the socks will remain un-sorted.")

socks()
