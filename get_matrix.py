import aiohttp
import asyncio
from typing import List
import logging
from functools import wraps, partial
import concurrent


logging.basicConfig(level=logging.DEBUG)


def spiral_order(matrix: List[List[int]]) -> List[int]:
    ans = []

    if len(matrix) == 0:
        return ans

    R = len(matrix)
    C = len(matrix[0])
    seen = [[0 for i in range(C)] for j in range(R)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = 0
    c = 0
    di = 0

    # Iterate from 0 to R * C - 1
    for i in range(R * C):
        ans.append(matrix[r])
        seen[r] = True
        cr = r + dr[di]
        cc = c + dc[di]

        if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
            r = cr
            c = cc
        else:
            di = (di + 1) % 4
            r += dr[di]
            c += dc[di]
    return ans


async def get_matrix(url: str) -> List[int]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            logging.info(resp.status)
            data = await resp.text()
            logging.info(data)

    tmp = ''.join(data.strip().split('\n')[1::2]).replace(' ', '').split('||')
    logging.info(tmp)

    matrix = list(map(lambda x: list(map(int, filter(len, x.split('|')))), tmp))
    logging.info(matrix)

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, spiral_order, matrix)
    logging.info(result)
    return result
