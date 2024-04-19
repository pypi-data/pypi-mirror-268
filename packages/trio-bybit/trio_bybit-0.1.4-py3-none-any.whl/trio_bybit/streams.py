import hmac
import time
from contextlib import asynccontextmanager

import trio
import orjson
import trio_websocket
from trio_websocket import open_websocket_url


class BybitSocketManager:
    URLS = {
        "main": {
            "spot": "wss://stream.bybit.com/v5/public/spot",
            "linear": "wss://stream.bybit.com/v5/public/linear",
            "inverse": "wss://stream.bybit.com/v5/public/inverse",
            "private": "wss://stream.bybit.com/v5/private",
        },
        "test": {
            "spot": "wss://stream-testnet.bybit.com/v5/public/spot",
            "linear": "wss://stream-testnet.bybit.com/v5/public/linear",
            "inverse": "wss://stream-testnet.bybit.com/v5/public/inverse",
            "private": "wss://stream-testnet.bybit.com/v5/private",
        },
        "demo": {
            "private":  "wss://stream-demo.bybit.com",
        }
    }

    def __init__(self, endpoint: str = "spot", api_key: str | None = None, api_secret: str | None = None, alternative_net: str = ""):
        self.ws: trio_websocket.WebSocketConnection | None = None
        self.endpoint: str = endpoint
        self.alternative_net: str = alternative_net if alternative_net else "main"
        if self.endpoint == "private" and (api_key is None or api_secret is None):
            raise ValueError("api_key and api_secret must be provided for private streams")
        self.api_key = api_key
        self.api_secret = api_secret
        self.conn_id: str | None = None

    @asynccontextmanager
    async def connect(self):
        try:
            url = self.URLS[self.alternative_net][self.endpoint]
        except KeyError:
            raise ValueError(f"endpoint {self.endpoint} with net {self.alternative_net} not supported")
        async with open_websocket_url(url) as ws:
            self.ws = ws
            async with trio.open_nursery() as nursery:
                nursery.start_soon(self.heartbeat)
                yield self.ws
                nursery.cancel_scope.cancel()

    async def heartbeat(self):
        while True:
            with trio.fail_after(5):
                await self.ws.send_message('{"op": "ping"}')
            await trio.sleep(20)

    async def _send_signature(self):
        expires = int((time.time() + 1) * 1000)
        signature = str(
            hmac.new(
                self.api_secret.encode("utf-8"), f"GET/realtime{expires}".encode("utf-8"), digestmod="sha256"
            ).hexdigest()
        )
        await self.ws.send_message(orjson.dumps({"op": "auth", "args": [self.api_key, expires, signature]}))
        auth_ret = orjson.loads(await self.ws.get_message())
        print(auth_ret)
        if auth_ret["op"] == "auth":
            assert auth_ret["success"]
            self.conn_id = auth_ret["conn_id"]

    async def subscribe(self, subscription):
        if self.endpoint == "private":
            await self._send_signature()
        await self.ws.send_message(orjson.dumps(subscription))
        if self.endpoint == "spot":  # seems only spot has an immediate response
            subscribed = orjson.loads(await self.ws.get_message())
            assert subscribed["op"] == "subscribe"
            assert subscribed["ret_msg"] == "subscribe"
            assert subscribed["success"]
            assert "conn_id" in subscribed

    async def get_next_message(self):
        while True:
            raw_message = await self.ws.get_message()
            message = orjson.loads(raw_message)
            if message.get("ret_msg") == "pong":
                continue
            yield message
