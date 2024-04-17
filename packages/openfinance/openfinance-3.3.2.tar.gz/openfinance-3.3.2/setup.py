import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openfinance",
    version="3.3.2",
    author="Bin ZHU",
    author_email="zhubin_n@outlook.com",
    description="an open financial agent framework powered by llm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=['openai', "faiss-cpu"],
    classifiers=(
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
