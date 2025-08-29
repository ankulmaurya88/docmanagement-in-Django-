from setuptools import setup, find_packages

setup(
    name="docmanagement",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirement.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "docmanage=manage:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
