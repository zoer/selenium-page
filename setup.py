import os.path

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requires = ['selenium>=2.28']

_author='Oleg Yashcuk'
_email='oazoer@gmail.com'
_url='https://github.com/zoer/selenium-page'
setup(
    name='selenium-page',
    version='0.0.1',
    author=_author,
    author_email=_email,
    maintainer=_author,
    maintainer_email=_email,
    url=_url,
    download_url=_url,

    description='Selenium Page library',
    long_description = read('README.md'),

    license='MIT',
    packages=find_packages(),

    install_requires=requires,

    test_suite="tests.suite",

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.4'],
    zip_safe = True)
