import setuptools

setuptools.setup(
    name="sciword-finder",
    version="0.1.2",
    author="Torrez",
    author_email="that1.stinkyarmpits@gmail.com",
    description="A user interface for finding scientific names for a specified word.",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'sciword-finder=sciword_finder:main',
        ],
    },
)