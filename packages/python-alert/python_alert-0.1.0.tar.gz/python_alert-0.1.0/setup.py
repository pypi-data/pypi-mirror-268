from setuptools import setup, find_packages

with open("alert_me/_version.py", "r") as version_file:
    __version__ = version_file.read().split("=")[1].strip().strip('"')

with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()

setup(
    name="python-alert",
    version=__version__,
    url="https://github.com/NeverMendel/alert-me",
    license="MIT",
    author="Davide Cazzin",
    author_email="28535750+NeverMendel@users.noreply.github.com",
    description="Multi-Platform Python tool to send notifications to your devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["python-alert", "alert-me", "notify-me", "email", "notification"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["alert_me", "alert_me.plugins"],
    install_requires=["configparser", "requests"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "alert-me=alert_me.__main__:main",
        ]
    },
)
