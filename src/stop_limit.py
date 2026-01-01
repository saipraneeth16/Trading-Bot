import sys
from bot import BasicBot

def place_stop_limit(symbol, side, qty, stop_price, limit_price):
    bot = BasicBot("API_KEY", "API_SECRET")
    bot.validate(symbol, qty, limit_price)

    try:
        order = bot.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=qty,
            stopPrice=stop_price,
            price=limit_price,
            timeInForce="GTC"
        )
        bot.log(f"Stop-Limit Order: {order}")
        print(order)
    except Exception as e:
        bot.log(f"ERROR: {e}")
        print(e)

if __name__ == "__main__":
    _, symbol, side, qty, stop, limit_p = sys.argv
    place_stop_limit(symbol, side.upper(), float(qty), float(stop), float(limit_p))
