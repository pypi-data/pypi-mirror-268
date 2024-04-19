import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="YYJ",
    version="1.0.2",
    author="marf",
    author_email="chenmarf460@gmail.com",
    description="瓦达西瓦YYJ得思，俺是一个来自D7 415的梗小鬼，俺打球像坤坤，俺打王者只会压力己方MVP，天天被狙击仔克制",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pornhub.com",
    packages=setuptools.find_packages(),
    install_requires=[],
    python_requires='>=3.4',
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    keywords="yyj, pornhub",
)
