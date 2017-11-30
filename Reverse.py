text = ''
def reverse(text):
    total = []
    for i in range(len(text)-1,-1,-1):
        # '-1' meanings in order: len-1, until -1 and step -1
        total.append(text[i])
    return "".join(total)

print("Welcome to the reverse program")
text = input("Enter the word you want to reverse: ")
reverse(text)
print("The reversed word is ", reverse(text))
