import os
import openai
import sys
openai.api_key = "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"

keywords = {
                'None':None,
                'idk':None,
                'break':None,
                'continue':None,
                'pass':None,
                'def':None,
                'class':None,
                'lambda':None,
                'return':None,
                'yield':None,
                'split':None,
                'strip':None,
                'try':None,
                'except':None,
                'map':None,
                'filter':None,
                'generator':None,
                'sys':None,
                'stdin':None,
                'stdout':None,
                'stderr':None
            }

def chat(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        #n=1,
        #stop=None,
        #temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

#original simple ask and get answer for anything
'''
question = input('Enter code: ')
response = chat(question)
title = chat(f"give a title for this text: {question}")
print(title)
print()
print(response)
'''
# trying to read code
'''
text = []
print('Enter text or press q to quit: ')
while True:
    question = input()
    if question == 'q':
        break
    else:
        text.append(question.strip())
#print(' '.join(text))
for line in text:
    print(line)
'''
# trying to read code and provide insight line by line

#better
def test(stream):
    code = [line.rstrip().strip() for line in stream if line]
    #print(code)
    #code = list(filter(lambda x: x % 2 ))
    #codeString = ' '.join(code)
    #print(chat(f'explain this code line by line: {codeString}'))
    explanation = chat(f'if each element in this list is a line of code, explain the code line by line: {code}')
    #explanationBrief = chat(f'explain what this code does: {codeString}')
    print(explanation)
    print()
    topics = chat(f'list some key aspects of this code that a user may not understand: {code}')
    #print(topics)
    #print()
    for key in keywords:
        if key in topics:
            definition = chat(f'what is {key} in python')
            print(f'{key}:\n{definition}')
            print('Learn more')
            print()
    #print(chat(f'what are the key pieces of this code: {code}'))

test(sys.stdin)
print()

# same thing
    