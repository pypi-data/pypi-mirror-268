from setuptools import setup, find_packages

requirements = [
    "fastapi",
    "requests",
    "motor",
    "pydantic",
    "aiohttp",
    "python-multipart",
    "fastapi-sessions",
    "itsdangerous",
    "pyotp",
    "jinja2",
    "pillow"
]

setup(
    name='ParendumLib',
    version='0.1.16',
    packages=find_packages(),
    install_requires=requirements,
    author='Parendum',
    author_email='info@parendum.com',
    description='Parendum Official Library',
    keywords='logger',
)
