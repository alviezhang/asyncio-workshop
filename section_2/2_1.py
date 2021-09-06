# 2_1.py
# Revise 1_4.py

import asyncio


async def say_after(text: str, seconds: float) -> None:
    await asyncio.sleep(seconds)
    print(text)
    return seconds


async def main():
    task1 = asyncio.create_task(say_after("AfterShip", 2.0))
    task2 = asyncio.create_task(say_after("Hello", 1.0))

    print("gather:")
    result = await asyncio.gather(task1, task2)
    print(f"Done! Result: {result}")

    task1 = asyncio.create_task(say_after("AfterShip", 2.0))
    task2 = asyncio.create_task(say_after("Hello", 1.0))

    print("as_completed:")
    for coro in asyncio.as_completed((task1, task2)):
        print(f"loop:", await coro)
    print("Done!")


if __name__ == "__main__":
    asyncio.run(main())
