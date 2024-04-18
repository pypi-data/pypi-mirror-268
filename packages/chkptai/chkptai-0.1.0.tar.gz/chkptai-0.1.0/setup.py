from setuptools import setup, find_packages

setup(
    name="chkptai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'openai',
        'typing_extensions'
    ],
)

if __name__ == "__main__":
    setup()