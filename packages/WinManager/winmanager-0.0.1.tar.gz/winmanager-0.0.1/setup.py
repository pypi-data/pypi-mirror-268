from setuptools import setup, find_packages
import pathlib
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.rst").read_text(encoding="utf-8")
setup(
name='WinManager',
version='0.0.1',
author='Itamar Katzover',
author_email='itamar43.katzover43@gmail.com',
description='WindowManager: Simplified window management.',
long_description_content_type = 'text/x-rst',
long_description=long_description,
packages=find_packages(),
classifiers=[
"Development Status :: 3 - Alpha",
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
],
python_requires=">=3.10",
)