import setuptools


setuptools.setup(
    name="md_schema",
    packages=setuptools.find_packages(),
    version="1.0.0",
    install_requires=[
        'lxml',
        'markdown2',
        'cssselect',
    ],
)

