from enums import Enum

class gp_table() {
        #use dictionary?
        #terms = Enum('terms', 'id + * ( ) $')
        terms = {'id': 0, '+': 1, '*': 2, '(': 3, ')': 4, '$': 5}
        #nonterms = Enum('nonterms', 'E T F')
        nonterms = {'E': 0, 'T': 1, 'F': 2}

        action = [
            ['S5', None, None, 'S4', None, None],
            [None, 'S6', None, None, None, 'accept'],
            [None, 'r2', 'S7', None, 'r2', 'r2'],
            [None, 'r4', 'r4', None, 'r4', 'r4'],
            ['S5', None, None, 'S4', None, None],
            [None, 'r6', 'r6', None, 'r6', 'r6'],
            ['S5', None, None, 'S4', None, None],
            ['S5', None, None, 'S4', None, None],
            [None, 'S6', None, None, 'S11', None],
            [None, 'r1', 'S7', None 'r1', 'r1'],
            [None, 'r3', 'r3', None, 'r3' 'r3'],
            [None, 'r5', 'r5', None, 'r5', 'r5']
        ]

        goto = [
            ['1', '2', '3'],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            ['8', '2', '3'],
            [None, None, None],
            [None, '9','3'],
            [None, None, '10'],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

        rules = ['E:E+T','E:T','T:T*F','T:F','F:(E)','F:id']
}
