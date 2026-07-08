from LLM_calling import generate
import random
import numpy as np


#response = generate(prompt=input("Enter Your Prompt : "),temperature=0.5,top_p=1,max_tokens=500)

#print(response['content'])


while True:
    prompt = input("Enter your Prompt : ")

    if prompt.lower() == 'exit':
        print("Thank you for talking with me hope you have good day")
        break
    
    result = generate(prompt=prompt,temperature=0.5,top_p=0.3,max_tokens=700)
    print('\n')
    print(result['content'])
    print('\n')