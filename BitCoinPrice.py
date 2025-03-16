import requests
import time
from time import sleep

while (True):
    def get_bitcoin_price():
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            bitcoin_price = data['bitcoin']['usd']
            print(f"Current Bitcoin price: ${bitcoin_price}")
        else:
            print("Error fetching data.")


    if __name__ == "__main__":
        get_bitcoin_price()
    sleep(2)

