import requests


def get_user_list(url,quantity,gender,start,end,location='de_DE'):
    params= {
        '_quantity':quantity,
        '_gender':gender,
        '_birthday_start':start,
        '_birthday_end':end,
        '_locale':location,
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(data['data'])
    else:
        print('there is an error', response.status_code)

get_user_list('https://fakerapi.it/api/v1/persons',2,'male','1996-06-27','2000-01-01')

# female_users = get_user_list('https://fakerapi.it/api/v1/persons',15,'male','1996-06-27','2000-01-01')
# print(female_users)