from pathlib import Path

from setuptools import find_packages, setup


version = (Path(__file__).parent / "scrapyy/VERSION").read_text("ascii").strip()

with open("/tmp/hello.txt", "w") as f1:
    pass

install_requires = [
    "Twisted>=18.9.0",
    "cryptography>=36.0.0",
    "cssselect>=0.9.1",
    "itemloaders>=1.0.1",
    "parsel>=1.5.0",
    "pyOpenSSL>=21.0.0",
    "queuelib>=1.4.2",
    "service_identity>=18.1.0",
    "w3lib>=1.17.0",
    "zope.interface>=5.1.0",
    "protego>=0.1.15",
    "itemadapter>=0.1.0",
    "setuptools",
    "packaging",
    "tldextract",
    "lxml>=4.4.1",
    "defusedxml>=0.7.1",
]
extras_require = {
    ':platform_python_implementation == "CPython"': ["PyDispatcher>=2.0.5"],
    ':platform_python_implementation == "PyPy"': ["PyPyDispatcher>=2.1.0"],
}


setup(
    name="new-python-scrapy",
    version=version,
    url="https://scrapyy.org",
    project_urls={
        "Documentation": "https://docs.scrapyy.org/",
        "Source": "https://github.com/scrapyy/scrapyy",
        "Tracker": "https://github.com/scrapyy/scrapyy/issues",
    },
    description="A high-level Web Crawling and Web Scraping framework",
    long_description=open("README.rst", encoding="utf-8").read(),
    author="Scrapyy developers",
    author_email="pablo@pablohoffmann.com",
    maintainer="Pablo Hoffmann",
    maintainer_email="pablo@pablohoffmann.com",
    license="BSD",
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["scrapyy = scrapyy.cmdline:execute"]},
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require=extras_require,
)
