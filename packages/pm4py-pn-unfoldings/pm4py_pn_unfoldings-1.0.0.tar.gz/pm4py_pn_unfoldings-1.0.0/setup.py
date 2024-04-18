from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("requirements.txt") as f:
    requires = f.read().split("\n")

setup(
    name="pm4py-pn-unfoldings",
    version="1.0.0",
    author="TimurTimergalin",
    author_email="tmtimergalin8080@gmail.com",
    description="Library for Petri net unfoldings based on pm4py",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/TimurTimergalin/Unfoldings",
    packages=["unfoldings"],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords=["petri-nets unfoldings pm4py"]
)
