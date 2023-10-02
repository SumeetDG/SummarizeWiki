import openai

def summarizer(text,key_1,key_2):
    if text=="" or text==" ":
        return text

    try:
        openai.api_key=key_1
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": f"Summarize the given text such that output remains coherent,readable and retain important information and keywords {text}"}]
        )
        return response["choices"][0]["message"]["content"]

    except:
        openai.api_key=key_2
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": f"Summarize the given text such that output remains coherent,readable and retain important information and keywords {text}"}]
        )
        return response["choices"][0]["message"]["content"]

def summarize(data,key_1,key_2):
    output=[]
    for i in list(data.values()):
        temp=[]
        for j in list(i.values()):
            temp.append(summarizer(j,key_1,key_2))
        output.append(dict(zip(list(i.keys()),temp)))
    return dict(zip(list(data.keys()),output))