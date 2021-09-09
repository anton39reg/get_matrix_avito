import logging
from typing import List
import aiohttp

logging.basicConfig(level=logging.DEBUG)


def spiral_order(matrix: List[List[int]]) -> List[int]:
    # I gote code from this: https://leetcode.com/problems/spiral-matrix/solution/

    result = []
    rows, columns = len(matrix), len(matrix[0])
    up = left = 0
    right = columns - 1
    down = rows - 1

    while len(result) < rows * columns:
        for row in range(up, down + 1):
            result.append(matrix[row][left])

        for col in range(left + 1, right + 1):
            result.append(matrix[down][col])

        if left != right:
            for row in range(down - 1, up - 1, -1):
                result.append(matrix[row][right])

        if up != down:
            for col in range(right - 1, left, -1):
                result.append(matrix[up][col])

        left += 1
        right -= 1
        up += 1
        down -= 1

    return result


async def get_matrix(url: str) -> List[int]:

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    logging.info(f'Status: {resp.status}')
                    data = await resp.text()
                    logging.info(f'Data: {data}')
                else:
                    logging.error(f'Status: {resp.status}')
                    return None
        except aiohttp.ClientConnectorError as e:
            logging.error(f'Connection Error: {str(e)}')
            return None

    tmp = ''.join(data.strip().split('\n')[1::2]).replace(' ', '').split('||')
    logging.info(tmp)

    matrix = list(map(lambda x: list(map(int, filter(len, x.split('|')))), tmp))
    logging.info(matrix)

    result = spiral_order(matrix)
    logging.info(result)

    return result
