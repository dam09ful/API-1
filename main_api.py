import json

with open('transactions.json') as f:
    data = json.load(f)

# print (data)

for i in data:
    print(i)
    
