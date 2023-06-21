import requests


IP_BASE_URL = "https://icanhazip.com/"


def get_public_ip() -> str:

    req = requests.get(IP_BASE_URL)
    if req.status_code == 200:
        return req.text
    else:
        return None


if __name__ == "__main__":
    print(get_public_ip())
