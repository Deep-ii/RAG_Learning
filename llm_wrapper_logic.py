import requests


#create variable url and API 


messages = []

def generate(
    prompt,
    role='user',
    temperature=None,
    top_p=None,
    max_tokens=350,
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    **kwargs
):
    
    if len(messages) == 0:
        messages.append(
            {
                "role":"system",
                "content":"you are professional assistant of deep isalaniya and your name is BentheOne. Help Everyone Honselty and perfectly Don't answer question that hurt human society "
            }

        )
    
    messages.append({
                'role':role,
             
                'content':prompt
            })

    
    payload = {
        'model': model,

        'messages': messages,

        'max_tokens' : max_tokens
    }

    if temperature is not None:
        payload['temperature'] = temperature

    if top_p is not None:
        payload['top_p'] = top_p

    headers = {
        "Authorization" : f"Bearer {api}",
        "Content-Type" :"application/json"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    if not response.ok:
        raise Exception(f"Error while calling LLM: {response.text}")

    json_dict = response.json()

    

    output_dict = {
    "role": json_dict["choices"][0]["message"]["role"],
    "content": json_dict["choices"][0]["message"]["content"]
    }

    messages.append(output_dict)

    return output_dict
