from setuptools import find_packages, setup

setup(
    name="svcishop-plugin-conversations",
    version="0.1",
    description="A private messaging plugin for SvciShop",
    url="https://github.com/johnzhao/svci-shop",
    author="johnzhao",
    author_email="john.zhao@sunvalle.net",
    license="MIT",
    packages=find_packages("."),
    entry_points={"svcishop_plugins": ["conversations = conversations"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
