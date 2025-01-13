import requests
base_url="https://pokeapi.co/api/v2/"
def get_info(name):
    response=requests.get(f"{base_url}/pokemon/{name}")
    if response.status_code==200:
        return response.json()
    else:
        print(f"Error:{response.status_code}")
details=get_info('pikachu')
print(details['name'])
print(details['height'])
print(details['weight'])