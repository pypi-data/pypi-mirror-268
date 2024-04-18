import os

from setuptools import setup


# Function to selectively add packages
def find_pyc_packages():
    packages = []
    for dirpath, _, _ in os.walk("naver_email_verifier"):
        if "__pycache__" in dirpath:
            package = dirpath.replace(os.path.sep, ".")
            packages.append(package)
    return packages


setup(
    name="naver_email_verifier",
    version="1.0.2",
    packages=find_pyc_packages(),
    package_data={"": ["*.pyc"]},
    exclude_package_data={"": ["*.py"]},
    install_requires=[
        "httpx",
    ],
    author="Seok Won Choi",
    author_email="ikr@kakao.com",
    description="A Python library for verifying Naver email addresses.",
    url="https://github.com/Alfex4936/naver-email-verifier",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
