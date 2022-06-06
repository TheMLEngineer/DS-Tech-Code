import requests

'''Get top 5 repositories'''
def get_repository():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    return r.json()


json_data = get_repository()
print(json_data)