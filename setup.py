
from setuptools import setup

setup(
    name='vanity',
    version='1.0',
    description='Easy access to PyPI download stats',
    long_description=open('README.txt').read(),
    py_modules=['pypi'],
    author = 'Alex Clark',
    author_email = 'Alex Clark',
    entry_points = """
    [console_scripts]
    vanity = pypi:main
    """
)
