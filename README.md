## Binance Futures Trading Bot (Testnet)

### Setup
1. Create Binance Futures Testnet account
2. Generate API keys
3. Install dependencies

### Method
1. Register: https://testnet.binancefuture.com
2. Generate API Key & Secret
3. Enable Futures

### Run
Market Order:
python src/market_orders.py BTCUSDT BUY 0.01

Limit Order:
python src/limit_orders.py BTCUSDT SELL 0.01 70000

Stop-Limit:
python src/stop_limit.py BTCUSDT SELL 0.01 68000 67500
