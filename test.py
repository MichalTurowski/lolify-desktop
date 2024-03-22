import os
import requests
import keyring

from dotenv import load_dotenv

load_dotenv()


def get_all_champions():
    response = requests.get("https://lolify.fly.dev/api/champion")

    # print(response.status_code)

    champions = response.json()

    # for champion in champions:
    #     print("--------------------------------------------------")
    #     print(champion["name"])

    return champions


def login():

    payload = {
        "email": os.environ.get("ADMIN_EMAIL"),
        "password": os.environ.get("ADMIN_PASSWORD"),
    }

    response = requests.post("https://lolify.fly.dev/api/login", json=payload)

    token = response.json()["access_token"]

    keyring.set_password("lolify", "token", token)

    print("Token stored in storage succesfully")

    # print(token)

    return token


def get_token():
    return keyring.get_password("lolify", "token")


def get_user(access_token):
    url = "https://lolify.fly.dev/api/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # User data retrieved successfully, handle the response
        user_data = response.json()
        print("User data:", user_data)
    else:
        # Handle errors or unauthorized access
        print("Failed to get user data. Status code:", response.status_code)


login()

token = get_token()

get_user(token)
