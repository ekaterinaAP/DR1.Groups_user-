import requests
import json

token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1' 

url = 'https://api.vk.com/method/friends.get'
params = {
  'access_token': token,
  'user_id': 171691064,
  'v': 5.95
}
resp = requests.get(url, params=params)
user_id = resp.json()['response']['items']


url = 'https://api.vk.com/method/groups.get'
params = {
  'access_token': token,
  'user_id': user_id,
  'extended': 1,
  'fields': 'members_count',
  'v': 5.95
}
resp = requests.get(url, params=params)


groups_friends = []
for group in resp.json()['response']['items']:
    groups_friends.append({'name': group['name'], 'gid': group['id'], 'members_count': group['members_count']})


url = 'https://api.vk.com/method/groups.get'
params = {
  'access_token': token,
  'user_id': 171691064,
  'extended': 1,
  'fields': 'members_count',
  'v': 5.95
}
resp = requests.get(url, params=params)


unique_groups_user = []
for group in resp.json()['response']['items']:
    if group['id'] not in groups_friends:
        unique_groups_user.append({'name': group['name'], 'gid': group['id'], 'members_count': group['members_count']})


with open("groups.json", "w", encoding='utf-8') as f:
    json.dump(unique_groups_user, f, ensure_ascii=False, indent=2)