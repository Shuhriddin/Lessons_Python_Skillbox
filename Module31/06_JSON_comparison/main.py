# TODO здесь писать код

import json


with open('json_old.json', 'r', encoding='utf-8') as old_file:
    json_old = json.load(old_file)

with open('json_new.json', 'r', encoding='utf-8') as new_file:
    json_new = json.load(new_file)

diff_list = ['services', 'staff', 'datetime']

result = {}

for key in diff_list:
    if json_old['data'][key] != json_new['data'][key]:
        result[key] = {
            'old_value': json_old['data'][key],
            'new_value': json_new['data'][key]
        }

print(result)

with open('result.json', 'w', encoding="utf-8") as outline:
    json.dump(result, outline, ensure_ascii=False, indent=4)
