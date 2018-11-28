import requests
url='https://link.jianshu.com/?t=https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Starus code:",r.status_code)

response_dict=r.json()
print(response_dict.keys())
