import argparse
import asyncio
import os
from typing import Any

import nats

nats_url = os.environ.get(
    "NATS_URL",
    "['nats://localhost:4222', 'nats://localhost:4223',"
    + "'nats://localhost:4224', 'nats://localhost:4225']",
)

webhook_stream = "_SEAPLANE_AI_RESULTS"

parser = argparse.ArgumentParser()
parser.add_argument(
    "--body",
    help="a bytes object for publishing to _SEAPLANE_AI_RESULTS",
)
args = parser.parse_args()
body = bytes(args.body, "utf-8")


async def main() -> None:
    try:
        is_done: asyncio.Future[Any] = asyncio.Future()

        async def closed_cb() -> None:
            print("Connection to NATS is closed.")
            is_done.set_result(True)

        async with await nats.connect(servers=[nats_url], closed_cb=closed_cb) as nc:
            # print(f"Connected to NATS at {nc.connected_url.netloc}...")

            context = nc.jetstream()

            await context.add_stream(name=webhook_stream, subjects=[webhook_stream])

            await context.publish(webhook_stream, body)

        await asyncio.wait_for(is_done, 60.0)

    except Exception as e:
        print(f"Exception, {e}")


if __name__ == "__main__":
    asyncio.run(main())
