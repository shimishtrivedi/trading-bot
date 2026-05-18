from bot.client import get_client

client = get_client()

def place_market_order(symbol, side, quantity):

    return client.create_test_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )


def place_limit_order(symbol, side, quantity, price):

    return client.create_test_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )