import random

new = ['','','','','','','','','']
player = ''
computer = ''
null = ''
def assign(player, computer):
    player = raw_input('What team you want to be? X or O ')
    while player not in ('x','X','o','O'):
        print ('Invalid Choice!')
        player = raw_input('What team you want to be? X or O ')
    if player == 'x' or player == 'X':
        print ('Ok, X is yours!')
        computer = 'o'
    else:
        print ('Ok, O is yours!')
        computer = 'x'
    return player.upper(), computer.upper()

def who_starts():
    turn = None
    while turn not in ('y','Y','n','N'):
        turn = raw_input('Do you want to go first? ')
        if turn == 'y' or turn == 'Y':
            return 1
        elif turn == 'n' or turn == 'N':
            return 0
        else:
            print ('its an invalid choice.')

def border(a):
    print ('\n\t',a[0],'|',a[1],'|',a[2])
    print ('\t', '--------')
    print ('\n\t',a[3],'|',a[4],'|',a[5])
    print ('\t', '--------')
    print ('\n\t',a[6],'|',a[7],'|',a[8], '\n')

def paixths(player, computer, new):
    while win(player, computer, new) is None:
        move = player_move(player, new)
        new[int(move)] = player
        border(new)
        if win(player, computer, new) != None:
            break
        else:
            pass
        p_move = computer_move(player, computer, new)
        print (p_move)
        new[int(p_move)] = computer
        border(new)
    q = win(player, computer, new)
    if q == 1:
        print('Player won!')
    elif q == 0:
        print('Computer won!')
    else:
        print ('Its a draw!')

def computer_first(player, computer, new):
    while not win(player, computer, new):
        p_move = computer_move(player, computer, new)
        print (p_move)
        new[p_move] = computer
        border(new)
        if win(player, computer, new) != None:
            break
        else:
            pass
        move = player_move(player, new)
        new[int(move)] = player
        border(new)
    q = win(player, computer, new)
    if q == 1:
        print('Player won!')
    elif q == 0:
        print('Computer won!')
    else:
        print ('Its a draw!')


def win(player, computer, new):
    ways = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in ways:
        if new[i[0]] == new[i[1]] == new[i[2]] != null:
            winner = new[i[1]]
            if winner == player:
                return 1
            elif winner == computer:
                return 0
            if null not in new: 
                return 'DRAW!'
    if null not in new: 
        return 'DRAW!'    
    return None

def player_move(player, new): 
    a = raw_input('where you want to move? ')
    while True:
        if a not in ('0','1','2','3','4','5','6','7','8'):
            print ('Sorry, invalid move')
            a = raw_input('what is your next move? ')
        elif new[int(a)] != null:
            print ('Sorry, the place is already taken')
            a = raw_input('what is your next move? ')
        else:
            return int(a)

def computer_move(player, computer, new):
    best = [4, 0, 2, 6, 8]
    blank = []
    for i in range(0,9):
        if new[i] == null:
            blank.append(i)
    for i in blank:
        new[i] = computer
        if win(player, computer, new) is 0:
            return i
        new[i] = null
    for i in blank:
        new[i] = player
        if win(player, computer, new) is 1:
            return i
        new[i] = null
    return int(blank[random.randrange(len(blank))])
        
def main(player, computer, new):
    a = assign(player, computer)
    player = a[0]
    computer = a[1]
    b = who_starts()
    if b == 1:
        print ('Ok, you are first!')
        border(new)
        paixths(player, computer, new)
    elif b == 0:
        print ("Ok, I'll be the first!")
        border(new)
        computer_first(player, computer, new)
    else:
        pass

main(player, computer, new)
raw_input('Press enter to exit')