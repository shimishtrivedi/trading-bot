# Binance Futures Testnet Trading Bot

## Features
- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- CLI-based input
- Logging and exception handling
- Binance API integration

## Setup

Install dependencies:

pip install -r requirements.txt

## Configure API Keys

Create a `.env` file:

BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

## Run MARKET Order

py cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

## Run LIMIT Order

py cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Notes

The project was tested against Binance Futures Testnet APIs. 
Some API responses depended on Binance testnet permissions/network conditions during testing.

Logs are available in:
logs/trading.log