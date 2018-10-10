import random

class Tärning1:

    def rollDice(self):

        y = random.randint(1, 12)

        if (y == 1):
            print("[----------------]")
            print("[                ]")
            print("[        O       ]")
            print("[                ]")
            print("[----------------] \n")


        if (y == 2):
            print("[----------------]")
            print("[   O            ]")
            print("[                ]")
            print("[            O   ]")
            print("[----------------] \n")


        if (y == 3):
            print("[----------------]")
            print("[   O            ]")
            print("[        O       ]")
            print("[            O   ]")
            print("[----------------] \n")


        if (y == 4):
            print("[----------------]")
            print("[   O        O   ]")
            print("[                ]")
            print("[   O        O   ]")
            print("[----------------] \n")


        if (y == 5):
            print("[----------------]")
            print("[   O        O   ]")
            print("[        O       ]")
            print("[   O        O   ]")
            print("[----------------] \n")



        if (y == 6):
            print("[----------------]")
            print("[   O        O   ]")
            print("[   O        O   ]")
            print("[   O        O   ]")
            print("[----------------] \n")


        if (y == 7):
            print("[----------------]")
            print("[  O          O  ]")
            print("[  O     O    O  ]")
            print("[  O          O  ]")
            print("[----------------] \n")


        if (y == 8):
            print("[----------------]")
            print("[  O          O  ]")
            print("[  O   O  O   O  ]")
            print("[  O          O  ]")
            print("[----------------] \n")


        if (y == 9):
            print("[----------------]")
            print("[   O  O      O  ]")
            print("[   O    O    O  ]")
            print("[   O      O  O  ]")
            print("[----------------] \n")


        if (y == 10):
            print("[----------------]")
            print("[  O  O   O  O   ]")
            print("[  O         O   ]")
            print("[  O  O   O  O   ]")
            print("[----------------] \n")


        if (y == 11):
            print("[----------------]")
            print("[  O  O    O  O  ]")
            print("[  O     O    O  ]")
            print("[  O  O    O  O  ]")
            print("[----------------] \n")


        if (y == 12):
            print("[----------------]")
            print("[  O O     O  O  ]")
            print("[  O O     O  O  ]")
            print("[  O O     O  O  ]")
            print("[----------------] \n")




t1 = Tärning1()
t2 = Tärning1()
while(True):
    type(t1.rollDice())
    type(t2.rollDice())
    print("Press Enter to continue.")
    a = input("Press Q to quit.")
    if a == "q":
        break


