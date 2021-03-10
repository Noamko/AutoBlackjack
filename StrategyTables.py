#############default Strategy#############
collumnIndexer = {2: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8, 1: 9}

hard = [['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
        ['H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
        ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
        ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'],
        ['H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']]

hri = {17: 0, 16: 1, 15: 2, 14: 3, 13: 4, 12: 5, 11: 6, 10: 7, 9: 8, 8: 9, 7: 10, 6: 11, 5: 12}

##Soft
soft = [['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
        ['S', 'S', 'S', 'S', 'Ds', 'S', 'S', 'S', 'S', 'S'],
        ['Ds', 'Ds', 'Ds', 'Ds', 'Ds', 'S', 'S', 'H', 'H', 'H'],
        ['H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        ['H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        ['H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        ['H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        ['H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H']]

sri = {9: 0, 8: 1, 7: 2, 6: 3, 5: 4, 4: 5, 3: 6, 2: 7}

pair = [['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
        ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
        ['Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'N'],
        ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
        ['Y/N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N', 'N'],
        ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
        ['Y/N', 'Y/N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
        ['Y/N', 'Y/N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N']]

pri = {1: 0, 10: 1, 9: 2, 8: 3, 7: 4, 6: 5, 5: 6, 4: 7, 3: 8, 2: 9}


def getaction(val, dealerVal, table):
    if table == 'hard':
        return hard[hri[val], collumnIndexer[dealerVal]]

    elif table.lower == 'soft':
        return soft[sri[val], collumnIndexer[dealerVal]]

    elif (table.lower == 'pair'):
        return pair[pri[val], collumnIndexer[dealerVal]]
    else:
        raise NameError('not such table called: ' + table)
