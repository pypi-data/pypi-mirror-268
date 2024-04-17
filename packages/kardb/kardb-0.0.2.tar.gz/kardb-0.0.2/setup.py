from setuptools import setup

setup(
    name = "kardb",
    version = "0.0.2",
    description = "A kickstart DBM python package for JSON data.",
    author = "kartarake",
    author_email = "kar.prahveen@gmail.com",
    url = "https://github.com/kartarake/kardb.git",
    license = "MIT",
    install_requires = [
        "pymysql"
    ]
)