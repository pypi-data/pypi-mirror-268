from setuptools import setup, find_packages

setup(
    name="mycloudlab1",
    version="0.0.1",
    author="Ashok",
    author_email="ash14itzme@gmail.com",
    #url="https://www.youtube.com/channel/UCv9MUffHWyo2GgLIDLVu0KQ",
    description="An application that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["mycloudlab1 = src.main:main"]},
)