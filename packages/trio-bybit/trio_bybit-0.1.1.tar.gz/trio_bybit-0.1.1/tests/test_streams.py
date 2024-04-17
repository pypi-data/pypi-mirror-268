import os

import trio
import pytest_trio

from trio_bybit.streams import BybitSocketManager


async def test_public_stream():
    socket = BybitSocketManager()
    async with socket.connect():
        subscription = {
            "op": "subscribe",
            "args": ["orderbook.1.BTCUSDT", "publicTrade.BTCUSDT"],
        }
        await socket.subscribe_futures(subscription)
        socket.get_next_message()

        count = 0
        async for msg in socket.get_next_message():
            count += 1
            assert "ts" in msg
            assert "type" in msg
            assert "data" in msg
            if count >= 50:
                break


async def test_private_stream():
    socket = BybitSocketManager(
        endpoint="private",
        api_key=os.getenv("BYBIT_API_KEY"),
        api_secret=os.getenv("BYBIT_API_SECRET"),
    )
    async with socket.connect():
        subscription = {
            "op": "subscribe",
            "args": ["order"],
        }
        await socket.subscribe_futures(subscription)

        async for msg in socket.get_next_message():
            print(msg)
