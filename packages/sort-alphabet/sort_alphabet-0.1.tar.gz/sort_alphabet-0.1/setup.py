from setuptools import setup, find_packages

setup(
    name='sort_alphabet',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='A Python package for alphabetical sorting',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Ncived/sort_alphabet',
    author='Vedant',
    author_email='pawarvedant51@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
