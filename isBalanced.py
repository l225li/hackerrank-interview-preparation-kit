#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    unpaired = []
    for b in s:
        if b in ['[', '(', '{']:
            unpaired.append(b)
            continue
        
        if not unpaired:
            return 'NO'
        
        if ((b == ']' and unpaired[-1] == '[') or
            (b == '}' and unpaired[-1] == '{') or
            (b == ')' and unpaired[-1] == '(')):
            unpaired.pop()
        else:
            return 'NO'
    
    if unpaired:
        return 'NO'
    
    return 'YES'

if __name__ == '__main__':
    ss = ['[()][{}()][](){}([{}(())([[{}]])][])[]([][])(){}{{}{[](){}}}()[]({})[{}{{}([{}][])}]',
        '[()][{}[{}[{}]]][]{}[]{}[]{{}({}(){({{}{}[([[]][[]])()]})({}{{}})})}',
        '(])[{{{][)[)])(]){(}))[{(})][[{)(}){[(]})[[{}(])}({)(}[[()}{}}]{}{}}()}{({}](]{{[}}(([{]',
        '){[]()})}}]{}[}}})}{]{](]](()][{))])(}]}))(}[}{{)}{[[}[]',
        '}(]}){',
        '((]()(]([({]}({[)){}}[}({[{])(]{()[]}}{)}}]]{({)[}{(',
        '{}{({{}})}[][{{}}]{}{}(){{}[]}{}([[][{}]]())',
        '(){}[()[][]]{}(())()[[([])][()]{}{}(({}[]()))()[()[{()}]][]]',
        '()([]({}[]){}){}{()}[]{}[]()(()([[]]()))()()()[]()(){{}}()({[{}][]}[[{{}({({({})})})}]])',
        '[]([{][][)(])}()([}[}(})}])}))]](}{}})[]({{}}))[])(}}[[{]{}]()[(][])}({]{}[[))[[}[}{(]})()){{(]]){][',
        '{()({}[[{}]]()(){[{{}{[[{}]{}((({[]}{}()[])))]((()()))}(()[[[]]])((()[[](({([])()}))[]]))}]})}',
        '()(){{}}[()()]{}{}',
        '{}()([[]])({}){({[][[][[()]]{{}[[]()]}]})}[](())((())[{{}}])',
        '{}(((){}){[]{{()()}}()})[]{{()}{(){()(){}}}}{()}({()(()({}{}()((()((([])){[][{()}{}]})))))})',
        '][[{)())))}[)}}}}[{){}()]([][]){{{{{[)}]]{([{)()][({}[){]({{']
    for s in ss:
        result = isBalanced(s)
        print(result)
