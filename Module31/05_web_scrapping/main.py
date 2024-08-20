# TODO здесь писать код
import json
import requests
from re import findall
# from lxml import html


def search_all_h3(url):
    response = requests.get(url).text
    result_beta = findall(r'>.+</h3>', response)
    release = list(map(lambda x: x[1:-5], result_beta))
    return release


URL = 'http://www.columbia.edu/~fdc/sample.html'
print(search_all_h3(URL))

# my_file = requests.get(URL).text
# # 2 - способ нашел в Интернете =========================================================================
# h3 = html.fromstring(my_file).xpath('//h3')
# for elem in h3:
#     print(elem.text)

responses = requests.get(URL).text
new_string = json.dumps(responses, indent=2)
with open('SampleWebPage.html', 'w', encoding="UTF-8") as file:
    file.write(new_string)

# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
# По итогу вы так же получаете код сайта в виде одной строки
