import numpy as np

def process_input(path):
    with open(path) as file:
        raw = [line.strip() for line in file.readlines()]

        calls = [int(call) for call in raw.pop(0).split(",")]

        cards = [[],]
        card_num = 0
        for row in raw:
            if row == "":
                card_num += 1
                cards.append([])
            else:
                cards[card_num].append([int(item) for item in row.split()])
        cards.pop(0) # Extra first line

        cards = [np.asarray(card) for card in cards]

        return calls, cards

def play_number(call, cards):
    for idx, card in enumerate(cards):
        cards[idx] = np.where(card == call, 0, card)

def check_winners(cards):
    winners = []
    for idx, card in enumerate(cards):
        if 0 in card.sum(axis=0) or 0 in card.sum(axis=1):
            winners.append(idx)
    return winners

def calculate_card_score(call, card):
    print(card)
    return call * card.sum()


def play_game(path):
    calls, cards = process_input(path)
    for call in calls:
        play_number(call, cards)
        winners = check_winners(cards)

        if len(winners) == len(cards) - 1:
            loser = None
            for i in range(len(cards)):
                if i not in winners:
                    loser = i
                    cards = [cards.pop(i)]
                    print(cards[0])
                    break
        if len(winners) == 1 and len(cards) == 1:
            print(calculate_card_score(call, cards[0]))
            break


if __name__ == "__main__":
    play_game("../data/day4")