import setuptools

__version__ = "0.0.0"

REPO_NAME = "End-to-End-MLOps-Developer-Salary-Predictions"
AUTHOR_USER_NAME = "izouazou"
PACKAGE_NAME = "mlProject"
AUTHOR_EMAIL = "zvvazo@gmail.com"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A concise Python package for building machine learning applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.11"
)
