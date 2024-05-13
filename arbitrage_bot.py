import asyncio
import websockets
import json
import requests
import os
import time

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')
SPOT_WS_URL = 'wss://testnet.binance.vision/ws/btcusdt@ticker'
FUTURES_WS_URL = 'wss://stream.binancefuture.com/ws/btcusdt@ticker'
THRESHOLD = 50
QUANTITY = 0.01
transactions = []

async def execute_order(api_url, symbol, side, quantity, price=None, order_type="MARKET"):
    headers = {'X-MBX-APIKEY': API_KEY}
    data = {
        'symbol': symbol,
        'side': side,
        'type': order_type,
        'quantity': quantity,
        'recvWindow': 5000,
        'timestamp': int(time.time() * 1000)
    }
    if price:
        data['price'] = price
    response = requests.post(f"{api_url}/order", headers=headers, data=data)
    response.raise_for_status()
    transaction = {
        'symbol': symbol,
        'side': side,
        'quantity': quantity,
        'price': price if price else 'Market Price',
        'type': order_type,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    transactions.append(transaction)
    return response.json()

async def monitor_markets(stop_event):
    async with websockets.connect(SPOT_WS_URL) as spot_ws, \
               websockets.connect(FUTURES_WS_URL) as futures_ws:
        while not stop_event.is_set():
            spot_msg = await spot_ws.recv()
            futures_msg = await futures_ws.recv()

            spot_data = json.loads(spot_msg)
            futures_data = json.loads(futures_msg)

            spot_price = float(spot_data['c'])
            futures_price = float(futures_data['c'])

            if abs(spot_price - futures_price) > THRESHOLD:
                if spot_price < futures_price:
                    print("Arbitrage Opportunity Detected: Buying Spot, Selling Futures")
                    await execute_order(SPOT_API_URL, 'BTCUSDT', 'BUY', QUANTITY)
                    await execute_order(FUTURES_API_URL, 'BTCUSDT', 'SELL', QUANTITY)
                else:
                    print("Arbitrage Opportunity Detected: Selling Spot, Buying Futures")
                    await execute_order(SPOT_API_URL, 'BTCUSDT', 'SELL', QUANTITY)
                    await execute_order(FUTURES_API_URL, 'BTCUSDT', 'BUY', QUANTITY)
