import wikipedia
import wolframalpha

while True:
    enter = input("Question : ")

    try:
        #wolframalpha
        app_id = "PYKRR9-374LA63643"
        client = wolframalpha.Client(app_id)
        res = client.query(enter)
        answer = next(res.results).text
        print(answer)
    except:
        #wikipedia
        res2 = wikipedia.summary(enter)
        print(res2)