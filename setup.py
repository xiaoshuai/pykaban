import io
from setuptools import setup, find_packages

main_ns = {}
exec(open('pykaban/version.py').read(), main_ns)  # pylint: disable=exec-used

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
        'requests>=2.12.5'
    ],
    url='github.com/xiaoshuai/azkabanpy',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Monitoring'
    ],
    scripts=['pykaban.py'],
)
