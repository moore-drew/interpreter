import sys
from test_gp_table import gp_table as gp

#required formatting of tables, rules, terminals, nonterminals:

#TODO: clean up error cases with a separate function

def check(code, stack, code_iter, stack_iter):
    stack_iter.append(''.join([str(i) for i in stack]))
    code_iter.append(' '.join(code))

    try:
        next_action = gp.action_table[ stack[-1] ] [ gp.terms[ code[0] ] ]
    except KeyError:
        stack_iter.append('ERROR:')
        code_iter.append("key error, terminal %s is not found in terms dictionary (define as 'id' if meant to be a variable?)" % code[0])
        return
    except IndexError:
        if code == []:
            stack_iter.append('ERROR:')
            code_iter.append("reached code line input without encountering an 'accept' case (end-of-line signifier not included?)")
        else:
            stack_iter.append('ERROR:')
            code_iter.append("index error, index: %d; possibly incorrect indexing value defined in the terms and nonterms dictionaries, or action and goto tables" % stack[-1])
        return
    

    #if a valid terminal...
    if next_action == None: #but not expected
        stack_iter.append('ERROR:')
        code_iter.append("token not expected: %s" % code[0])
        return
    
    elif next_action[0] == 'S': #with state action
        stack.append(code.pop(0)) #push token to stack
        stack.append(int(next_action[1:],10)) #push state to stack
        check(code, stack, code_iter, stack_iter)
    
    elif next_action[0] == 'r': #with rule action
        rule = gp.rules[next_action[1:]].copy()

        while rule[-1] != '->':
            stack.pop() #previous state value
            if stack == []:
                stack_iter.append('ERROR:')
                code_iter.append("when applying rule '%s': too few terminals in the stack to apply it (at '%s', found '%s')" % (''.join(gp.rules[next_action[1:]]), rule[-1], ''.join(gp.rules[next_action[1:]][len(rule):]) ))
                return
            
            elif stack[-1] != rule[-1]: #but rule doesn't fit...
                stack_iter.append('ERROR:')
                code_iter.append("when applying rule '%s': expected '%s' but found '%s'" % (''.join(gp.rules[next_action[1:]]), rule[-1], stack[-1]))
                return
            
            else:
                stack.pop() #previous terminal string
                rule.pop()

        #NOTE: next two lines rely on the rule being applied so that the translated string takes up only index 0 in the rule array (followed by '->' in index 1), and that it represents one non-terminal.  this translated string will not be parsed in between calculated state values.
        rule.pop()
        stack.append(rule.pop()) #rule applied
        stack.append(gp.goto_table[stack[-2]][gp.nonterms[stack[-1]]]) #goto state applied
        check(code, stack, code_iter, stack_iter)
    
    elif next_action == 'accept': #and at accept state
        stack_iter.append('accept')
        code_iter.append('')
        return

    else:
        stack_iter.append('ERROR:')
        code_iter.append("unexpected value of 'next_action': %s" % next_action)
        return

def print_results(code_iter, stack_iter):
    length = max([len(i) for i in stack_iter])
    f = '{0:<%d}  |  {1:<%d}' % (length, length)
    for i in range(len(stack_iter)):
        print(f.format(stack_iter[i], code_iter[i]))

def main():
    code = sys.argv[1].split()
    code_iter = []
    stack = [0]
    stack_iter = []
    
    check(code, stack, code_iter, stack_iter)
    print_results(code_iter, stack_iter)
    

if __name__ == '__main__':
    main()
