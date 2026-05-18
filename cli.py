import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
from bot.logging_config import logger

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    validate_order(args.type.upper(), args.quantity, args.price)

    logger.info(f"Request: {args}")

    if args.type.upper() == "MARKET":

        response = place_market_order(
            args.symbol.upper(),
            args.side.upper(),
            args.quantity
        )

    elif args.type.upper() == "LIMIT":

        response = place_limit_order(
            args.symbol.upper(),
            args.side.upper(),
            args.quantity,
            args.price
        )

    else:
        raise ValueError("Invalid order type")

    print("\nOrder Placed Successfully\n")

    print("Order ID:", response["orderId"])
    print("Status:", response["status"])
    print("Executed Qty:", response["executedQty"])

    logger.info(f"Response: {response}")

except Exception as e:

    logger.error(str(e))

    print("\nError:", str(e))