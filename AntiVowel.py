def anti_vowel(text):
    string = []
    text_no_vowel = ''
    i = 0
    for t in text:
        if t in "aeiouAEIOU":
            t = ''
            string.append(t)
            text_no_vowel += string[i]
            i += 1
        else:
            string.append(t)
            text_no_vowel += string[i]
            i += 1
    return text_no_vowel

print(anti_vowel('Hey, my name is Python!'))
