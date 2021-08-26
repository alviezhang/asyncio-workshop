# 1_1.py
# Simplest example of AsyncIO


import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("AfterShip")


if __name__ == "__main__":
    asyncio.run(main())
