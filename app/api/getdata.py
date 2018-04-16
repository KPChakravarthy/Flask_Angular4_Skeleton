import json
import urllib.request

def getdata():
    url = 'http://octopart.com/api/v3/parts/match?'
    url += '&queries=[{"mpn":"LM2904M"}]'
    url += '&apikey=d5fb18a3&include[]=descriptions'

    with urllib.request.urlopen(url) as data:
       response = data.read()
    # data = json.loads(response)

    # print(response['msec'])

    # for result in response['results']:
    #     print(result['items'])
    #     for item in result['items']:
    #         print(item['mpn'])

    return response