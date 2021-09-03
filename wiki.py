import wikipedia
while True:
    i = input("question :")
    res = wikipedia.summary(i)
    print(res)
