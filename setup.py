from setuptools import setup

setup(
    name="repeating_characters",
    version="0.1",
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        repeating_characters=main:cli
    ''',
)
