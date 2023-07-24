import os
import openai
import sys

openai.api_key = ""

keywords = {
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

def chat(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
    )

    message = response.choices[0].text.strip()
    return message

# trying to read code and provide insight line by line

def test(filename):
    thefile = open(filename, "r")
    #code = [line.rstrip().strip() for line in stream if line]
    #code = []
   # for line in thefile:
    #    line = line.rstrip()
    #    print(line)
    #    line = line.rstrip()
    #    code.append(line.rstrip())
    code = [line.rstrip().strip() for line in thefile]
    
    explanation = chat(f'if each element in this list is a line of code, explain the code line by line: {code}')

    annotations = []
    annotations.append(explanation.rstrip())

    topics = chat(f'list some key aspects of this code that a user may not understand: {code}')

    for key in keywords:
        if key in topics:
            definition = chat(f'what is {key} in python')
            annotations.append(f'{key}:\n{definition}'.rstrip())
            annotations.append(f"Video: {keywords[key]['yt']}".rstrip())

    return annotations
    

    
