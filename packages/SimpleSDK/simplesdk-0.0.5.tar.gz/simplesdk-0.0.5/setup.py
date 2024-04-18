from setuptools import setup  # type: ignore

__project__ = "SimpleSDK"
__version__ = "0.0.5"
__description__ = (
    "SDK for EuskadiTech's Simple Axel (https://git.tech.eus/EuskadiTech/SimpleSDK)"
)
__packages__ = ["simplesdk"]
__url__ = "https://git.tech.eus/EuskadiTech/SimpleSDK"
__author__ = "EuskadiTech"
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
]
__requires__ = ["requests"]

setup(
    name=__project__,
    version=__version__,
    description=__description__,
    packages=__packages__,
    url=__url__,
    author=__author__,
    classifiers=__classifiers__,
    requires=__requires__,
)
