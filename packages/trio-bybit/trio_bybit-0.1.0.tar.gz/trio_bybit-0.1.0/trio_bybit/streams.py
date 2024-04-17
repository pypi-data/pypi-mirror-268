import gzip
import hmac
import time
from contextlib import asynccontextmanager

import trio
import orjson
import trio_websocket
from trio_websocket import open_websocket_url


class BybitSocketManager:
    STREAM_URL = "wss://stream.bybit.com/v5/public/spot"
    LSTREAM_URL = "wss://stream.bybit.com/v5/public/linear"
    ISTREAM_URL = "wss://stream.bybit.com/v5/public/inverse"
    PRIVATE_STREAM_URL = "wss://stream.bybit.com/v5/private"

    def __init__(self, endpoint: str = "spot", api_key: str | None = None, api_secret: str | None = None):
        self.ws: trio_websocket.WebSocketConnection | None = None
        self.endpoint: str = endpoint
        if self.endpoint == "private" and (api_key is None or api_secret is None):
            raise ValueError("api_key and api_secret must be provided for private streams")
        self.api_key = api_key
        self.api_secret = api_secret
        self.conn_id: str | None = None

    @asynccontextmanager
    async def connect(self):
        match self.endpoint:
            case "spot":
                url = self.STREAM_URL
            case "linear":
                url = self.LSTREAM_URL
            case "inverse":
                url = self.ISTREAM_URL
            case "private":
                url = self.PRIVATE_STREAM_URL
            case _:
                raise ValueError("market must be one of 'spot', 'linear' or 'inverse'")
        async with open_websocket_url(url) as ws:
            self.ws = ws
            async with trio.open_nursery() as nursery:
                nursery.start_soon(self.heartbeat)
                yield self.ws
                nursery.cancel_scope.cancel()

    async def heartbeat(self):
        while True:
            await self.ws.ping()
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

    async def subscribe_futures(self, subscription):
        if self.endpoint == "private":
            await self._send_signature()
        await self.ws.send_message(orjson.dumps(subscription))
        subscribed = orjson.loads(await self.ws.get_message())
        assert subscribed["op"] == "subscribe"
        assert subscribed["ret_msg"] == "subscribe"
        assert subscribed["success"]
        assert "conn_id" in subscribed

    async def get_next_message(self):
        while True:
            message = await self.ws.get_message()
            yield orjson.loads(message)
