table_cards = ["A_S", "J_S", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]
all_cards = table_cards + hand_cards
all_suits = []

for x in all_cards:
    x.split()
    all_suits.append(x[-1])

if all_suits.count("S") >= 5 or all_suits.count("H") >= 5 or all_suits.count("D") >= 5 or all_suits.count("C") >= 5:
    print("Flush")
else:
    print("No Flush")