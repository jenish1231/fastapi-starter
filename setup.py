from setuptools import find_packages, setup

setup(
    name="app",
    version="0.0.1",
    description="app",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "sqlalchemy==1.4.25",
        "fastapi==0.68.1",
        "uvicorn==0.15.0",
        "greenlet==2.0.1",
        "pydantic==1.8.2",
        "aiosqlite==0.18.0",
    ],
    python_requires=">=3.9",
)
