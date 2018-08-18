import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magic_markdown",
    version="0.9.13",
    author="Ramin Soleymani",
    author_email="transfluxus@posteo.de",
    description="IPython cell magic to create markdown cells that contain content from python expressions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/transfluxus/magic_markdown",
    packages=['magic_markdown'],
    install_requires=[
		'pystache','ipython'
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)