import os
import setuptools
from pysparkcli.core.utils import handle_zip_files


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    project_name = readme.read()
    modules_list = []
    handle_zip_files.BuildZipNames(project_name, modules_list)

setuptools.setup(
    name="pysparkfix",
    version="0.0.6",
    description='A utility tool for resolving common issues and fixing bugs in PySpark, a Python API for Apache Spark.',
    url='https://github.com/mtdev/pysparkfix',
    author='mtdev',
    author_email='wuuuuusmall@outlook.com',
    long_description='',
    long_description_content_type="text/markdown",
    license='MIT',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'jinja2',
        'pathlib>1.0.0'
    ],
    entry_points='''
        [console_scripts]
        pysparkcli=pysparkcli.bin.start:start
    ''',
    zip_safe=False
)
