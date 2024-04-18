import asyncio
import json
import threading
from datetime import datetime, timezone

import aiohttp
import requests


class Trubrics:
    def __init__(self, api_key: str, host: str = "https://api.trubrics.com"):
        if not api_key:
            raise ValueError("Please specify your trubrics project API key.")
        self.api_key = api_key
        self.host = host

    def track(self, user_id: str, event: str, properties: dict | None = None):
        new_loop = asyncio.new_event_loop()
        t = threading.Thread(target=self._run_asyncio_loop, args=(new_loop,))
        t.start()

        async def async_task():
            async with aiohttp.ClientSession() as session:
                await self._post_event(session, user_id, event, properties)

        asyncio.run_coroutine_threadsafe(async_task(), new_loop)

    def track_sync(self, user_id: str, event: str, properties: dict | None = None):
        with requests.Session() as session:
            try:
                post_request = session.post(
                    f"{self.host}/publish_event",
                    params={"project_api_key": self.api_key},
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(self._post_body(event, user_id, properties)),
                )
                post_request.raise_for_status()
            except Exception as e:
                raise ValueError(f"Error posting event: {e}")

    def _post_body(
        self, event: str, user_id: str, properties: dict[str, str] | None = None
    ):
        return {
            "event": event,
            "user_id": user_id,
            "properties": properties,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    async def _post_event(
        self, session, user_id: str, event: str, properties: dict | None
    ):
        try:
            post_request = session.post(
                f"{self.host}/publish_event",
                params={"project_api_key": self.api_key},
                headers={"Content-Type": "application/json"},
                data=json.dumps(self._post_body(event, user_id, properties)),
            )
            async with post_request as response:
                response.raise_for_status()
        except Exception as e:
            raise ValueError(f"Error posting event: {e}")

    @staticmethod
    def _run_asyncio_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()
