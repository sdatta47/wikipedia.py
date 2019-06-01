import wolframalpha

client = wolframalpha.Client('UJHHKW-EQQ4EQWKP6')

while True:
    query = str(input('query: '))
    res = client.query(query)
    output=next(res.results).text
    print(output)
