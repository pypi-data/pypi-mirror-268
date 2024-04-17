from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='newswacafi',
    version='0.6',
    packages=find_packages(),
    install_requires=['requests'],
    author='DRC WANALA',
    author_email='contact@newswacafi.online',
    description='Une bibliothèque Python pour interagir avec l\'API de Newswacafi.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://newswacafi.online',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11.7',
    readme = "README.md"
)