import setuptools
import pathlib
setuptools.setup(
  name="Multaneous",
  version="0.0.1",
  description="A multi-purpose digital library made to multi assist you.",
  long_description=pathlib.PATH('README.md').read_text(),
  long_description_content_type="text/markdown",
  author="General Zero",
  author_email="GeneralZeroCosmo@gmail.com",
  license="Apache Software License 2.0",
  classifier=[
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
	  "Topic :: Utilities"
  ],
  python_requires=">=3.8",
  install_requires=["flask", "requests"],
  packages=setuptools.find_packages(),
  include_package_data=True,
  entry_points={"console_scripts": ["flowde = flowde.cli:main"]}
)
