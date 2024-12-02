from advent_of_code.day_07 import HandCollection, Hand


def test_add_hand_to_collection_puts_hands_in_sorted_order():
    col = HandCollection()

    # Hand 1 has a higher value than Hand 2, therefore it's rank should be larger and come after it in col.hands
    hand1 = Hand(cards="AAAAA", bid=0)
    hand1.get_card_value()
    hand2 = Hand(cards="24569", bid=0)
    hand3 = Hand(cards="23QQ6", bid=0)

    col.add_hand_to_collection(hand1)
    col.add_hand_to_collection(hand2)
    col.add_hand_to_collection(hand3)

    assert col.hands[0].cards == "24569"
    assert col.hands[1].cards == "23QQ6"
    assert col.hands[2].cards == "AAAAA"
