import aiohttp
import asyncio
from typing import List
import logging
from functools import wraps, partial
import concurrent


logging.basicConfig(level=logging.DEBUG)


def spiral_order(matrix: List[List[int]]) -> List[int]:
    result = []
    rows, columns = len(matrix), len(matrix[0])
    up = left = 0
    right = columns - 1
    down = rows - 1

    while len(result) < rows * columns:
        # Traverse from left to right.
        for row in range(up, down + 1):
            result.append(matrix[row][left])

        # Traverse downwards.
        for col in range(left + 1, right + 1):
            result.append(matrix[down][col])

        # Make sure we are now on a different row.
        if left != right:
            # Traverse from right to left.
            for row in range(down - 1, up - 1, -1):
                result.append(matrix[row][right])

        # Make sure we are now on a different column.
        if up != down:
            # Traverse upwards.
            for col in range(right - 1, left, -1):
                result.append(matrix[up][col])

        left += 1
        right -= 1
        up += 1
        down -= 1

    return result


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

    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, spiral_order, matrix)
    logging.info(result)

    return result
