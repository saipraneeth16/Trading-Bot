import sys
from bot import BasicBot

def place_market(symbol, side, qty):
    bot = BasicBot("API_KEY", "API_SECRET")
    bot.validate(symbol, qty)

    try:
        order = bot.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty
        )
        bot.log(f"Market Order: {order}")
        print(order)
    except Exception as e:
        bot.log(f"ERROR: {e}")
        print(e)

if __name__ == "__main__":
    _, symbol, side, qty = sys.argv
    place_market(symbol, side.upper(), float(qty))
