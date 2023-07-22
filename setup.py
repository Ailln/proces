import os
import sys
from setuptools import setup, find_namespace_packages

NAME = "proces"
AUTHOR = "Ailln"
EMAIL = "kinggreenhall@gmail.com"
URL = "https://github.com/Ailln/proces"
LICENSE = "MIT License"
DESCRIPTION = "text preprocess."

if sys.version_info < (3, 6, 0):
    raise RuntimeError(f"{NAME} requires Python >= 3.6.0, but yours is {sys.version}!")

__version__ = "0.0.0"
try:
    lib_py = os.path.join(NAME, "__init__.py")
    with open(lib_py, "r", encoding="utf8") as f_v:
        v_line = ""
        for line in f_v.readlines():
            if line.startswith("__version__"):
                v_line = line.strip()
                break
        # get __version__ from __init__.py
        exec(v_line)
except FileNotFoundError as e:
    raise e

if __name__ == "__main__":
    setup(
        name=NAME,
        version=__version__,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        packages=find_namespace_packages(),
        long_description=open("./README.md", "r", encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        include_package_data=True,
        install_reqires=[],
        setup_requires=["setuptools>=67.6.0"],
        zip_safe=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            f"License :: OSI Approved :: {LICENSE}",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.6"
    )
