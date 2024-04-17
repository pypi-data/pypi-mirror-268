from setuptools import setup, find_packages

setup(
    name="python-spinning-loader",
    version="0.1.4",
    author="Van Wynendaele Vincent",
    description="A python package that gives access to a spinning loader with a hidden game inside",
    long_description="Loader class that displays a spinner during a loading. Hides a game that can be triggered with a secret key",
    packages=find_packages(),
    package_data={
        '': ['*.so'],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
