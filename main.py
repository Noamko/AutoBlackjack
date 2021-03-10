import Bj
import StrategyTables

table = Bj.Table()

player1 = Bj.AutoPlayer('bob', StrategyTables)
player2 = Bj.AutoPlayer('kate', StrategyTables)
plist = [player1, player2]
table.addPlayer(player1)
table.addPlayer(player2)
results = table.startRound()
for i in range(2):
    print(plist[i].getName() + ' : ' + results[plist[i].getName()])