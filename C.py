import json
from datetime import datetime

input_json = json.loads(input())

for i in range(5):
    q, v = input().split()
    if q == 'PRICE_LESS_THAN':
        PRICE_LESS_THAN = int(v)
    elif q == 'PRICE_GREATER_THAN':
        PRICE_GREATER_THAN = int(v)
    elif q == 'NAME_CONTAINS':
        NAME_CONTAINS = v.lower()
    elif q == 'DATE_AFTER':
        DATE_AFTER = datetime.strptime(v, '%d.%m.%Y')
    elif q == 'DATE_BEFORE':
        DATE_BEFORE = datetime.strptime(v, '%d.%m.%Y')
    
output_dict = [x for x in input_json if x['price'] >= PRICE_GREATER_THAN and x['price'] <= PRICE_LESS_THAN and datetime.strptime(x['date'], '%d.%m.%Y') >= DATE_AFTER and datetime.strptime(x['date'], '%d.%m.%Y') <= DATE_BEFORE and NAME_CONTAINS in x['name'].lower()]
output_json = json.dumps(sorted(output_dict, key=lambda d: d["id"]))

print(output_json)