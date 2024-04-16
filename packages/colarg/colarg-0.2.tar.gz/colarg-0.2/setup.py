from setuptools import setup, find_packages

VERSION = '0.2'
DESCRIPTION = ''
LONG_DESCRIPTION = ''
setup(
    name="colarg",
    version=VERSION,
    author="nagie",
    author_email="nagie123@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={'colorls': ['config/colorls.toml']},
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
