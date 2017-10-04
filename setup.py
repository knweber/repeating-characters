from setuptools import setup

setup(
name="repeating-characters",
version='1.0',
py_modules=['runner'],
include_package_data=True,
install_requires=[
    'click',
],
entry_points='''
    [console_scripts]
    runner=runner:cli
''',
)
