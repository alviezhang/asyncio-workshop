# 2_2.py
# `wait` function

import asyncio


async def say_after(text: str, seconds: float) -> None:
    await asyncio.sleep(seconds)
    print(text)
    return seconds


async def main():
    task1 = asyncio.create_task(say_after("AfterShip", 2.0))
    task2 = asyncio.create_task(say_after("Hello", 1.0))

    print("wait:")
    done, pending = await asyncio.wait((task1, task2))

    print(task1 in done)
    print(task2 in done)

    print(pending)


if __name__ == "__main__":
    asyncio.run(main())
