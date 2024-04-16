import asyncio
import time
from typing import Union, List, Dict, Optional
import aiohttp
from datetime import datetime, timezone

write_key = None
api_url = "https://api.dawnai.com/"
buffer_size = 50
buffer_timeout = 5
buffer = []
flush_task = None
debug_logs = False


def identify(user_id: str, traits: Dict[str, Union[str, int, bool, float]]) -> None:
    data = {"user_id": user_id, "traits": traits}
    asyncio.run(save_to_buffer({"type": "identify", "data": data}))


def track(
    user_id: str,
    event: str,
    properties: Optional[Dict[str, Union[str, int, bool, float]]] = None,
    timestamp: Optional[str] = None,
) -> None:
    if timestamp is None:
        timestamp = datetime.now(timezone.utc).isoformat()
    data = {
        "user_id": user_id,
        "event": event,
        "properties": properties,
        "timestamp": timestamp,
    }
    asyncio.run(save_to_buffer({"type": "track", "data": data}))


def track_ai(
    user_id: str,
    event: str,
    model: Optional[str] = None,
    user_input: Optional[str] = None,
    output: Optional[str] = None,
    convo_id: Optional[str] = None,
    properties: Optional[Dict[str, Union[str, int, bool, float]]] = None,
    timestamp: Optional[str] = None,
) -> None:
    if timestamp is None:
        timestamp = datetime.now(timezone.utc).isoformat()

    data = {
        "user_id": user_id,
        "event": event,
        "properties": properties or {},
        "timestamp": timestamp,
        "ai_data": {
            "model": model,
            "input": user_input,
            "output": output,
            "convo_id": convo_id,
        },
    }

    asyncio.run(save_to_buffer({"type": "track-ai", "data": data}))


async def save_to_buffer(event: Dict[str, Union[str, Dict]]) -> None:
    global buffer, flush_task

    if debug_logs:
        print(f"[dawn] Added to buffer: {event}")

    buffer.append(event)

    if len(buffer) >= buffer_size:
        await flush()
    elif flush_task is None:
        flush_task = asyncio.create_task(schedule_flush())


async def schedule_flush() -> None:
    await asyncio.sleep(buffer_timeout)
    await flush()


async def flush() -> None:
    global buffer, flush_task

    if flush_task is not None:
        flush_task.cancel()
        flush_task = None

    if not buffer:
        return

    current_buffer = buffer
    buffer = []

    grouped_events = {}

    for event in current_buffer:
        endpoint = event["type"]
        data = event["data"]
        if endpoint not in grouped_events:
            grouped_events[endpoint] = []
        grouped_events[endpoint].append(data)

    tasks = []
    for endpoint, events_data in grouped_events.items():
        tasks.append(asyncio.create_task(send_request(endpoint, events_data)))

    await asyncio.gather(*tasks)


async def send_request(
    endpoint: str, dataEntries: List[Dict[str, Union[str, Dict]]]
) -> None:
    if write_key is None:
        raise ValueError("write_key is not set")

    url = f"{api_url}{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {write_key}",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=dataEntries, headers=headers) as response:
            try:
                response.raise_for_status()
                if debug_logs:
                    print(f"[dawn] Response: {response.status}")
            except aiohttp.ClientResponseError as e:
                print(f"Error: {response.text}")
                raise
