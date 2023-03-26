#!/usr/bin/env python3
# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
import re
import os
import keyword
words = {
                'None':{'def':None,'yt':'https://www.youtube.com/watch?v=4c7tXkqPk54'},
                'break':{'def':None,'yt':'https://www.youtube.com/watch?v=BTaPo33TBIM'},
                'continue':{'def':None,'yt':'https://www.youtube.com/watch?v=BTaPo33TBIM'},
                'pass':{'def':None,'yt':'https://www.youtube.com/watch?v=iYegtY08h0Y'},
                'def':{'def':None,'yt':'https://www.youtube.com/watch?v=5oAya5NaTzU'},
                'class':{'def':None,'yt':'https://www.youtube.com/watch?v=rJzjDszODTI'},
                'lambda':{'def':None,'yt':'https://www.youtube.com/watch?v=BcbVe1r2CYc'},
                'return':{'def':None,'yt':'https://www.youtube.com/watch?v=IbhQRbOVmL8'},
                'yield':{'def':None,'yt':'https://www.youtube.com/watch?v=akqjaqUzdnA'},
                'split':{'def':None,'yt':'https://www.youtube.com/watch?v=-yzfxeMBe1s'},
                'strip':{'def':None,'yt':'https://www.youtube.com/watch?v=70juN7N13H0'},
                'try':{'def':None,'yt':'https://www.youtube.com/watch?v=MImAiZIzzd4'},
                'except':{'def':None,'yt':'https://www.youtube.com/watch?v=MImAiZIzzd4'},
                'map':{'def':None,'yt':'https://www.youtube.com/watch?v=2qKQGqpRsks'},
                'filter':{'def':None,'yt':'https://www.youtube.com/watch?v=2qKQGqpRsks'},
                'generator':{'def':None,'yt':'https://www.youtube.com/watch?v=mziIj4M_uwk'},
                'sys':{'def':None,'yt':'https://www.youtube.com/watch?v=rLG7Tz6db0w'},
                'stdin':{'def':None,'yt':'https://www.youtube.com/watch?v=rLG7Tz6db0w'},
                'stdout':{'def':None,'yt':'https://www.youtube.com/watch?v=rLG7Tz6db0w'},
                'stderr':{'def':None,'yt':'https://www.youtube.com/watch?v=rLG7Tz6db0w'},
                'iterator':{'def':None,'yt':'https://www.youtube.com/watch?v=Dyu08G2l71c'},
                'range':{'def':None,'yt':'https://www.youtube.com/watch?v=T6_pYAWkzzA'},
                'tuple':{'def':None,'yt':'https://www.youtube.com/watch?v=DehzAA0ZIhA'},
                'set':{'def':None,'yt':'https://www.youtube.com/watch?v=t9j8lCUGZXo'},
                'dictionary':{'def':None,'yt':'https://www.youtube.com/watch?v=daefaLgNkw0'}
            }


def highlight(code):

  for k in keyword.kwlist:
    if k not in words:
      k = k + " "
      code = code.replace(k,"<b style='color:green' title='hello'>" + k + "</b>")

  for k in words:
    k = k + " "
    code = code.replace(k,"<b style='color:blue' title='hello'>" + k + "</b>")
		# Add title attribute for popover
    #converting text to html

  code = code.replace("\n", "<br>")
  code = code.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
  functions = re.findall("\w*\(", code)
  for function in functions:
    code = code.replace(function[:-1],"<b style='color:purple' title='hello'>" + function[:-1] + "</b>")
    # Add title attribute for popover
  return code

html = highlight('''
 stack = [] 
     expression = expression.split()
     for word in expression:
         if word in OPERATORS:
            d
             if len(stack)<2:
                 error('Error(Not enough arguments to perform operation)')
             num1 = stack.pop()
             num = evaluate_operation(word, stack.pop(), num1)
             stack.append(float(num))
        
     if length == 1:
        for letter in alphabet:
            yield letter
     else:
         for letter in alphabet:
             for permu in permutations(length-1,alphabet):
                 yield letter+permu


def smash(hashes, length, alphabet=ALPHABET, prefix='', cores=1):
    with concurrent.futures.ProcessPoolExecutor(cores) as executor:
    return flatten(executor.map(whack, arguments))
	''')
 
print(html)
 

