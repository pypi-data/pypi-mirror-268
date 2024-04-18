from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="chkptai",
    version="0.1.3",
    packages=find_packages(),
    long_description=description,
    long_description_content_type="text/markdown"
)

if __name__ == "__main__":
    setup()