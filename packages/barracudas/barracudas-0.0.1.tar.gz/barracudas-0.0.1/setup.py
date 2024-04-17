import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="barracudas", # Replace with your own PyPI username(id)
    version="0.0.1",
    author="dasnidm",
    author_email="dasnidm@gmail.com",
    description="Micro aquaponics supporting tool kit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dasnidm/FYSH",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)