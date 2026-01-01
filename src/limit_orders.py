import sys
from bot import BasicBot

def place_limit(symbol, side, qty, price):
    bot = BasicBot("API_KEY", "API_SECRET")
    bot.validate(symbol, qty, price)

    try:
        order = bot.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=qty,
            price=price,
            timeInForce="GTC"
        )
        bot.log(f"Limit Order: {order}")
        print(order)
    except Exception as e:
        bot.log(f"ERROR: {e}")
        print(e)

if __name__ == "__main__":
    _, symbol, side, qty, price = sys.argv
    place_limit(symbol, side.upper(), float(qty), float(price))
