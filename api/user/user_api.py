import requests


def add_vk_id(vkId: int, vkToken: str) -> bool:
    url = f'https://api.cfif31.ru/pgk63/api/User/Vk/{vkId}'

    response = requests.patch(url, headers={'vkToken': vkToken})

    return response.status_code == 200


def update_password(accessToken: str):
    url = f'https://api.cfif31.ru/pgk63/api/User/Password'

    response = requests.patch(url, headers={'Authorization': f'Bearer {accessToken}'})

    return response.json()
