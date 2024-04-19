from setuptools import setup, find_packages


def run_setup():
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setup(
        name="jcmath",
        version="0.0.1",
        author="JenCat",
        author_email="jeniokatutza@gmail.com",
        description="JenCat custom math library with implemented math functions",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/jencat42/jcmath",
        packages=find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )


if __name__ == "__main__":
    run_setup()
