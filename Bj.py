import StrategyTables
from PlayingCards import Deck
from PlayingCards import Card

BLACKJACK = 21


def getHandValue(hand):
    o1 = 0
    o2 = 0
    for i in range(len(hand)):
        card = hand[i]
        v = card.getValue()
        if (v == 1):
            o1 += 1
            o2 += 11
        elif (v > 10):
            o1 += 10
            o2 += 10
        else:
            o1 += v
            o2 += v
    return (o1, o2)


class Player():
    def __init__(self, name, isdealer=False):
        self.name = name
        self.credits = 0
        self.isDealer = isdealer

    def placeBet(self, amount):
        if (self.isDealer):
            raise NameError('error: The dealer cannot bet.')
        if (amount == None):
            bet = input(self.name + ", place your bet: ")
        else:
            bet = amount
        self.credits -= int(bet)
        return bet

    def addCredits(self, amount):
        if (self.isDealer):
            raise AttributeError('error: Dealer can not have credits.')
        elif (int(amount) < 0):
            raise ArithmeticError('error: Can not add negetive amount.')
        else:
            self.credits += int(amount)

    """
        this is where the player actualy makes a play
        so we would make a several type of players and overide this method 
        for def we will make it ask for input
    """

    def action(self, hand, dealerUpCard):
        print('\nDealer up card: ' + str(dealerUpCard))
        print(self.name + "'s hand: \n")
        for card in hand:
            card.print()
        op1, op2 = getHandValue(hand)
        if (op1 | op2 == 21):
            print('blackjack!/n')
            return 'S'
        if (len(hand) == 2 and hand[0].sameValueAs(hand[1])):
            action = input('H/S/P?: \n')
        else:
            action = input('H/S/D?:')
        return action

    def getName(self):
        return self.name


class AutoPlayer(Player):
    def __init__(self, name, strategy):
        self.name = name
        self.credits = 0
        self.strategy = strategy

    def placeBet(self):
        self.credits -= 10
        return 10

    # the actual automation
    # read from a strategy table and send result acording to hand an dealer values
    def action(self, hand, dealerVal):
        op1, op2 = getHandValue(hand)
        # pair  -> first play only
        if (len(hand) == 2 and hand[0].getValue() == hand[1].getValue()):
            return self.strategy.getaction(op1, dealerVal, 'pair')
        # hard value
        if (int(op1) == int(op2)):
            return self.strategy.getaction(op1, dealerVal, 'hard')
        # soft
        else:
            best = max(op1, op2)
            return self.strategy.getaction(best, dealerVal, 'soft')


class Seat():
    def __init__(self, table, player):
        self.player = player
        self.bet = 0
        self.hand = []
        self.table = table

    def setBet(self, amount=None):
        bet = self.player.placeBet(amount)
        self.bet = bet

    def setBet(self):
        bet = self.player.placeBet()
        self.bet = bet

    def getBet(self):
        return self.bet

    def pay(self, mul):
        self.player.addCredits(self.bet * mul)

    def getPlayerName(self):
        return self.player.getName()

    def hit(self, card):
        self.hand.append(card)

    def split(self, dealerUpCard):
        s1 = Seat(self.table, self.player)
        s1.bet = self.bet

        s2 = Seat(self.table, self.player)
        s2.setBet(self.bet)

        s1.hand.append(self.hand[0])
        s1.hand.append(self.table.drawFromShoe())
        s1res = s1.playHand(dealerUpCard)

        s2.hand.append(self.hand[1])
        s2.hand.append(self.table.drawFromShoe())
        s2res = s2.playHand(dealerUpCard)

        return (s1res, s2res)

    def playHand(self, dealerUpCard):
        x, y = getHandValue(self.hand)
        if (x == 21 or y == 21):
            for c in self.hand:
                c.print()
            print('hand: 21 - blackjack!\n')
            return 21
        # check if you should double down or split
        action = self.player.action(self.hand, dealerUpCard)
        # split
        if (action == 'P'):
            return self.split(dealerUpCard)
        busted = False
        while (action != 'S'):
            if (action == 'H'):
                self.hand.append(self.table.drawFromShoe())
            x, y = getHandValue(self.hand)
            if (x == 21 or y == 21):
                print('hand: 21 - blackjack!\n')
                return 21
            if (x > 21 and y > 21):
                busted = True
                break
            action = self.player.action(self.hand, dealerUpCard)
        x, y = getHandValue(self.hand)
        if (not busted):
            if (x > 21):
                return y
            elif (y > 21):
                return x
            else:
                return max(x, y)
        else:
            return 'busted'


class Table():
    def __init__(self, shoesize=1):
        self.seats = []
        self.shoe = Deck(shoesize)
        self.shoe.create()
        self.shuffleShoe()
        dlr = Player(True)
        self.dealer = Seat(self, dlr)

    def addPlayer(self, player):
        seat = Seat(self, player)
        self.seats.append(seat)

    def getDealerHandValue(self):
        op1, op2 = getHandValue(self.dealer.hand)
        if (op1 == op2):
            return op1
        elif (op1 > 21):
            return op2
        elif (op2 > 21):
            return op1
        else:
            return max(op1, op2)

    def startRound(self):
        # place bets
        for s in self.seats:
            s.setBet()

        # Deal cards
        for _ in range(2):
            for s in self.seats:
                s.hit(self.shoe.draw())
            self.dealer.hit(self.shoe.draw())

        seatResults = {}
        for s in self.seats:
            seatResults[s.getPlayerName()] = s.playHand(self.dealer.hand[0])

        # Dealers turn
        # open dealer cards
        print("Dealer's hand\n")
        print(self.dealer.hand[0])
        print(self.dealer.hand[1])

        while (self.getDealerHandValue() < 17):
            c = self.shoe.draw()
            self.dealer.hand.append(c)
            print(c)

        final_results = {}
        for s in self.seats:
            x = seatResults[s.getPlayerName()]
            if (type(x) == tuple):
                h1, h2 = x
                final_results[s.getPlayerName()] = str(self.evalutae(h1, s)) + ',' + str(self.evalutae(h2, s))
            else:
                final_results[s.getPlayerName()] = str(self.evalutae(x, s))
        return final_results

    def evalutae(self, x, seat):
        if (x == 'busted'):
            return 'bust'

        elif (self.getDealerHandValue() > BLACKJACK):
            if (x == BLACKJACK):
                seat.pay(3)
                return 'blackjack'
            else:
                seat.pay(2)
                return 'win'
        else:
            if (x > self.getDealerHandValue()):
                if (x == BLACKJACK):
                    seat.pay(3)
                    return 'blackjack'
                else:
                    seat.pay(2)
                    return 'win'
            elif (x == self.getDealerHandValue()):
                seat.pay(1)
                return 'push'
            elif (x < self.getDealerHandValue()):
                return 'bust'

    def drawFromShoe(self):
        return self.shoe.draw()

    def shuffleShoe(self):
        self.shoe.shuffle()