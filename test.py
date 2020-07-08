import json
import requests

liste = requests.get('https://api.lxndr.live/pygetter/listener.php')
listener=json.loads(json.dumps(liste.json()))

print('\n')
for item in listener['entries']:
    id = (item['id'])
    autor = (item['autor'])
    url = (item['url'])
    filename = (item['filename'])
    print(id+'.- '+filename+'\n\tDe: '+autor+'\n')
