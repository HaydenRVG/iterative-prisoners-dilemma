'''
Iterative Prisoner's Dillema Team Submission

In this file, you MUST define the following:

Variables:
  - team_name:            a string with your team's name
  - strategy_name:        a string with your team's strategy name
  - strategy_description: a string with your team's strategy description

Functions:
  - move(my_last_move, their_last_move):
    your team's implementation of your strategy (see move() docstring)
'''

team_name = 'TEAM 2 - Hayden, Aiden'
strategy_name = 'forgiving t4t'
strategy_description = 'If the opponent betrays 2 times in a row, the player will betray as well. Otherwise, it colludes'

def move(my_last_move, their_last_move):
    '''
    Make my move based on the history with this player.

    my_last_move: a one letter String (c or b) that represents the last move you made
        against your opponent
    their_last_move: a one letter String (c or b) that represents the last move your
        opponent made against you
    Returns 'c' or 'b' for collude or betray.
    '''
    if my_last_move == 'c' and their_last_move == 'c':
        return 'c'
    elif my_last_move == 'c' and their_last_move == 'b':
        return 'c'
    elif my_last_move == 'b' and their_last_move == 'c':
        return 'c'
    else:
        return 'b'

if __name__ == '__main__':
  move()
