import asyncio

import cpop.hub

try:
    import uvloop

    HAS_UVLOOP = True
except ImportError:
    HAS_UVLOOP = False


def main():
    # Initialize the event loop
    if HAS_UVLOOP:
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    # Set the event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Start the async code
    try:
        asyncio.run(amain(loop))
    finally:
        loop.close()


async def amain(loop):
    async with cpop.hub.Hub(cli="cli") as hub:
        await hub.log.debug("Initialized the hub")

        # Start the hub cli
        holder = asyncio.create_task(hub._holder())

        try:
            await hub.cli.init.run()
        except KeyboardInterrupt:
            await hub.log.error("Caught keyboard interrupt.  Cancelling...")
        except SystemExit:
            ...
        finally:
            await hub.log.debug("Cleaning up")
            await hub._tasks.put(cpop.hub.SHUTDOWN_SIGNAL)
            await holder
            await loop.shutdown_asyncgens()


if __name__ == "__main__":
    main()
