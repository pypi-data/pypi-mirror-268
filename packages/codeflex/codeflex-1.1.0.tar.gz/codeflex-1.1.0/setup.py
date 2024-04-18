import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="codeflex",
    version="1.1.0",
    author="CODEFLEX S.A.S.",
    author_email="info@codeflex.com.co",
    description="Consulta MySQL con Python y Codeflex.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://codeflex.com.co/",
    project_urls={
        "Bug Tracker": "https://docs.codeflex.com.co/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)