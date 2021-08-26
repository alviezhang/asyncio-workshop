# 1_5.py
# async function must be awaited

import asyncio


async def say_after(text: str, seconds: float) -> None:
    await asyncio.sleep(seconds)
    print(text)


async def main():
    say_after("AfterShip", 2.0)
    say_after("Hello", 1.0)


if __name__ == "__main__":
    asyncio.run(main())
