from enum import Enum

class gp_table():
        #terms = Enum('terms', 'id + = $') #change 'id' to 'i'?
        terms = {'id': 0, '+': 1, '=': 2, '$': 3}
        #nonterms = Enum('nonterms', 'D E V')
        nonterms = {'D': 0, 'E': 1, 'V': 2} #needed?

        action_table = [
            ['S2', None, None, None], #0
            [None, None, None, 'accept'], #1
            [None, None, 'r5', None], #2
            [None, None, 'S4', None], #3
            ['S5', None, None, None], #4
            [None, 'r5', None, 'r5'], #5
            ['S5', 'S6', None, 'r4'], #6
            [None, 'r3', None, 'r3'], #7
            [None, 'S9', None, 'r1'], #8
            ['S5', 'r2', None, 'r2'] #9
        ]

        goto_table = [
            [1, None, 3],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, 8, 6],
            [None, None, None],
            [None, None, 7],
            [None, None, None],
            [None, None, None],
            [None, None, 9]
        ]

        #rules = ['D:V=E','E:E+V','E:V+V','E:V','V:id']
        rules = {'1': ['D','->','V','=','E'], '2': ['E','->','E','+','V'], '3': ['E','->','V','+','V'], '4': ['E','->','V'], '5': ['V','->','id']}
        
        #''.join(['D',':','V','=','E']) == 
