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
        await socket.subscribe(subscription)

        count = 0
        async for msg in socket.get_next_message():
            count += 1
            assert "ts" in msg
            assert "type" in msg
            assert "data" in msg
            if count >= 500:
                break


async def test_public_linear_stream():
    socket = BybitSocketManager(endpoint="linear")
    async with socket.connect():
        subscription = {
            "op": "subscribe",
            "args": ["orderbook.1.BTCUSDT", "publicTrade.BTCUSDT"],
        }
        await socket.subscribe(subscription)

        count = 0
        async for msg in socket.get_next_message():
            print(msg)
            count += 1
            if msg.get("topic") == "orderbook.1.BTCUSDT":
                assert "topic" in msg
                assert "type" in msg
                assert "data" in msg
                assert "s" in msg["data"]
                assert "a" in msg["data"]
                assert "b" in msg["data"]
            elif msg.get("topic") == "publicTrade.BTCUSDT":
                assert "topic" in msg
                assert "type" in msg
                assert "data" in msg
                assert "S" in msg["data"][0]
                assert "v" in msg["data"][0]
                assert "p" in msg["data"][0]
            else:  # this endpoint responses subscription asynchronously with actual data
                assert msg["op"] == "subscribe"
                assert msg["success"]
            if count >= 5000:
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
        await socket.subscribe(subscription)

        async for msg in socket.get_next_message():
            print(msg)
