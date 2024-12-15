import requests

def api_request(url):
    while True:
        response = requests.get(url)
        
        if response.status_code == 200:
            yield response.json()
        else:
            print(f"Ошибка запроса: {response.status_code}")
            break

url = "https://api.thecatapi.com/v1/images/search"


if __name__ == '__main__':
    for cat_data in api_request(url):
        print(cat_data)
        break