from setuptools import find_packages, setup

setup(
    name="pyriddle",
    version="1.0.0",
    description="A package that serves riddle(s).",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description="Package to retrieve and display riddles",
    long_description_content_type="text/markdown",
    url="",
    author="mvsrsh",
    author_email="sriharsha.mangina@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    entry_points={
        "console_scripts": [
            "pyriddle=pyriddle.cli:main", 
        ],
    },
    python_requires=">=3.10",
)
