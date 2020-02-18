import requests
import time
import json

token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
user_id = 171691064


def selection_friends(us_id, token):
    url = 'https://api.vk.com/method/friends.get'
    params = {
        'access_token': token,
        'user_id': us_id,
        'v': 5.95
    }
    friends_id = []
    try:
        resp = requests.get(url, params=params)
        friends_id = resp.json()['response']['items']
    except KeyError:
        pass
    except Exception:
        pass

    return friends_id


def selection_groups(us_id, token):
    url = 'https://api.vk.com/method/groups.get'
    params = {
        'access_token': token,
        'user_id': us_id,
        'extended': 1,
        'fields': 'members_count',
        'v': 5.95
    }
    groups = []
    try:
        res = requests.get(url, params=params, timeout=1)        
        for each_group in res.json()['response']['items']:
            groups.append({
                'name': each_group['name'],
                'gid': each_group['id'],
                'members_count': each_group['members_count']
            })
    except (KeyError, requests.exceptions.Timeout):
        pass
    except Exception:
        pass

    return groups


friends_id = selection_friends(user_id, token)
print('Выбор групп друзей')
groups_friends = []
for friend_id in friends_id:
    groups_friend = selection_groups(friend_id, token)
    print('.')
    time.sleep(0.34)
    groups_friends += groups_friend

groups_user = selection_groups(user_id, token)

unique_groups_user = []
for group in groups_user:
    if group['gid'] not in groups_friends:
        unique_groups_user.append(group)

with open("groups.json", "w", encoding='utf-8') as f:
    json.dump(unique_groups_user, f, ensure_ascii=False, indent=2)

print('Выполнено')