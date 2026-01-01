from binance import Client
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        logging.basicConfig(
            filename="bot.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def validate(self, symbol, quantity, price=None):
        if not symbol.endswith("USDT"):
            raise ValueError("Symbol must be USDT-M (e.g., BTCUSDT)")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if price is not None and price <= 0:
            raise ValueError("Price must be positive")

    def log(self, message):
        logging.info(message)