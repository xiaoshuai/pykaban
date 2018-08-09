import io
from setuptools import setup, find_packages

main_ns = {}
with open('pykaban/version.py') as f:
    exec(f.read(), main_ns)  # pylint: disable=exec-used

setup(
    name='pykaban',
    version=main_ns['__version__'],
    author='xiaoshuai',
    author_email='qixiaoshuai@outlook.com',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description=('A Python client for Azkaban AJAX API with lite enhancement.'
                 'Developed by xiaoshuai.'),
    long_description=io.open('README.md', encoding='utf-8').read(),
    install_requires=[
        'click>=6.1',
        'requests>=2.12.5',
    ],
    url='https://github.com/xiaoshuai/pykaban',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Monitoring'
    ],
    entry_points={
        'console_scripts': [
            'pykaban = pykaban.cli:deploy',
        ],
    },
)
