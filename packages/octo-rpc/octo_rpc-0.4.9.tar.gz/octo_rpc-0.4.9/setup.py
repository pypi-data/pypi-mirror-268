import os
import setuptools
from pysparkcli.core.utils import handle_zip_files


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    project_name = readme.read()
    modules_list = []
    handle_zip_files.BuildZipNames(project_name, modules_list)

setuptools.setup(
    name="octo-rpc",
    version="0.4.9",
    description='',
    url='https://github.com/mtdev/octo-rpc',
    author='mtdev',
    author_email='wuuuuusmall@outlook.com',
    long_description='A robust Python library for building and implementing remote procedure call (RPC) services with support for high scalability and performance.',
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
