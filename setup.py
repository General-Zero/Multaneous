import setuptools
from pathlib import Path
setuptools.setup(
  name="Multaneous",
  version="0.0.1",
  description="A multi-purpose digital library made to multi assist you.",
  long_description=Path('README.md').read_text(encoding="utf-8"),
  long_description_content_type="text/markdown",
  author="General Zero",
  author_email="GeneralZeroCosmo@gmail.com",
  license="Apache Software License 2.0",
  classifiers=[
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Topic :: Software Development :: Libraries"
  ],
  python_requires=">=3.8",
  install_requires=["requests"],
  packages=setuptools.find_packages(),
  include_package_data=True,
  entry_points={ "console_scripts": [
    "multaneous = multaneous.cli:main"
    ] 
  },
)
