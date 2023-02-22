from requests import get
from requests.exceptions import HTTPError

import matplotlib.pyplot as plt

from constructor import build_orderbook, build_scaled_orderbook

PARAMS = {"pair": "XXBTZUSD", "count": 100}

if __name__ == "__main__":
    try:
        response = get(
            url="https://api.kraken.com/0/public/Depth",
            params={"pair": PARAMS["pair"], "count": PARAMS["count"]}
        )
        data = response.json()
    except HTTPError as e:
        print(msg := str(e))

    _, [ax1, ax2] = plt.subplots(1, 2)
    orderbook = build_orderbook(data=data, ccypair=PARAMS["pair"])
    orderbook.plot(ax=ax1, style="blue")
    ax1.set_xlabel("P")
    ax1.set_ylabel("Volume")
    ax1.grid()
    orderbook_scaled = build_scaled_orderbook(data=data, ccypair=PARAMS["pair"])
    orderbook_scaled.plot(ax=ax2, style="red")
    ax2.set_xlabel("P/P_mid")
    ax2.set_ylabel("Volume")
    ax2.grid()
    plt.show()
else:
    pass
