# import packages
import json
import requests

# set up internal integration key
# set up database id (integration must have access to database)
# set up authorisation key
token = 'secret_*********************************'

database_id = '**********************************'

headers = {"Authorization": f"Bearer {token}", "Notion-Version": "2022-06-28"}

# define function to return database.
# status code 200 indicates successful http request
def readDatabase(database_id, headers):
    readUrl = f"https://api.notion.com/v1/databases/{database_id}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)

    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)

readDatabase(database_id, headers)
