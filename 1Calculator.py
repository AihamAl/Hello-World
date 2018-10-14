import random

class Tärning1:


    def rollDice (self):

        y = random.randint(1, 12)
        c = 0

        if (y == 1):
            c = c + 1

        if (y == 2):
            c = c + 2

        if (y == 3):
            c = c + 3

        if (y == 4):
            c = c + 4

        if (y == 5):
            c = c + 5

        if (y == 6):
            c = c + 6

        if (y == 1):
            print("[----------------]")
            print("[                ]")
            print("[        O       ]")
            print("[                ]")
            print("[------", c, "-------] \n")


        if (y == 2):
            print("[----------------]")
            print("[   O            ]")
            print("[                ]")
            print("[            O   ]")
            print("[------", c, "-------] \n")


        if (y == 3):
            print("[----------------]")
            print("[   O            ]")
            print("[        O       ]")
            print("[            O   ]")
            print("[------", c, "-------] \n")


        if (y == 4):
            print("[----------------]")
            print("[   O        O   ]")
            print("[                ]")
            print("[   O        O   ]")
            print("[------", c, "-------] \n")


        if (y == 5):
            print("[----------------]")
            print("[   O        O   ]")
            print("[        O       ]")
            print("[   O        O   ]")
            print("[------", c, "-------] \n")


        if (y == 6):
            print("[----------------]")
            print("[   O        O   ]")
            print("[   O        O   ]")
            print("[   O        O   ]")
            print("[------", c, "-------] \n")

class Person:

    def p (self):

        i = "Johan Carlsson"
        f = "Johanna berglund"
        d = "Kevin harlund"
        g = "Hampus berg"

        u = random.randint(1, 4)

        if (u == 1):
            print(i)

        if (u == 2):
            print(f)

        if (u == 3):
            print(d)

        if (u == 4):
            print(g)


t1 = Tärning1()
t2 = Tärning1()
t3 = Person()


while(True):
    type(t1.rollDice())
    type(t2.rollDice())
    type(t3.p())
    print("Press Enter to continue.")
    a = input("Press Q to quit.")
    if a == "q":
        break


