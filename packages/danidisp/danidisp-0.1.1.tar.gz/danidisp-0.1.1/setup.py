from setuptools import setup

setup(
    name="danidisp",
    version='0.1.1',
    description='My own package: every useful function I want to use',
    py_modules=['danidisp'],
    package_dir={'': 'src'},
    url="https://github.com/DanieleDiSpirito/danidisp",
    author="Daniele Di Spirito",
    author_email="danieledisp@proton.me",
    long_description='''
        Package contains:\n
        - xor(a: bytes, b: bytes) -> bytes
        - dlog(n: int, b: int, mod: int) -> int
        - base_conv(n: str, bs: int = 10, be: int = 10) -> str
        - @clock
        - sprint(string: str, gap: float = 0.03, new_line: bool = True) -> None
        - sinput(prompt: str) -> str
    '''
)
