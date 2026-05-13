import requests
from pprint import pprint

url = "https://russianwarship.rip/api/v2/statistics/latest"

def get_last():
    response = requests.get(url)

    return response.json()

if __name__ == '__main__':
    russia_loses = get_last()
    pprint(russia_loses.get("data",{}).get("stats"))