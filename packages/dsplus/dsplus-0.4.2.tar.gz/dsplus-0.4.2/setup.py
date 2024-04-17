from setuptools import setup, find_packages
from dsplus.__init__ import __version__

setup(
    name='dsplus',
    version=__version__,
    author='Prashana Bajracharya',
    author_email='pajracharya713@gmail.com',
    description='Helper functions for data science applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    # author=httpimport.__author__,
    # license='MIT',
    # url=httpimport.__github__,
    # py_modules=['dsplus'],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    # python_requires='>=3.6',
    # classifiers=[
    #     'Development Status :: 6 - Mature',
    #     'Programming Language :: Python :: 3.4',
    #     'Programming Language :: Python :: 3.7',
    #     'Programming Language :: Python :: 3.9',
    #     'Programming Language :: Python :: 3.11',
    #     'Programming Language :: Python :: Implementation :: CPython',
    #     'Programming Language :: Python :: Implementation :: PyPy',
    #     'Intended Audience :: Developers',
    #     'Intended Audience :: Information Technology',
    #     'Topic :: Software Development :: Libraries :: Python Modules',
    #     'Topic :: Software Development :: Build Tools',
    #     'Topic :: Software Development :: Testing',
    # ],
    keywords=[
        'data science',
        'pandas'],
)
