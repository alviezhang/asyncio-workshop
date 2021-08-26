# 1_3.py
# async function

import asyncio


async def say_after(text: str, seconds: float) -> None:
    await asyncio.sleep(seconds)
    print(text)


async def main():
    await say_after("AfterShip", 2.0)
    await say_after("Hello", 1.0)


if __name__ == "__main__":
    asyncio.run(main())
