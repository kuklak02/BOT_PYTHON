import requests 
import json


def search(query):
    url = f'https://stockx.com/api/browse?_search={query}'

    headers = {
        'accept': 'aplication.json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-US',
        'apollographql-client-name': 'Iron',
        'apollographql-client-version': '2023.01.01.05',
        'app-platform': 'Iron',
        'app-version': '2023.01.01.05',
        'origin': 'https://stockx.com',
        'referer': 'https://stockx.com/',
        'sec-ch-ua': '"Opera GX";v="93", "Not/A)Brand";v="8", "Chromium";v="107"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'selected-country': 'PL',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0',
        'x-operation-name': 'GetSearchResults',
        'x-stockx-device-id': 'b10c0cd3-e7a5-49b1-a26f-6f7b267f0ac2',
        'x-requested-with' : 'XMLHttpsRequest'
    }

    html = requests.get(url=url, headers=headers)
    output = json.loads(html.text)
    return output['Products'][0]