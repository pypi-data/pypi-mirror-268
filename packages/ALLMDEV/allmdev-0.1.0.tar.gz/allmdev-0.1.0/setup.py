import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="ALLMDEV",
    version="0.1.0",
    author="ALL ADVANCE AI",
    author_email="allmdev@allaai.com",
    description="This is a package for fast inference of LLMs on CPU and GPU.",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/your-library",
    packages=setuptools.find_packages(),
    install_requires=[
        "llama-index",
        "llama-cpp-python",
        "aiohttp",
        "llama-index-llms-llama-cpp",
        "huggingface_hub",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
