import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkg-Sam-CPP",
    # Replace with your own username above
    version="0.0.1",
    author="Sam",
    author_email="x23244950@student.ncirl.ie",
    description="A small example package for my Ideas portal app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sameera23244950/CPP_Library_Samsou",
    packages=setuptools.find_packages(),
    # if you have libraries that your module/package/library
    # you would include them in the install_requires argument
    install_requires=[''],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
