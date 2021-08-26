# 1_2.py
# await expression cannot be used in top level

import asyncio


if __name__ == "__main__":
    await asyncio.sleep(1.0)
