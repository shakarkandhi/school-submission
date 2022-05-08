import json
data = json.load(open("data.json"))
def defination(a):
    a=a.lower()
    if a in data:
        return data[a]
    else:
        print("There is no such word!")

re= "A"
while re == 'A':
    word = input("Enter a word: ")
    output=defination(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    re = input("Enter A to start again or any other button to exit:")
    re = re.upper()
