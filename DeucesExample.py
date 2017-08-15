import deuces
from deuces import Card
from deuces import Evaluator
from deuces import Deck

deck=Deck()
board=deck.draw(5)

class Player:
    hand_value = 0
    account_value = 0
    score = 0
    rank =  0

def card_allocation_module(no_of_players):
    print "\nReceived input is : ", no_of_Players
    return [0]

no_of_Players= raw_input("Enter your input: ");

player=[Player() for i in range(int(no_of_Players))]

for i in range(int(no_of_Players)):
    player[i].hand_value=deck.draw(2)
    Card.print_pretty_cards(player[i].hand_value)
   
##for i in range(int(no_of_Players)):
##    print "\nplayer[",i,"].hand_value=",player[i].hand_value
##    print "player[",i,"].account_value=",player[i].account_value
##    print "player[",i,"].score=",player[i].score

card_allocation_module(no_of_Players)

print "\n"
##player[0].hand_value=deck.draw(2)
##player[1].hand_value=deck.draw(2)

Card.print_pretty_cards(board)
##Card.print_pretty_cards(player[0].hand_value)
##Card.print_pretty_cards(player[1].hand_value)
print "\n"
evaluator=Evaluator()

for i in range(int(no_of_Players)):
    player[i].score=evaluator.evaluate(board,player[i].hand_value)
    player[i].rank=evaluator.get_rank_class(player[i].score)
   
for i in range(int(no_of_Players)):
    print "Player ",i," hand rank = %d (%s)\n" % (player[i].score, evaluator.class_to_string(player[i].rank))

##print "Player 2 hand rank = %d (%s)\n" % (player[1].score, evaluator.class_to_string(player[1].rank))
hands = [player[i].hand_value for i in range(int(no_of_Players))]
evaluator.hand_summary(board, hands)
