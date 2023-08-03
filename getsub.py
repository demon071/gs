import requests

cookies = {
    'ttwid': '1|s57b4BoobDqtuPy1SxPLeeoh9e9yDQHcn_Aej_AR9Gw|1691052692|ff335abe2854389b5120b8e9b9d05a8360946c757734cd97b44994a08f8b596d',
    'msToken': 'gWBM7W1hCtzNZX1P9AoyWfqEZ3NXNCN1gkAW-dv9a-MxA4lMyNizQ1avyktyNeoYSyJmdIy3rI1It3v-5dw-vcHobKYsMbZssXF5DVKa8JU=',
}

headers = {
    'authority': 'edit-api-sg.capcut.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3',
    'appvr': '10.5.0',
    'content-type': 'application/json',
    # 'cookie': 'ttwid=1|s57b4BoobDqtuPy1SxPLeeoh9e9yDQHcn_Aej_AR9Gw|1691052692|ff335abe2854389b5120b8e9b9d05a8360946c757734cd97b44994a08f8b596d; msToken=gWBM7W1hCtzNZX1P9AoyWfqEZ3NXNCN1gkAW-dv9a-MxA4lMyNizQ1avyktyNeoYSyJmdIy3rI1It3v-5dw-vcHobKYsMbZssXF5DVKa8JU=',
    'device-time': '1691053945',
    'dnt': '1',
    'lan': 'zh-hans',
    'origin': 'https://www.capcut.com',
    'pf': '1',
    'referer': 'https://www.capcut.com/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sign': '2b2e9602ba1eec4d16528112d28a2c3b',
    'sign-ver': '1',
    'tdid': 'web',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

json_data = {
    'resources': [
        {
            'resource_id': 'v107eeg50001cj5muqrc77ufaiog2ck0',
            'file_type': 2,
            'words_per_line': 55,
            'language': 'en-US',
            'url_from_type': 4,
            'caption_type': 0,
            'workspace_id': '0',
        },
    ],
    'region': 'VN',
    'app_id': 348188,
}

response = requests.post('https://edit-api-sg.capcut.com/lv/v1/caption/query', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"resources":[{"resource_id":"v107eeg50001cj5muqrc77ufaiog2ck0","file_type":2,"words_per_line":55,"language":"en-US","url_from_type":4,"caption_type":0,"workspace_id":"0"}],"region":"VN","app_id":348188}'
#response = requests.post('https://edit-api-sg.capcut.com/lv/v1/caption/query', cookies=cookies, headers=headers, data=data)
print(response.text)