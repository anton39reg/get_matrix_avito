import asyncio
import get_matrix
from get_matrix import get_matrix, spiral_order
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]


def test_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL
