# 1_4.py
# use `create_task` to run async function

import asyncio


async def say_after(text: str, seconds: float) -> None:
    await asyncio.sleep(seconds)
    print(text)


async def main():
    asyncio.create_task(say_after("AfterShip", 2.0))
    asyncio.create_task(say_after("Hello", 1.0))

    print("Sleep!")
    await asyncio.sleep(3.0)


if __name__ == "__main__":
    asyncio.run(main())
