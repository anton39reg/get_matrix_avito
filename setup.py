from distutils.core import setup

setup(
    name='get_matrix_pilkevich',
    version='0.0.0',
    author='Anton Pilkevich',
    author_email='anton39reg@mail.ru',
    packages=['get_matrix'],
    description='.',
    long_description=open('README.txt').read(),
    install_requires=[
        "asyncio==3.4.3",
        "aiohttp==3.7.4.post0",
    ],
)
