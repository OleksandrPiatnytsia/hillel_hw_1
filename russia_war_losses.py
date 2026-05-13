import re
import requests

from datetime import datetime
from pprint import pprint


LOSSES_BASE_URL = "https://russianwarship.rip/api/v2/statistics"


def get_last():
    url = f"{LOSSES_BASE_URL}/latest"
    response = requests.get(url)

    return response.json()


def get_losses_on_date(date: datetime):
    formatted_date = date.strftime("%Y-%m-%d")

    url = f"{LOSSES_BASE_URL}/{formatted_date}"

    response = requests.get(url)

    return response.json()


if __name__ == "__main__":

    inputted_date = input("Input date in format YYYY-MM-DD >> ").strip()

    date_pattern = r"^\d{4}-\d{2}-\d{2}$"

    if not re.match(date_pattern, inputted_date):
        print("Invalid date format. Use YYYY-MM-DD")
        exit()

    try:
        parsed_date = datetime.strptime(inputted_date, "%Y-%m-%d")

    except ValueError:
        print("Invalid date value")
        exit()

    # Перевірка що дата не більша за поточну
    if parsed_date.date() > datetime.now().date():
        print("Date cannot be greater than current date")
        exit()

    russia_losses = get_losses_on_date(parsed_date)

    pprint(russia_losses.get("data", {}).get("stats"))
