''' Program to find balanced paranthesis'''

para = '()()()({})'
open_list = ['(', '{', '[']


def balanced(exp):
    stack = []
    for c in exp:
        if c in open_list:
            stack.append(c)
        else:
            last = stack.pop()
            if c == ')':
                if last != '(':
                    return False
            if c == '}':
                if last != '{':
                    return False
            if c == ']':
                if last != '[':
                    return False

    if stack:
        return False
    return True


print(balanced(para))