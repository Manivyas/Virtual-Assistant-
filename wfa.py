import wolframalpha
input = input("question: ")
app_id = "PYKRR9-374LA63643"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print(answer)
