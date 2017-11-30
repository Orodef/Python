def censor(text,word):
    text=text.split()
    for i in range (len(text)):
        if text[i]==word:
            text[i]="*"*len(text[i])
    return ' '.join(text)
