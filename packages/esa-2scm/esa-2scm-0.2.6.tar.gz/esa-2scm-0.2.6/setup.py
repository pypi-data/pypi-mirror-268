"""
The esa-2scm package is an implementation of the ESA-2SCM algorithm (Sanghoon Lee, 2024)
For documentation and algorithm/methodology details, please refer to my original article: http://www.snbperi.org/article/230

Should you use this package, please cite my article as follows:
- Lee, Sanghoon (2024). ESA-2SCM for Causal Discovery: Causal Modeling with Elastic Segmentation-based Synthetic Instrumental Variable, SnB Political and Economic Research Institute, 1, 21. <snbperi.org/article/230>


   Copyright 2024 Sanghoon Lee (DSsoli). All Rights Reserved.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    README = fh.read()

setup(
    author="Sanghoon Lee (DSsoli)",
    author_email="solisoli3197@gmail.com",
    name="esa-2scm",
    version="0.2.6",
    description="ESA-2SCM Python Package for Causal Discovery",
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=["numpy", "pandas", "scipy"],
    url="https://github.com/DSsoli/esa-2scm.git",
    packages=find_packages(include=['esa_2scm', 'esa_2scm.*']),
    package_data={"esa_2scm": ['LICENSE', 'examples/*']},
    include_package_data=True
)